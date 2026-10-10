# Voltweave Power Consumer

C++ class `UVWVConsumerComponent`. Requests power: a lamp, a machine, a door.

## Properties

| Property | Default | Description |
|---|---|---|
| Requested Watts | 100 | Demand while switched on. |
| Switched On | on | Whether the consumer asks for power at all. |
| Priority | 0 | The consumer with the lowest number is served first when power is short. |
| Allow Partial Power | on | Off makes the consumer all-or-nothing: it is switched off completely if its full demand cannot be met. Good for machines. |
| Min Operating Fraction | 0 | Below this fraction of its demand the consumer receives nothing, so the power goes to others instead of being wasted on something that cannot run. |
| *Power State* (runtime state) | | `Off`, `Unpowered`, `Underpowered` or `Powered`. |
| *Granted Watts* (runtime state) | | Power received right now. |

## Power states

| State | Meaning |
|---|---|
| Off | The consumer does not request power (switched off or zero demand). |
| Unpowered | It requests power and receives none. |
| Underpowered | It receives only part of the demand (a brownout). |
| Powered | It receives everything it requested. |

## Functions

* Server only: **Set Switched On**, **Set Requested Watts**.
* Everywhere: **Get Power State**, **Get Granted Watts**, **Get Satisfaction** (received divided by requested, 0 to 1), **Is Powered** (full power), **Has Power** (full or partial power).

## Events

* **On Power State Changed** `(Consumer, NewState, OldState)`
* **On Power Level Changed** `(Consumer, Satisfaction)`

Both fire on the server and on clients, after the network has finished evaluating, so it is safe to change the grid from inside a handler.

For how power is shared between several consumers see [Sharing power](../concepts/sharing-power.md).
