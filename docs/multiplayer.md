# Multiplayer

The grid is **server authoritative**.

* The server (or a standalone or listen-server host) simulates the grid and is the only one allowed to change it.
* Every node component replicates the state needed to *show* the grid: the wiring, the enabled flag, the energized flag and the network id, and per type the source's output and running flag, the consumer's power state and granted watts, the switch position, the protection device's state, flow and heat, and the battery's energy, state and power.
* Clients never simulate. The component events (**On Power State Changed**, **On Switch Changed** and so on) also fire on clients when the replicated state arrives, so visuals and sounds work the same everywhere. **Voltweave State Feedback** and the **Voltweave Cable** work on clients out of the box.

## Setup checklist

1. The Actor that owns a node **must replicate** (*Replicates* is on). Components of Actors that do not replicate cannot send their state to clients. All `BP_VWV_*` Actors already replicate. **Build > Check Map** reports a node whose Actor does not replicate.
2. Place or spawn the Actors on the server, as usual.
3. Make changes (**Set Switched On**, **Toggle**, **Close Breaker** and so on) **on the server**. On a client these functions log a warning and do nothing. The warning is rate limited, so a call made every frame does not flood the log.

## Letting players interact

Component functions are not RPCs. A client asks the server to act through an Actor it owns, usually its pawn or its player controller:

1. On the client, find the node the player is looking at or pressing a button for.
2. Call a **Run on Server** event on the pawn and pass the node (or the Actor) as a parameter.
3. On the server, **validate** the request (range, line of sight, permissions) and then call the function, for example **Toggle** on a switch.

In C++ this is a `UFUNCTION(Server, Reliable)` on your character. A complete, compiled example is on the [C++ page](guides/cpp.md#let-a-player-act-on-the-grid). Always validate on the server: never trust a client.

## Nodes added while playing

**Add Grid Node To Actor** (server only) creates a node at runtime. It replicates like any other node when the owning Actor replicates, including to clients that join later. Unreal gives replicated dynamic components their own automatically generated names on each machine, so refer to such a node by reference (the return value of the function), not by its component name.

## What clients cannot see

Aggregated network statistics (**Get Networks**, **Get Network Info**, a HUD overview of all networks) exist only where the grid is simulated. Clients can still read each node's own values (granted watts, flow, charge and so on), its **Network Id** and its **Energized** flag. If your interface needs network totals on a client, add up the values of the nodes that share a *Network Id*.

## Bandwidth

Values are only updated when they change noticeably (for example the output of a source by 0.5 W, the energy of a battery by 0.2 percent of its capacity, the heat of a protection device by 2 percent), so a steady grid sends nothing.

## How it is verified

During development a scripted scenario runs on a dedicated server and a connected client. The server switches, trips, overloads and drains the grid step by step, adds a node at runtime, and after each step the state of every node is logged on both sides; all steps must be identical. A client that joins after the scenario must receive the identical final state. For release candidate 1 the scenario was started 31 times in a row: 30 runs completed with no difference at all, and one run was discarded because the server process froze while the engine was starting, before any Voltweave code ran. It covers one server and one client; it was not tested with many clients or with network latency and packet loss.
