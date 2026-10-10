# A fuse box

**Goal:** a fuse that protects a circuit and has to be replaced when it blows.

## Build it

1. Place `BP_VWV_Generator`, `BP_VWV_Fuse`, `BP_VWV_Junction` and two `BP_VWV_Machine` Actors.
2. Connect generator, fuse, junction and the two machines in a line: generator to fuse, fuse to junction, junction to each machine (four cables).
3. Select the fuse's *Fuse* component and set **Rated Watts** to `250`.
4. Select each machine's *PowerConsumer* and set **Requested Watts** to `200`. Together they request 400 W, which is 1.6 times the rating of the fuse.
5. Press Play. The fuse heats up (watch *Heat* in **Voltweave | Runtime State**), its LED turns amber and then red when it blows. Everything behind it loses power.
6. Switch one machine off (untick **Switched On** on its consumer), then call **Replace Fuse** on the fuse component (for example from a Blueprint on a key press, in the server or standalone game). The remaining 200 W is within the rating and the line is back.

The larger the overload the faster the fuse blows: at twice its rating it blows after *Time To Trip At Double Load* seconds (3 by default), and above *Instant Trip Ratio* times the rating it blows at once.

## A breaker instead

Use `BP_VWV_Breaker` and **Close Breaker** instead. A tripped breaker can be reset any number of times, and *Auto Reset Delay Seconds* can close it by itself after a pause. See [Breaker and Fuse](../components/protection.md) and [Protection devices](../concepts/protection.md).
