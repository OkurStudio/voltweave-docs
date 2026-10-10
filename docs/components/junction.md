# Voltweave Junction

C++ class `UVWVNodeComponent`. The base of every node: a connection point with a position. Use it as a distribution point where several wires meet.

## Properties

| Property | Description |
|---|---|
| Initial Connections | Actors (and optionally a node name) this node is wired to when the game starts. |
| Node Enabled | A disabled node does not conduct, like a cut wire. |
| *Energized* (runtime state) | True while the node belongs to a network that has supply available. |
| *Network Id* (runtime state) | Identifier of the network the node currently belongs to. |

An **Initial Connections** entry holds an Actor and an optional *Component Name*. Leave the name empty when the Actor has exactly one node; if it has several, type the name of the node component. Targets that appear later (spawned after this node) are connected as soon as they begin play.

## Functions

| Function | Notes |
|---|---|
| Connect To, Disconnect From, Disconnect All | Server only. Change the wiring at runtime. |
| Is Connected To, Get Connections | Query the wiring. |
| Set Node Enabled | Server only. |
| Is Energized, Get Network Id | Available on the server and on clients. |
| Get Network Info | Server only: returns the aggregated information of the network. |
| Get Indicator State, Get Debug Label | A simplified state for lights and UI, and a short text for debug displays. |

## Event

**On Energized Changed** `(Node, bEnergized)` fires on the server and on clients when the node gains or loses power from its network.

See the [complete reference](../api/reference.md) for every member.
