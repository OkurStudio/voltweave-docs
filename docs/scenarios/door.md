# A door that needs power

**Goal:** a door that stays shut while its generator is off and opens when power arrives.

## Build it

1. Create an Actor Blueprint `BP_PowerDoor` with a door mesh.
2. Add the component **Voltweave Power Consumer** and set *Requested Watts* to `50`.
3. Select the consumer in the Components panel. In the Details panel, under **Events**, click the **+** next to **On Power State Changed**. An event node appears in the Event Graph. It has the pins *Consumer*, *New State* and *Old State*.
4. Drag from *New State* and compare it with `Powered` (an equality node on the enum, or a Switch on the enum). If it is `Powered`, play the opening animation or rotate the door; otherwise close it. The state `Underpowered` (a brownout) is a good place for a stuttering door.
5. In the level place `BP_PowerDoor`, `BP_VWV_Generator` and a `BP_VWV_Cable`. Set the cable's *Start > Actor* to the generator and *End > Actor* to the door.
6. Press Play. The door follows the generator: untick **Running** on the generator's *PowerSource* component in the Details panel while playing and the door closes.

!!! tip "At the start of the game"
    The event fires when the state *changes*. To set the correct pose at the beginning, also call **Is Powered** on the consumer in *Begin Play* and apply the result.

!!! tip "Door first, lamps later"
    If power is short, you may want the door served before the lamps. Give the door's consumer *Priority* `0` (the lamp Blueprint uses 2). See [Sharing power](../concepts/sharing-power.md).

## In C++

The same door as an Actor class, with the handler bound in code, is on the [C++ page](../guides/cpp.md#a-node-on-your-own-actor).
