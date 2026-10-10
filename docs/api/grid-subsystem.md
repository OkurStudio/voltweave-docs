# Grid subsystem

C++ class `UVWVGridSubsystem`, a world subsystem: there is one per world. In Blueprints get it with **Get Voltweave Grid**, in C++ with `UVWVGridSubsystem::Get(WorldContextObject)`.

## Functions

| Function | Description |
|---|---|
| **Get Networks**, **Get Network Info** | Aggregated state per network (see [Types](types.md#network-information)). Available where the grid is simulated. |
| **Get All Nodes**, **Get Node Count** | Inspection of the nodes registered in the world. |
| **Get Last Solve Time Ms** | Duration of the last evaluation in milliseconds. |
| **Solve Now** | Forces an immediate evaluation. Server only; rarely needed because every change evaluates the grid automatically. |
| **Is Simulating** | True on the server and in standalone games. Network totals exist only there. |

## Events

* **On Network State Changed** `(Network, PreviousState)`: a network went from one state to another, for example from Healthy to Blackout, or from Blackout to Healthy when two networks merged.
* **On Grid Solved**: after every evaluation.

Events are delivered after the evaluation has finished, so it is safe to change the grid from a handler.

## C++ only: native hook for new nodes

`OnNodeRegisteredNative()` is a native multicast delegate that fires whenever a node registers with the grid, including nodes that were just recreated. See the [C++ guide](../guides/cpp.md#redo-wiring-when-a-node-is-recreated) for an example.

The subsystem works only on the server, as it is the only place the grid is simulated: see [Multiplayer](../multiplayer.md).
