# A solar panel with day and night

**Goal:** power that follows the time of day.

## Build it

1. In your panel Blueprint add **Voltweave Power Source** and set *Max Output Watts* to the peak output of the panel.
2. In your day and night logic (for example the level Blueprint, or the Actor that moves the sun) call **Set Output Scale** on the panel's source: `0` at night, `1` at full sun, anything in between at dawn and dusk. It is a server call, so run it on the server.
3. Update the scale at a modest rate, for example once a second or when the sun angle has changed noticeably, instead of on every frame.
4. Place a `BP_VWV_Battery` on the same network to carry the load through the night, as in the [emergency light](emergency-light.md) scenario.

**Get Available Watts** on the source shows what the panel offers right now (`Max Output Watts x Output Scale`), and its *Indicator* shows a warning while the panel delivers almost all it can.
