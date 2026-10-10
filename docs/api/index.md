# API reference

Everything is available from Blueprints and C++. The pages in this section describe the entry points; the generated [complete reference](reference.md) lists every class, property, function, event and enumeration of the plugin with its Blueprint name, C++ signature and description.

| Page | Contents |
|---|---|
| [Blueprint function library](blueprint-library.md) | Helper functions: find nodes, wire Actors, ask if something is powered, format text. |
| [Grid subsystem](grid-subsystem.md) | The world subsystem that knows every network. |
| [Events](events.md) | Every event you can bind, and when it fires. |
| [Types](types.md) | Enumerations and the network information structure. |
| [Console commands](console.md) | Debug commands and variables. |
| [Complete reference](reference.md) | Generated from the plugin headers. |

Component pages: [Junction](../components/junction.md), [Power Source](../components/source.md), [Power Consumer](../components/consumer.md), [Switch](../components/switch.md), [Breaker and Fuse](../components/protection.md), [Battery](../components/battery.md), [State Feedback](../components/feedback.md), [Cable](../components/cable.md).

!!! info "Server only"
    Functions that change the grid have an effect only on the server (or in a standalone game). On a client they log a rate-limited warning and do nothing.
