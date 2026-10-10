# Installation

## Requirements

| | |
|---|---|
| Unreal Engine | **5.8** |
| Platform | **Windows 64-bit**. Other platforms and engine versions are not supported in this release. |
| Third-party dependencies | None. The plugin does not change your project's input settings. |
| Optional demo plugin | Uses the Enhanced Input plugin, which is enabled automatically. |

!!! info "Do I need Visual Studio?"
    **Using Voltweave in the editor** (Blueprints, Play In Editor): if your copy of the plugin contains compiled Editor binaries, you do not need a compiler. If Unreal asks to rebuild the plugin modules when you open the project, which is what happens with the source package, you need Visual Studio 2022 with the *Game development with C++* workload for that one-time build.

    **Packaging a game:** in our tests a Blueprint-only project could not load Voltweave in the packaged game (the error was "module could not be found"), while the same project converted to a C++ project could. Plan on a C++ project (add any C++ class once with *Tools > New C++ Class*) and a C++ toolchain for packaging. We are still confirming whether a copy installed through the Fab launcher behaves differently, and this page will be updated when we know.

## Install the plugin

1. **From the Fab library:** install the plugin to your engine or add it to your project from the Fab library in the Epic Games Launcher.
   **From a zip file** (source package): copy the `Voltweave` folder into your project's `Plugins` folder. Create the folder if it does not exist.
2. Open the project. With a source package Unreal asks to rebuild the plugin modules; accept. If your copy already contains compiled Editor binaries, no rebuild is requested.
3. Check that the plugin is enabled under **Edit > Plugins**, category *Gameplay*, entry *Voltweave*. Restart the editor if Unreal asks you to.
4. In the Content Browser open **Settings** and enable **Show Plugin Content**. You now see the `Voltweave Content` folder with the ready-made Blueprints (`Blueprints`) and materials (`Materials`).

## Check that it works

* In any Actor Blueprint, **Add Component** and search for "Voltweave": the node components appear.
* Open **Project Settings > Plugins > Voltweave**: the [settings](../components/settings.md) are there.

Continue with [your first power network](first-network.md).

## The optional demo plugin

The playable demo hall is a separate plugin, **Voltweave Demo**. Install it next to Voltweave (from the Fab library, or by copying the `VoltweaveDemo` folder into your `Plugins` folder). A source copy is compiled when you open the project, which needs the toolchain mentioned above. Then enable *Show Plugin Content* and open `Voltweave Demo Content/Maps/L_VWV_Demo`. See [The demo hall](../demo.md).

Voltweave never depends on the demo, so you can remove the demo plugin at any time.

## Updating and removing

Close the editor, replace the `Voltweave` folder (or update from the Fab library) and reopen the project. To remove Voltweave, first remove all Voltweave components and Actors from your levels and Blueprints, then delete the folder.
