# Project settings

**Project Settings > Plugins > Voltweave** (C++ class `UVWVSettings`). The settings apply to the whole project.

| Setting | Default | Description |
|---|---|---|
| Solver Frequency Hz | 20 | How many times per second the network is re-evaluated while something time dependent is happening (a battery charging or discharging, a protection device overheating). Changes to the wiring or to a state are always evaluated immediately. |
| Allocation Policy | Priority | How available power is shared when there is not enough for everyone: **Priority** serves the lowest priority number first, **Proportional** gives every consumer the same fraction of its demand. See [Sharing power](../concepts/sharing-power.md). |
| Max Cascade Iterations | 8 | Upper bound of re-evaluations caused by protection devices tripping one after another within one evaluation. |
| Draw Debug By Default | off | Draws nodes, wires and state in the world while playing. Also controlled by the console variable `Voltweave.Debug.Draw`. |
| Log Network Events | off | Writes network changes (blackouts, trips, recoveries) to the log category `LogVoltweave`. |
