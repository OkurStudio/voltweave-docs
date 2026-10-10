# Voltweave Power Source

C++ class `UVWVSourceComponent`. Produces power: a generator, a solar panel, a mains connection.

## Properties

| Property | Default | Description |
|---|---|---|
| Max Output Watts | 1000 | Maximum power the source can deliver. |
| Running | on | Off means the source offers no capacity. |
| Output Scale | 1 | A multiplier between 0 and 1, for example a throttle or the angle of the sun. |
| *Output Watts* (runtime state) | | Power the source delivers right now. |

The capacity a source offers is `Max Output Watts x Output Scale` while it is running and enabled. When several sources share a network they share the load in proportion to their capacity.

## Functions (server only unless noted)

**Set Running**, **Set Max Output Watts**, **Set Output Scale**. Readable everywhere: **Get Available Watts** (what the source offers right now), **Get Output Watts**, **Get Load Fraction** (output relative to the available capacity, 0 to 1).

## Events

* **On Running Changed** `(Source, bRunning)`
* **On Output Changed** `(Source, OutputWatts)`

Both fire on the server and on clients.

!!! example "Day and night for a solar panel"
    Call **Set Output Scale** from your time of day logic: 0 at night, 1 at noon. See the [solar panel scenario](../scenarios/solar-panel.md).
