# Types

All of these are usable in Blueprints. The complete list with every value is in the [generated reference](reference.md#enumerations).

## Enumerations

| Enumeration | Values |
|---|---|
| `EVWVConsumerState` | Off, Unpowered, Underpowered, Powered |
| `EVWVNetworkState` | Idle, Healthy, Deficit, Blackout |
| `EVWVProtectionKind` | Breaker, Fuse |
| `EVWVProtectionState` | Closed, Open, Tripped, Blown |
| `EVWVBatteryState` | Idle, Charging, Discharging, Empty, Full |
| `EVWVAllocationPolicy` | Priority, Proportional |
| `EVWVIndicatorState` | Off, Good, Warning, Fault |
| `EVWVFeedbackPreset` | Custom, Lamp, IndicatorLED |

## Network information

`FVWVNetworkInfo` describes one network. You get it from the [grid subsystem](grid-subsystem.md) (**Get Networks**, **Get Network Info**), from a node (**Get Network Info**) and as the parameter of **On Network State Changed**.

| Field | Meaning |
|---|---|
| Network Id | Stable while the network keeps its lowest node. Not a persistent identifier. |
| State | Overall state of the network. |
| Node Count | Number of nodes in the network. |
| Supply Capacity Watts | Maximum watts all sources of the network can deliver. |
| Demand Watts | Watts requested by all consumers. |
| Delivered Watts | Watts granted to consumers. |
| Battery Discharge Watts | Power currently drawn from batteries. |
| Battery Charge Watts | Power currently going into batteries. |
| Energized | True if anything in the network can currently supply power. |

## Connection target

`FVWVConnectionTarget` is used by **Initial Connections** and by the cable's *Start* and *End*: an *Actor* plus an optional *Component Name*.
