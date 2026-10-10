# Voltweave Battery

C++ class `UVWVBatteryComponent`. Stores energy. It charges from surplus power and discharges to cover a shortfall, and never does both at once.

## Properties

| Property | Default | Description |
|---|---|---|
| Capacity Watt Seconds | 60000 | Total energy. A 100 W load drains 6000 watt-seconds per minute. |
| Initial Charge Fraction | 1 | Charge level when the game starts, from 0 to 1. |
| Max Charge Watts | 500 | Upper limit of the charging power. |
| Max Discharge Watts | 1000 | Upper limit of the discharging power. |
| Charge Efficiency | 0.9 | Fraction of the drawn charging power that is stored. |
| Charging Allowed, Discharging Allowed | on | Disable one direction. |
| *Stored Watt Seconds* (runtime state) | | Energy in the battery. |
| *Battery State* (runtime state) | | `Idle`, `Charging`, `Discharging`, `Empty` or `Full`. |
| *Power Watts* (runtime state) | | Positive while discharging into the network, negative while charging. |

## Functions (server only unless noted)

**Set Charging Allowed**, **Set Discharging Allowed**, **Set Stored Energy**. Everywhere: **Get Stored Energy**, **Get Charge Fraction** (0 to 1), **Get Battery State**, **Get Power Watts**, **Get Seconds Until Empty** (-1 when not discharging).

## Event

**On Battery State Changed** `(Battery, NewState, OldState)` fires on the server and on clients.

A network that has a battery keeps being evaluated over time while the battery charges or discharges (see [Time and updates](../concepts/time-and-authority.md)).
