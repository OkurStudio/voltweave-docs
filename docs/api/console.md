# Console commands

Open the console with the tilde key while playing (in the editor, in a development or debug build).

| Command | Description |
|---|---|
| `Voltweave.Debug.Draw 1` | Draws nodes, wires and states in the world. `0` is off. `-1` (the default) uses the project setting *Draw Debug By Default*. |
| `Voltweave.Dump` | Prints all networks and nodes of the current world to the log. |
| `Voltweave.Solve` | Forces an immediate evaluation of the grid. |

Colors of the debug drawing: green = energized, red = no power, orange = does not conduct.

To log every blackout, overload and recovery, enable *Log Network Events* in the [project settings](../components/settings.md). The messages go to the log category `LogVoltweave`.
