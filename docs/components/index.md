# Components

Every electrical part of Voltweave is a component you add to an Actor. Find them under **Add Component > Voltweave** in the Blueprint editor or the Details panel.

| Component | Role | Page |
|---|---|---|
| Voltweave Junction | A plain connection point. Conducts and does nothing else. It is also the base of all other nodes. | [Junction](junction.md) |
| Voltweave Power Source | Supplies power: generator, solar panel, mains connection. | [Power Source](source.md) |
| Voltweave Power Consumer | Requests power: lamp, machine, door. | [Power Consumer](consumer.md) |
| Voltweave Switch | Conducts only while closed. | [Switch](switch.md) |
| Voltweave Breaker / Fuse | Opens when too much power flows through it. | [Breaker and Fuse](protection.md) |
| Voltweave Battery | Stores surplus power and releases it when supply runs short. | [Battery](battery.md) |
| Voltweave State Feedback | Makes lights and materials follow the state of a node, without Blueprint logic. | [State Feedback](feedback.md) |
| Voltweave Cable | An Actor that wires two Actors together and draws the cable. | [Cable](cable.md) |

All node components (everything except State Feedback and the Cable) are *scene components* with a position, and they share the properties, functions and events of the Junction. Project wide options are on the [Settings](settings.md) page.

!!! tip "Names in the editor"
    Blueprint names on these pages are the names Unreal shows in the editor, for example **Set Running**. The C++ name of the same function is `SetRunning`. The [complete reference](../api/reference.md) lists both for every member and is generated from the plugin headers.

## Runtime state in the Details panel

While the game runs, select a node component to see its live values in the category **Voltweave | Runtime State** (for example *Granted Watts*, *Heat*, *Stored Watt Seconds*). These properties are read only; change the configuration properties instead and the network re-evaluates immediately.
