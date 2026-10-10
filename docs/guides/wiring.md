# Wiring

A **wire** connects two nodes. Wires are bidirectional, and a node can have any number of them; use [Junctions](../components/junction.md) as distribution points. Four ways to create wires:

| Way | When to use it | Authority |
|---|---|---|
| **Cable Actor** | Wires you place by hand in a level. It also draws the cable. | Created at BeginPlay |
| **Initial Connections** | Wires you define on a node without a cable mesh. | Created at BeginPlay |
| **Connect To** | Wires you create in Blueprint or C++ while playing. | Server only |
| **Connect Actors** | The same, when you have two Actors instead of two nodes. | Server only |

## Cable Actor

Drop `BP_VWV_Cable` into the level and set **Start > Actor** and **End > Actor** with the Actor picker. If an Actor has several nodes, enter the node's name in *Component Name*. See the [Cable](../components/cable.md) page.

## Initial Connections

Every node has an **Initial Connections** list. Add an entry, pick the other Actor (and, if needed, the name of its node component). The connection is made when the game starts. If the other Actor is spawned later, the connection is made as soon as it begins play. In the editor, a selected Actor draws a dashed line for each entry.

## Connect To and Connect Actors

On the server, call **Connect To** on a node with another node as the target, or **Connect Actors** with two Actors (it wires the first node of each). **Disconnect From**, **Disconnect All** and **Disconnect Actors** remove wires. Connect To, Disconnect From, Connect Actors and Disconnect Actors return whether they succeeded.

Wires can be created and removed at any time. Networks split and merge automatically, so you can build puzzles around cutting and restoring lines.

## Making nodes appear at runtime

**Add Grid Node To Actor** (server) adds a node component to an existing Actor and returns it. The component is replicated when the Actor replicates, including to players who join later.

!!! warning "Recreated components"
    When an Actor's construction script runs again while playing, its components are recreated. Cables and Initial Connections re-wire automatically. Connections that you made with **Connect To** are lost with the old component; in C++ you can redo them from the [native hook](cpp.md#redo-wiring-when-a-node-is-recreated).

## See the wiring

* **In the editor:** a selected Actor draws its nodes, its live connections and the entries of Initial Connections, with a label for the state.
* **While playing:** enter `Voltweave.Debug.Draw 1` in the console to draw every node, wire and state in the world.
* **Check Map:** *Build > Check Map* lists nodes that are connected to nothing and cables with a missing end. See [Troubleshooting](../troubleshooting.md).
