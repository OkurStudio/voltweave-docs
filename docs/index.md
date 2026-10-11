---
title: Voltweave documentation
hide:
  - navigation
  - toc
---

# Voltweave

**A modular, replicated power grid for Unreal Engine 5.8.** Turn any Actor into a power source, consumer, switch, fuse, breaker or battery by adding a component. No C++ is required.

[Get started :material-arrow-right:](getting-started/installation.md){ .md-button .md-button--primary }
[Build your first network](getting-started/first-network.md){ .md-button }

!!! info "Version"
    This documentation describes Voltweave **0.2.0-rc.3** (release candidate) for Unreal Engine 5.8 on Windows 64-bit.

## What you get

| | |
|---|---|
| **Power sources** | Generators, solar panels, mains: capacity, on/off and a throttle. |
| **Consumers** | Lights, machines, doors: demand, priority, brownouts, an all-or-nothing option. |
| **Switches** | Open or close any connection at runtime. |
| **Fuses and breakers** | A thermal trip curve, instant short-circuit trip, reset or replace, optional auto-reset. |
| **Batteries** | Charge from surplus, discharge when supply is short, efficiency and limits. |
| **Dynamic networks** | Wires can be added and removed while playing; networks split and merge automatically. |
| **Outages** | Blackout and overload events per network, priority based load shedding. |
| **Multiplayer** | Server authoritative; the state needed for visuals and interface is replicated. |
| **No scripting for visuals** | The State Feedback component makes lights and materials follow a node. |
| **Debugging** | Map Check, live runtime state, in-viewport wiring, a debugger tab, console commands. |

## Find what you need

<div class="grid cards" markdown>

-   :material-download: **[Installation](getting-started/installation.md)**

    Requirements, installing the plugin and what you need to package a game.

-   :material-flash: **[First power network](getting-started/first-network.md)**

    A generator, a lamp and a cable in five minutes. Blueprint only.

-   :material-graph: **[How the grid works](concepts/how-it-works.md)**

    Nodes, networks, sharing power, protection devices, time and authority.

-   :material-puzzle: **[Components](components/index.md)**

    Every component with its properties, functions and events.

-   :material-script-text: **[Blueprint guide](guides/blueprint.md)** and **[C++ guide](guides/cpp.md)**

    Everyday workflow, wiring, events, and compiled C++ examples.

-   :material-lightbulb-on: **[Example scenarios](scenarios/index.md)**

    A door that needs power, an emergency light, a solar panel, a fuse box and more.

-   :material-lan: **[Multiplayer](multiplayer.md)**

    Authority, replication and letting players act on the grid.

-   :material-book-open-variant: **[API reference](api/index.md)**

    The function library, the grid subsystem, events, types and the complete generated reference.

-   :material-wrench: **[Troubleshooting](troubleshooting.md)**

    Map Check, debug tools and common problems.

</div>

## Requirements at a glance

* Unreal Engine **5.8**, **Windows 64-bit**.
* No third-party dependencies, and your project's input settings are never changed.
* A C++ toolchain is needed when Unreal has to compile the plugin, and for packaging a game. Details on the [Installation](getting-started/installation.md) page.

!!! note "Created with AI"
    Voltweave was developed with the help of generative AI tools (code, documentation and the content generation scripts) and is covered by automated tests and verification steps. Please report anything that does not behave as documented.
