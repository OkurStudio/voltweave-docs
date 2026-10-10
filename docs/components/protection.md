# Voltweave Breaker and Fuse

C++ class `UVWVProtectionComponent`. One component with two kinds. It measures the power that flows **through** it, heats up on an inverse-time curve when that flow exceeds its rating, and opens when it gets too hot. See [Protection devices](../concepts/protection.md) for the model.

## Properties

| Property | Default | Description |
|---|---|---|
| Kind | Breaker | A breaker trips and can be reset any number of times; a fuse blows and must be replaced. |
| Rated Watts | 1000 | Power that may flow through the device continuously. 0 disables the protection. |
| Time To Trip At Double Load | 3 | Seconds until the device opens when it carries twice its rating. Smaller overloads take longer, bigger ones are faster. |
| Instant Trip Ratio | 4 | Flow as a multiple of the rating at or above which the device opens instantly (short circuit). 0 disables. |
| Cooling Time Seconds | 10 | Seconds the device needs to cool down completely. |
| Auto Reset Delay Seconds | 0 | Breakers only: seconds after a trip until the breaker closes by itself. 0 means never. |
| State | Closed | Initial state. Use Open to start with an opened breaker. |
| *Flow Watts* (runtime state) | | Power flowing through the device. |
| *Heat* (runtime state) | | Accumulated heat from 0 to 1. The device opens at 1. |

## States

| State | Meaning |
|---|---|
| Closed | Conducting. |
| Open | Manually opened (breakers only). |
| Tripped | Opened automatically because of an overload (breakers). |
| Blown | Destroyed because of an overload (fuses). |

## Functions (server only unless noted)

* **Open Breaker**: manually opens a breaker. Fuses cannot be opened.
* **Close Breaker**: closes a breaker, or resets a tripped one. Fails for blown fuses.
* **Replace Fuse**: replaces a blown fuse.
* **Force Trip**: trips a breaker or blows a fuse immediately.
* Everywhere: **Get Protection State**, **Is Tripped Or Blown**, **Get Flow Watts**, **Get Load Ratio** (flow divided by rating), **Get Heat**.

## Events

* **On Protection State Changed** `(Device, NewState, OldState)`
* **On Tripped** `(Device)`: the device opened because of an overload.

Tripping removes the device from the network, which can overload the next device upstream. The grid resolves such cascades within one evaluation; the limit is *Max Cascade Iterations* in the [settings](settings.md).
