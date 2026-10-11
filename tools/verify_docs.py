#!/usr/bin/env python3
"""Consistency checks of the documentation against the generated API data (tools/generated/api.json).

Checks
  1. Every C++ type name (UVWV..., AVWV..., FVWV..., EVWV...) mentioned in a page exists in the API.
  2. Every **bold** or *italic* phrase that looks like a Blueprint name, property or enum value is a known name.
  3. Every C++ code block either includes a snippet file or consists of lines that appear in a snippet file.
  4. The version named in the pages matches the version of the API data.
  5. The repository contains no files that must never be published (plugin binaries, assets, descriptors, archives).

Exit code 1 on any finding. Usage: python tools/verify_docs.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
api = json.load(open(os.path.join(ROOT, "tools", "generated", "api.json"), encoding="utf-8"))
findings = []

# ---- vocabulary ------------------------------------------------------------------------------------------------
type_names = set()
known = set()      # display names (lower case) of anything a user can see in the editor
code_names = set()  # exact C++ identifiers


def add(*names):
    for n in names:
        if n:
            known.add(n.lower())
            code_names.add(n)


for c in api["classes"]:
    type_names.add(c["name"])
    add(c["name"], c.get("display"))
    for m in c["members"]:
        add(m["name"], m["display"])
        # Blueprint shows booleans without the b prefix and sometimes with "Is"
for e in api["enums"]:
    type_names.add(e["name"])
    add(e["name"])
    for v in e["values"]:
        add(v["name"], re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", v["name"]))
for d in api["delegates"]:
    type_names.add(d["name"])
    add(d["name"])
    ps = d["params"]
    for k in range(0, len(ps) - 1, 2):  # (type, name) pairs: the event parameters shown in Blueprints
        pname = ps[k + 1]
        add(pname, re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", re.sub(r"^b(?=[A-Z])", "", pname)))

# Names that are not part of the plugin API but are legitimate in the pages (engine terms, editor menus, our own
# product names, phrases used as emphasis). Anything else Title Case in bold is reported.
ALLOWED = {
    "server only", "settings", "show plugin content", "build > check map", "edit > plugins", "project settings > plugins > voltweave",
    "tools > new c++ class", "add component", "play", "plugins", "events", "components", "details", "world outliner",
    "replicates", "movable", "static", "run on server", "begin play", "get all nodes", "get node count", "add",
    "start > actor", "end > actor", "component name", "voltweave | runtime state", "voltweave content", "window",
    "category", "gameplay", "voltweave", "voltweave demo", "voltweave debugger", "bind event to on network state changed",
    "network id", "energized", "power state", "granted watts", "output watts", "flow watts", "heat", "stored watt seconds",
    "battery state", "power watts", "indicator", "mode", "selected", "preset", "lamp", "indicator led", "custom",
    "no", "yes", "get networks", "get network info", "solve now", "is simulating", "last solve time ms", "get last solve time ms",
    "on network state changed", "on grid solved", "get voltweave grid", "switch on", "game development with c++",
    "unreal engine", "fab", "windows", "okurstudio", "initial connections", "node enabled", "connect to", "disconnect from",
    "disconnect all", "is connected to", "get connections", "set node enabled", "is energized", "get network id",
    "get indicator state", "get debug label", "on energized changed", "set running", "set max output watts", "set output scale",
    "get available watts", "get output watts", "get load fraction", "on running changed", "on output changed",
    "set switched on", "set requested watts", "get power state", "get granted watts", "get satisfaction", "is powered", "has power",
    "on power state changed", "on power level changed", "set closed", "toggle", "is closed", "on switch changed",
    "open breaker", "close breaker", "replace fuse", "force trip", "get protection state", "is tripped or blown", "get flow watts",
    "get load ratio", "get heat", "on protection state changed", "on tripped", "set charging allowed", "set discharging allowed",
    "set stored energy", "get stored energy", "get charge fraction", "get battery state", "get power watts", "get seconds until empty",
    "on battery state changed", "apply preset", "get look for state", "rebind", "refresh cable", "is live",
    "find grid node", "get grid nodes", "add grid node to actor", "connect actors", "disconnect actors", "is actor powered",
    "consumer state to text", "network state to text", "protection state to text", "battery state to text", "format watts",
    "developer tools", "github issues", "cable actor", "voltweave junction", "voltweave power source", "voltweave power consumer", "voltweave switch", "voltweave breaker / fuse",
    "voltweave battery", "voltweave state feedback", "voltweave cable", "voltweave consumer state",
}
known |= ALLOWED

title_phrase = re.compile(r"^(?:[A-Z][A-Za-z0-9]*|of|to|on|at|or|and|the|for|in)(?: (?:[A-Z][A-Za-z0-9]*|of|to|on|at|or|and|the|for|in|Hz|ms))+$")


def pages():
    for dirpath, _, files in os.walk(DOCS):
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(dirpath, f)


snippet_lines = set()
for f in os.listdir(os.path.join(ROOT, "snippets")):
    for line in open(os.path.join(ROOT, "snippets", f), encoding="utf-8"):
        snippet_lines.add(line.strip())

generated = os.path.join(DOCS, "api", "reference.md")
for page in pages():
    rel = os.path.relpath(page, DOCS).replace("\\", "/")
    text = open(page, encoding="utf-8").read()
    # 1. type names
    if page != generated:
        for m in re.finditer(r"`((?:U|A|F|E)VWV\w+)`", text):
            if m.group(1) not in type_names:
                findings.append(f"{rel}: unknown type `{m.group(1)}`")
        for m in re.finditer(r"`(VWV\w+)`", text):
            if m.group(1) not in ("VWVSolver", "VWVProtectionModel", "VWVValidation") and m.group(1) not in code_names:
                findings.append(f"{rel}: unknown VWV name `{m.group(1)}`")
    # strip code blocks for the phrase checks
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    if page != generated and not rel.startswith("release-notes"):
        for m in re.finditer(r"(?<![*\w])\*\*([^*\n]+)\*\*(?!\*)", prose):
            phrase = m.group(1).strip()
            if title_phrase.match(phrase) and phrase.lower() not in known:
                findings.append(f"{rel}: bold phrase not found in the API: **{phrase}**")
        for m in re.finditer(r"(?<![*\w])\*([A-Z][^*\n]+)\*(?!\*)", prose):
            phrase = m.group(1).strip()
            if title_phrase.match(phrase) and phrase.lower() not in known and len(phrase.split()) <= 5:
                findings.append(f"{rel}: italic phrase not found in the API: *{phrase}*")
    # 3. C++ blocks
    for m in re.finditer(r"```(cpp|csharp)[^\n]*\n(.*?)```", text, flags=re.S):
        body = m.group(2)
        if "--8<--" in body:
            continue
        for line in body.splitlines():
            s = line.strip()
            if s and s not in snippet_lines and not s.startswith("//"):
                findings.append(f"{rel}: C++ line not found in any snippet: {s}")
    # 4. version
    for m in re.finditer(r"0\.2\.0-rc\.\d+", text):
        if rel not in ("release-notes.md",) and m.group(0) != api["version"]:
            findings.append(f"{rel}: version {m.group(0)} differs from API data {api['version']}")

# 5. forbidden files
forbidden_ext = {".uasset", ".umap", ".uplugin", ".dll", ".lib", ".pdb", ".exe", ".zip", ".usf", ".ush"}
for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in (".git", "site", "__pycache__")]
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext in forbidden_ext:
            findings.append(f"forbidden file in the repository: {os.path.relpath(os.path.join(dirpath, f), ROOT)}")
        if f.endswith(".cpp") or f.endswith(".h"):
            if os.path.basename(dirpath) != "snippets":
                findings.append(f"source file outside snippets/: {os.path.relpath(os.path.join(dirpath, f), ROOT)}")

for f in findings:
    print("FINDING:", f)
print(f"{len(findings)} finding(s); API version {api['version']}")
sys.exit(1 if findings else 0)
