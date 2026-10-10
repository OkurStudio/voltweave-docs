# The demo hall

**Voltweave Demo** is a separate, optional plugin with a playable level. It is not needed to use Voltweave and can be removed at any time. Voltweave itself never depends on it.

## Open it

1. Install the demo plugin next to Voltweave (see [Installation](getting-started/installation.md#the-optional-demo-plugin)).
2. Enable **Show Plugin Content** in the Content Browser.
3. Open `Voltweave Demo Content/Maps/L_VWV_Demo` and press **Play**.

## Controls

| Key | Action |
|---|---|
| `W` `A` `S` `D` | Move |
| Mouse | Look |
| `Space` | Jump |
| `E` or left mouse button | Interact with the object you are looking at (within about 3.5 m) |
| `R` | Restart the level |
| `Esc` | Leave a packaged demo (in the editor, `Esc` ends Play In Editor) |

Look at an object to read its live state. The HUD in the top left lists the networks of the level (shown on the server and in standalone games only).

The level uses only Voltweave's own Blueprints, engine basic shapes and one material. It has no sound, and your project's input settings are not changed.

## The six bays

| Bay | What it shows | Try this |
|---|---|---|
| 1 Power basics | Source, junction, consumers, cables | Switch a lamp off: the generator output drops. Stop the generator: everything goes dark. |
| 2 Switches | Switches cut everything behind them | Open the machine switch; open the main switch. |
| 3 Overload protection | A breaker and a fuse | Switch on the third machine: the breaker heats up (LED amber) and trips (red). Reset it after turning something off. On the right, switch on both machines behind the fuse: it blows; replace it. |
| 4 Priorities and brownout | 600 W requested, 500 W available | The critical lamp and the machine are served; the two low priority lamps dim and flicker. Start the standby generator to fix it. See [Priorities and brownouts](scenarios/priorities-and-brownouts.md). |
| 5 Battery and blackout | A battery takes over | Stop the generator: the battery powers the lamps, drains and finally a blackout occurs. Start it again to recharge. |
| 6 Redundancy | Two generators, two paths | Stop one generator: the important machine keeps running, the other is shed. Open a switch to isolate a generator. See [Redundancy](scenarios/redundancy.md). |

Each bay has a board on the wall that explains what to try.

## Using the demo pieces in your own project

* Copy the `BP_VWV_*` Actors from `Voltweave Content/Blueprints` into your own levels, or use them as templates.
* The **Voltweave State Feedback** component of each Actor shows how to make visuals follow the grid without scripting.
* To play the demo in multiplayer, start a listen server or a dedicated server on the demo map; clients interact through a server call on their pawn (see [Multiplayer](multiplayer.md)).
