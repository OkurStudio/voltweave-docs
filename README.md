# voltweave-docs

Official documentation for **Voltweave – Modular Power Grid System** for Unreal Engine 5.8.

The site is published with GitHub Pages: <https://okurstudio.github.io/voltweave-docs/>

This repository contains documentation only. The plugin itself (source code, assets, development tools) is a commercial product and is **not** part of this repository.

© 2026 OKUR BİLGİSAYAR YAZILIM VE PRODÜKSİYON E-TİCARET LİMİTED ŞİRKETİ. All rights reserved.

## Structure

| Path | Contents |
|---|---|
| `docs/` | The pages (Markdown) |
| `docs/api/reference.md` | Generated from the plugin's public headers, do not edit by hand |
| `snippets/` | The C++ examples included by the pages. Each file is compiled against the real plugin headers |
| `tools/` | Scripts that check the documentation (see below) |
| `mkdocs.yml` | Site configuration (MkDocs with the Material theme) |
| `.github/workflows/docs.yml` | Builds and publishes the site on every push to `main` |

## Build the site locally

```bash
pip install -r requirements.txt
python tools/verify_docs.py
mkdocs build --strict
mkdocs serve
```

## How the documentation is kept correct

* `tools/extract_api.py --product <plugin folder>` reads the plugin headers and regenerates `tools/generated/api.json` and `docs/api/reference.md`. Run it whenever the plugin changes. Only declarations and their documentation comments are read.
* `tools/verify_docs.py` checks the pages against that data: type names, Blueprint names, properties, C++ code blocks (they must come from `snippets/`) and the version. It also refuses files that must never be published (plugin binaries, assets, descriptors, archives, source files outside `snippets/`). It runs in the publishing workflow.
* `tools/verify_snippets.ps1 -ProductRepo <development repository>` compiles every file in `snippets/` against the plugin (needs the plugin, Unreal Engine 5.8 and Visual Studio, so it is run by the maintainer, not in the workflow).
* `mkdocs build --strict` fails on broken links and anchors.

## Feedback

Please open an issue for mistakes or unclear pages in the documentation. The product support contact is published with the product listing on Fab.
