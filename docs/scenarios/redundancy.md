# Redundancy

**Goal:** two generators and two switches feed a shared bus, and you want to see what survives when something fails. This is bay 6 of the [demo hall](../demo.md).

## The setup

* Generator A and generator B, 600 W each. Each has its own switch. Both switches connect to a junction (the bus).
* On the bus: machine A (400 W, priority 0), machine B (400 W, priority 1), both *Allow Partial Power* off, and a lamp (50 W, priority 0).

## What happens

| Situation | Result |
|---|---|
| Both generators run | 1200 W is available for 850 W of demand: everything is powered. |
| One generator stops | 600 W is available. The lamp (50 W) and machine A (400 W) are served by priority. The remaining 150 W cannot run machine B, which is all-or-nothing, so machine B is switched off completely. |
| Open generator A's switch | Generator A is isolated and delivers nothing. The bus lives on generator B alone: machine A and the lamp keep power, machine B is shed. |

This is the same priority logic as in [Sharing power](../concepts/sharing-power.md), combined with the fact that an open switch is a cut wire and splits networks.
