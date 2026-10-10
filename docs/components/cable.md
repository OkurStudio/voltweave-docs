# Voltweave Cable

C++ class `AVWVCableActor`. An Actor that wires two Actors together and draws the cable between them. The cable lights up while both ends carry power.

Place it in the level, pick the two Actors, and it creates the electrical connection when the game starts. The ready-made Blueprint is `BP_VWV_Cable`.

## Properties

| Property | Default | Description |
|---|---|---|
| Start, End | | The two ends. Each holds an Actor and an optional *Component Name* (needed only when the Actor has several nodes). |
| Thickness | 4 | Cable diameter in centimeters. |
| Live Color | green | Color while power flows through the cable. |
| Dead Color | near black | Color while the cable is dead. |
| Cable Material | empty | Material of the cable. It should expose the vector parameters `Color` and `Emissive`. A plain engine material is used when empty. |
| Connect On Begin Play | on | If on, the cable creates the electrical connection itself. Turn it off if you wire the nodes in another way. |

## Functions

**Refresh Cable** recomputes the geometry from the two end points. **Is Live** is true while both ends are connected and energized.

## Behaviour

* A cable re-wires itself when one end is recreated at runtime (for example when an Actor's construction script runs again).
* **Build > Check Map** reports cables with a missing end, an end without a Voltweave node, or both ends on the same node.
