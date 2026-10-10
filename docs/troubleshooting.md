# Troubleshooting and debugging

## Tools, from quick to detailed

1. **Setup checks (Build > Check Map).** Voltweave adds its findings to the Map Check of the loaded level, see below. Run it first.
2. **The Details panel while playing.** Select a node component of a running Actor. The category **Voltweave | Runtime State** shows live values: *Power State*, *Granted Watts*, *Output Watts*, *Flow Watts*, *Heat*, *Stored Watt Seconds*, *Network Id*, *Energized*. Editing a normal property (for example *Requested Watts* or *Running*) while playing re-evaluates the grid immediately, so you can tune values live.
3. **Wiring in the editor viewport.** Select an Actor: its nodes draw a wire sphere, a line for each live connection and a dashed white line for each *Initial Connections* entry, with a label that shows the state.
4. **Debug draw while playing.** `Voltweave.Debug.Draw 1` (or *Draw Debug By Default* in the project settings) draws every node, wire and state label. Green is energized, red has no power, orange does not conduct.
5. **The Voltweave Debugger tab.** The editor tab *Voltweave Debugger* lists every network and its nodes while a Play In Editor session runs, with supply, demand, delivered power and battery flow. It is registered in the *Developer Tools* group of the **Window** menu.
6. **Console commands.** `Voltweave.Dump` prints networks and nodes to the log, `Voltweave.Solve` forces an evaluation. See [Console commands](api/console.md).
7. **Log network changes.** Enable *Log Network Events* in the [project settings](components/settings.md) to write every blackout, overload and recovery to the log category `LogVoltweave`.

## Setup checks (Map Check)

**Build > Check Map** (or the Map Check window) includes Voltweave findings for the loaded level:

* nodes that are connected to nothing, and *Initial Connections* entries that point nowhere
* cables with a missing end, an end without a Voltweave node, or both ends on the same node
* State Feedback components without a node, without anything to drive, or with static lights that cannot change
* sources, consumers, batteries and protection devices whose settings make them inert (for example a source with 0 W, a battery with no capacity, a protection device with a rating of 0)
* nodes whose Actor does not replicate (an information message: it is fine for single player)

Click a message to select the component.

## Common problems

| Symptom | Likely cause |
|---|---|
| A consumer never gets power | It is not connected. Check the cable's *Start* and *End* or *Initial Connections*, run Check Map and use the viewport wiring. |
| A consumer is `Unpowered` but the generator runs | A switch or breaker on the path is open or tripped, or a node is disabled. The debugger tab shows which networks exist. |
| Everything is dark on multiplayer clients | The owning Actor does not replicate. |
| Calls do nothing on a client | Changes to the grid are server only; see [Multiplayer](multiplayer.md). The log shows a warning. |
| A breaker never trips | *Rated Watts* is 0, or the flow stays below the rating. Check *Flow Watts* and *Heat* in the runtime state. |
| A breaker trips instantly | The flow reached *Instant Trip Ratio* times the rating, a short circuit by design. |
| A machine flickers on and off | It is all-or-nothing and the supply hovers around its demand. Add capacity or give it a different priority. |
| A lamp stays bright in a brownout | In **Voltweave State Feedback**, *Scale By Satisfaction* is off, or the lights are not *Movable* (static lights cannot change intensity). |
| A battery never charges | There is no surplus (supply equals demand), *Charging Allowed* is off, or the battery is full. |
| Wiring is lost after changing a value in Play In Editor | Some editor edits re-run an Actor's construction script, which recreates its components. Cables and *Initial Connections* re-wire automatically. Wiring made with your own **Connect To** calls is lost with the old component; in C++ [redo it from the native hook](guides/cpp.md#redo-wiring-when-a-node-is-recreated). |
| Invalid numbers (NaN, negative watts) | They are treated as zero instead of breaking the grid. Fix the source of the value. |

## Still stuck?

See [Support](support.md) for what to include in a report.
