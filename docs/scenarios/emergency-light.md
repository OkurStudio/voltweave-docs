# An emergency light

**Goal:** a lamp that stays on for a while after the generator stops.

## Build it

1. Place a `BP_VWV_Generator`, a `BP_VWV_Battery`, a `BP_VWV_Lamp` and a `BP_VWV_Junction`.
2. Connect all three (generator, battery, lamp) to the junction with three `BP_VWV_Cable` Actors. The junction is the shared bus.
3. Select the battery's *Battery* component. Set **Capacity Watt Seconds** to `6000`. A 100 W lamp drains 6000 watt-seconds in one minute, so this battery lasts one minute. Set **Initial Charge Fraction** to `1`.
4. Press Play. While the generator runs, the battery is full or charging from the surplus.
5. Untick **Running** on the generator's *PowerSource* component. The lamp stays lit, the battery's *Battery State* changes to `Discharging` and *Stored Watt Seconds* falls. After about a minute the battery is `Empty` and the lamp goes dark: a blackout.
6. Tick **Running** again. The lamp is powered by the generator and the battery recharges.

## Things to try

* Add a second, more important consumer with *Priority* `0` next to the lamp (priority 2). When the battery cannot cover everything, the important consumer is served first.
* Bind **On Network State Changed** of the [grid subsystem](../api/grid-subsystem.md) to show a "power lost" message when the network enters `Blackout`, and a "power restored" message when it leaves it.
* Show the remaining time to the player with the battery's **Get Seconds Until Empty**.

The same idea is bay 5 of the [demo hall](../demo.md).
