# Using Voltweave in Blueprints

Everything in Voltweave is available from Blueprints and the Details panel. This page shows the everyday workflow. The [first power network](../getting-started/first-network.md) page is the five-minute version.

## The ready-made Actors

The plugin ships nine Blueprint Actors in `Voltweave Content/Blueprints`. Drop them into a level, duplicate them, or open them to see how they are built. All of them replicate.

| Blueprint | Node component | Defaults |
|---|---|---|
| `BP_VWV_Generator` | PowerSource (Power Source) | 1000 W |
| `BP_VWV_Lamp` | PowerConsumer (Power Consumer), a light and State Feedback (*Lamp*) | 100 W, priority 2 |
| `BP_VWV_Machine` | PowerConsumer | 400 W, priority 1, all-or-nothing |
| `BP_VWV_Switch` | Switch | closed |
| `BP_VWV_Breaker` | Breaker (Breaker / Fuse, kind *Breaker*) | 600 W |
| `BP_VWV_Fuse` | Fuse (Breaker / Fuse, kind *Fuse*) | 300 W |
| `BP_VWV_Battery` | Battery | 30000 Ws, charge up to 300 W, discharge up to 800 W |
| `BP_VWV_Junction` | Junction | |
| `BP_VWV_Cable` | a [Cable](../components/cable.md) Actor | wires two Actors together |

Except for the cable, each of them also has a State Feedback component with an indicator LED or a lamp look.

## Make your own Actor part of the grid

1. Open (or create) the Actor Blueprint.
2. In the **Components** panel choose **Add** and search for "Voltweave". Add the component that fits: **Voltweave Power Consumer** for something that needs power, **Voltweave Power Source** for something that supplies it, and so on. The [components overview](../components/index.md) lists all of them.
3. Select the component and set its properties in the Details panel (for example *Requested Watts*).
4. Optionally add **Voltweave State Feedback** so that lights and materials follow the state, with no Blueprint logic. Remember that lights must be *Movable*.
5. Enable **Replicates** on the Actor if the game is multiplayer. See [Multiplayer](../multiplayer.md).

An Actor can hold several nodes, for example a machine with a consumer and a switch. When a cable or a connection target must point to one specific node, give the node component a clear name and type that name into *Component Name*.

## Wire things together

Choose any of four ways (all described on [Wiring](wiring.md)): a **Cable** Actor in the level, **Initial Connections** on a node, **Connect To** at runtime, or **Connect Actors** at runtime.

## Read the state and react to changes

Do not poll. Every node component has events that you can bind:

1. In the Blueprint, select the component in the Components panel.
2. In the Details panel scroll to **Events** and click the **+** next to the event, for example **On Power State Changed**.
3. The event graph gets a new event node. It also fires on clients, so visuals and sounds work the same everywhere.

| Node | Events |
|---|---|
| Any node | On Energized Changed |
| Power Consumer | On Power State Changed, On Power Level Changed |
| Power Source | On Running Changed, On Output Changed |
| Switch | On Switch Changed |
| Breaker / Fuse | On Protection State Changed, On Tripped |
| Battery | On Battery State Changed |

For a quick yes/no answer use the library node **Is Actor Powered**. To get hold of a node from an Actor use **Find Grid Node** (the first node of a class) or **Get Grid Nodes** (all of them). **Get Voltweave Grid** returns the grid subsystem, whose **On Network State Changed** event announces blackouts and recoveries of whole networks. The [Blueprint function library](../api/blueprint-library.md) page lists everything.

!!! example "A door in Blueprints"
    The [door scenario](../scenarios/door.md) builds a door that opens only while it has power, with one event.

## Change the grid while playing

Switching, wiring and changing numbers must happen **on the server** (in a single player game, that is simply your game). Nodes expose setters for this: **Set Switched On**, **Set Closed**, **Toggle**, **Set Running**, **Set Requested Watts**, **Close Breaker**, **Replace Fuse**, and so on. Called on a client, they log a warning and do nothing. A client that wants to change something asks the server; see [Multiplayer](../multiplayer.md).

To give an Actor a node while playing, call **Add Grid Node To Actor** on the server. It returns the new component, which you can then configure and wire.

## Tune while playing

While the game runs, select a node component in the Details panel: the category **Voltweave | Runtime State** shows the live values. Editing a normal property such as *Requested Watts* or *Running* re-evaluates the network immediately, so you can tune numbers live.
