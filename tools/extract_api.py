#!/usr/bin/env python3
"""Extracts the public, reflected Voltweave API from the plugin headers and writes
   tools/generated/api.json   (machine readable, used by verify_docs.py)
   docs/api/reference.md      (the complete reference page)

Only declarations and their documentation comments are read. No implementation code is copied.

Usage: python tools/extract_api.py --product "<path to the Voltweave plugin folder>"
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Enum values whose header comment is missing. The wording follows the behaviour described in the concepts pages.
FALLBACK = {
    ("EVWVBatteryState", "Idle"): "Neither charging nor discharging.",
    ("EVWVBatteryState", "Charging"): "Storing surplus power from the network.",
    ("EVWVBatteryState", "Discharging"): "Supplying power to the network.",
    ("EVWVBatteryState", "Empty"): "No stored energy is left.",
    ("EVWVBatteryState", "Full"): "Fully charged.",
}


def pretty(name):
    """Unreal's display name rule: strip a leading b/E/F/U/A prefix where applicable, split camel case."""
    if re.match(r"^b[A-Z]", name):
        name = name[1:]
    out = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name)
    out = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", out)
    return out


def read_comment(lines, idx):
    """Documentation comment directly above line idx (a /** ... */ block or consecutive // lines)."""
    j = idx - 1
    while j >= 0 and not lines[j].strip():
        j -= 1
    if j < 0:
        return ""
    s = lines[j].strip()
    if s.endswith("*/"):
        k = j
        while k >= 0 and "/**" not in lines[k]:
            k -= 1
        block = " ".join(lines[k:j + 1])
        block = re.sub(r"/\*\*|\*/|^\s*\*", "", block)
        block = re.sub(r"\s*\*\s+", " ", block)
        return re.sub(r"\s+", " ", block).strip()
    return ""


def parse_header(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    items = []
    cls = None
    kind = None
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"\s*UCLASS\((.*)\)\s*$", line)
        if m:
            meta = m.group(1)
            j = i + 1
            while j < len(lines) and "class" not in lines[j]:
                j += 1
            cm = re.search(r"class\s+\w+_API\s+(\w+)\s*:\s*public\s+(\w+)", lines[j])
            if cm:
                dn = re.search(r'DisplayName\s*=\s*"([^"]+)"', meta)
                cls = {"name": cm.group(1), "parent": cm.group(2), "display": dn.group(1) if dn else None,
                       "doc": read_comment(lines, i), "members": [], "kind": "class", "file": os.path.basename(path)}
                items.append(cls)
                kind = "class"
            i += 1
            continue
        m = re.match(r"\s*USTRUCT\((.*)\)\s*$", line)
        if m:
            j = i + 1
            while j < len(lines) and "struct" not in lines[j]:
                j += 1
            sm = re.search(r"struct\s+\w+_API\s+(\w+)", lines[j])
            if sm:
                cls = {"name": sm.group(1), "parent": None, "display": None, "doc": read_comment(lines, i),
                       "members": [], "kind": "struct", "file": os.path.basename(path)}
                items.append(cls)
            i += 1
            continue
        m = re.match(r"\s*UENUM\((.*)\)\s*$", line)
        if m:
            j = i + 1
            em = re.search(r"enum class\s+(\w+)", lines[j])
            if em:
                enum = {"name": em.group(1), "doc": read_comment(lines, i), "values": [], "kind": "enum",
                        "file": os.path.basename(path)}
                k = j + 1
                while k < len(lines) and "};" not in lines[k]:
                    vm = re.match(r"\s*(\w+)\s*(=\s*[^,]+)?,?\s*$", lines[k])
                    if vm and not lines[k].strip().startswith(("/", "*", "{")):
                        enum["values"].append({"name": vm.group(1), "doc": read_comment(lines, k)})
                    k += 1
                items.append(enum)
                i = k
            continue
        m = re.match(r"\s*DECLARE_DYNAMIC_MULTICAST_DELEGATE(\w*)\((.*)\)\s*;", line)
        if m:
            args = [a.strip() for a in m.group(2).split(",")]
            items.append({"kind": "delegate", "name": args[0], "params": args[1:], "file": os.path.basename(path)})
            i += 1
            continue
        m = re.match(r"\s*(UPROPERTY|UFUNCTION)\((.*)\)\s*$", line)
        if m and cls is not None:
            spec = m.group(2)
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            decl = lines[j].strip()
            k = j
            while not re.search(r"[;{]\s*(//.*)?$", lines[k]) and k < j + 4:
                k += 1
                decl += " " + lines[k].strip()
            decl = re.sub(r"\{.*$", "", decl).rstrip("; ").strip()
            doc = read_comment(lines, i)
            dn = re.search(r'DisplayName\s*=\s*"([^"]+)"', spec)
            members = cls["members"]
            if m.group(1) == "UFUNCTION":
                fm = re.search(r"(\w+)\s*\(", decl)
                if not fm:
                    i += 1
                    continue
                fname = fm.group(1)
                if fname.startswith("OnRep_") or "BlueprintCallable" not in spec and "BlueprintPure" not in spec:
                    i += 1
                    continue
                members.append({"type": "function", "name": fname, "display": dn.group(1) if dn else pretty(fname),
                                "signature": decl, "pure": "BlueprintPure" in spec, "doc": doc,
                                "static": decl.startswith("static")})
            else:
                if "Transient" in spec and "EditAnywhere" not in spec and "BlueprintAssignable" not in spec:
                    i += 1
                    continue
                visible = any(f in spec for f in ("EditAnywhere", "EditDefaultsOnly", "VisibleAnywhere",
                                                   "BlueprintReadOnly", "BlueprintAssignable", "Config"))
                if not visible:
                    i += 1
                    continue
                pm = re.match(r"(.+?)\s+(\w+)(\s*=\s*.+)?$", decl)
                if not pm:
                    i += 1
                    continue
                ptype, pname = pm.group(1), pm.group(2)
                default = pm.group(3).strip(" =") if pm.group(3) else ""
                cat = re.search(r'Category\s*=\s*"([^"]+)"', spec)
                members.append({"type": "event" if "BlueprintAssignable" in spec else "property", "name": pname,
                                "display": dn.group(1) if dn else pretty(pname), "ctype": ptype,
                                "default": default, "category": cat.group(1) if cat else "",
                                "editable": "EditAnywhere" in spec or "EditDefaultsOnly" in spec,
                                "readonly_runtime": "VisibleAnywhere" in spec, "config": "Config" in spec, "doc": doc})
        i += 1
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", required=True, help="path of the Voltweave plugin folder")
    args = ap.parse_args()
    public = os.path.join(args.product, "Source", "Voltweave", "Public")
    version = json.load(open(os.path.join(args.product, "Voltweave.uplugin"), encoding="utf-8-sig"))["VersionName"]
    api = {"version": version, "classes": [], "enums": [], "delegates": []}
    for dirpath, _, files in os.walk(public):
        for f in sorted(files):
            if not f.endswith(".h"):
                continue
            for it in parse_header(os.path.join(dirpath, f)):
                if it["kind"] in ("class", "struct"):
                    api["classes"].append(it)
                elif it["kind"] == "enum":
                    api["enums"].append(it)
                else:
                    api["delegates"].append(it)
    api["classes"].sort(key=lambda c: c["name"])
    api["enums"].sort(key=lambda c: c["name"])
    os.makedirs(os.path.join(ROOT, "tools", "generated"), exist_ok=True)
    json.dump(api, open(os.path.join(ROOT, "tools", "generated", "api.json"), "w", encoding="utf-8"), indent=1)

    md = []
    md.append("# Complete reference\n")
    md.append(f"Generated from the public headers of Voltweave {version}. Every name on this page exists in that version.\n")
    md.append("Blueprint names are the display names Unreal shows in the editor. *Server only* means the call has an effect only where the grid is simulated (the server or a standalone game); on a client it logs a warning and does nothing.\n")
    md.append("## Enumerations\n")
    for e in api["enums"]:
        md.append(f"### `{e['name']}`\n")
        if e["doc"]:
            md.append(e["doc"] + "\n")
        md.append("| Value | Meaning |\n|---|---|")
        for v in e["values"]:
            doc = v["doc"] or FALLBACK.get((e["name"], v["name"]), "")
            md.append(f"| `{v['name']}` | {doc} |")
        md.append("")
    dgs = {d["name"]: d for d in api["delegates"]}
    for c in api["classes"]:
        title = c["display"] or c["name"]
        md.append(f"## {title} (`{c['name']}`)\n")
        if c["parent"] and c["kind"] == "class":
            md.append(f"Derives from `{c['parent']}`. Header: `{c['file']}`.\n")
        if c["doc"]:
            md.append(c["doc"] + "\n")
        props = [m for m in c["members"] if m["type"] == "property"]
        evs = [m for m in c["members"] if m["type"] == "event"]
        fns = [m for m in c["members"] if m["type"] == "function"]
        if props:
            md.append("**Properties**\n\n| Name | Type | Default | Description |\n|---|---|---|---|")
            for p in props:
                mode = "editable" if p["editable"] else ("runtime state" if p["readonly_runtime"] else "read only")
                d = p["default"].replace("|", "\\|") if p["default"] else ""
                dflt = f"`{d}`" if d else ""
                md.append(f"| {p['display']} (`{p['name']}`) | `{p['ctype']}` | {dflt} | {p['doc']} *({mode})* |")
            md.append("")
        if evs:
            md.append("**Events**\n\n| Name | Parameters | Description |\n|---|---|---|")
            for e in evs:
                dg = dgs.get(e["ctype"])
                params = ""
                if dg:
                    ps = dg["params"]
                    params = ", ".join(f"`{ps[k]} {ps[k + 1]}`" for k in range(0, len(ps) - 1, 2))
                md.append(f"| {e['display']} (`{e['name']}`) | {params} | {e['doc']} |")
            md.append("")
        if fns:
            md.append("**Functions**\n\n| Blueprint name | C++ signature | Description |\n|---|---|---|")
            for f in fns:
                sig = f["signature"].replace("|", "\\|")
                tag = " *(pure)*" if f["pure"] else ""
                md.append(f"| {f['display']}{tag} | `{sig}` | {f['doc']} |")
            md.append("")
    open(os.path.join(ROOT, "docs", "api", "reference.md"), "w", encoding="utf-8", newline="\n").write("\n".join(md) + "\n")
    print("classes:", len(api["classes"]), "enums:", len(api["enums"]), "version:", version)


if __name__ == "__main__":
    main()
