# Priorities and brownouts

**Goal:** decide who keeps power when there is not enough. This is bay 4 of the [demo hall](../demo.md).

## The setup

* One junction as the bus. Two generators feed it: one runs (500 W), a standby generator is switched off (also 500 W).
* Four consumers hang on the bus:

| Consumer | Request | Priority | Settings |
|---|---|---|---|
| Critical lamp | 100 W | 0 | |
| Machine | 300 W | 1 | *Allow Partial Power* off (all-or-nothing) |
| Lamp | 100 W | 2 | |
| Lamp | 100 W | 2 | |

Demand is 600 W; the running generator offers 500 W.

## What happens

The grid serves priority 0 first, then priority 1, then 2:

1. The critical lamp receives its 100 W.
2. The machine receives its 300 W (the 400 W so far is covered).
3. The 100 W that is left is shared by the two lamps of priority 2, so each receives 50 W. They are `Underpowered`: with the State Feedback preset *Lamp* they dim and flicker.

Start the standby generator (**Running** on its *PowerSource*) and everything is `Powered`.

## Try variations

* Change the machine to *Allow Partial Power* on: it would then run with less than its 300 W, as long as it reaches its *Min Operating Fraction*.
* Switch the [project's allocation policy](../components/settings.md) to **Proportional** and compare: priorities no longer decide who dims, every consumer receives the same fraction of its demand.
* Lower the priority number of a lamp to 0 and watch it keep full power while the other lamps dim.

Background: [Sharing power](../concepts/sharing-power.md).
