# Voltweave Switch

C++ class `UVWVSwitchComponent`. Conducts only while closed. An open switch behaves like a cut wire: everything behind it is separated from the supply, and the network splits in two.

## Property

| Property | Default | Description |
|---|---|---|
| Closed | on | Whether the switch conducts. |

## Functions

* Server only: **Set Closed**, **Toggle** (returns the new closed state).
* Everywhere: **Is Closed**.

## Event

**On Switch Changed** `(Switch, bClosed)` fires on the server and on clients.

!!! note
    A switch has no power rating. To protect a line against overload use a [Breaker or Fuse](protection.md).
