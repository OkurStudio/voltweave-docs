# Voltweave State Feedback

C++ class `UVWVFeedbackComponent`. Makes an Actor *look* like its node without any Blueprint logic: lights switch on and off, dim in a brownout, and materials glow. It works on the server and on clients.

## Quick setup

1. Add **Voltweave State Feedback** to an Actor that has a node (for example a Power Consumer).
2. Leave *Targets* empty to drive every light component of the Actor, or add the lights and meshes you want.
3. Pick the preset **Lamp**.
4. Make sure the lights are **Movable**: a Static light cannot change intensity at runtime (Map Check warns about it).

## Properties

| Property | Default | Description |
|---|---|---|
| Node | empty | The node to watch. Empty means the first node on the Actor. |
| Targets | empty | Lights and meshes to drive. Empty means every light of the Actor. Meshes get dynamic material instances. |
| Preset | Indicator LED | **Lamp**: lights up while powered, dims and flickers in a brownout, dark otherwise. **Indicator LED**: green, amber, red. **Custom**: you set every look. Editing a look switches the preset to Custom. |
| Off / Good / Warning / Fault Look | | Color, light intensity multiplier and emissive multiplier for each state. |
| Flicker On Warning | off | Flicker while the node is in the warning state (a brownout for consumers). |
| Scale By Satisfaction | off | For consumers: additionally scale light intensity and emissive by the received fraction of the demand. |
| Color Parameter Name | `Color` | Vector parameter of your material that receives the color. |
| Emissive Parameter Name | `Emissive` | Vector parameter that receives color times emissive strength. |
| Emissive Strength | 4 | Global multiplier of the emissive strength. |
| Blend Speed | 10 | How quickly looks blend from one state to the next. |

`M_VWV_Basic` (included with the plugin) has both the `Color` and the `Emissive` parameter, so meshes using an instance of it work out of the box.

## Indicator states

Every node reports one of four indicator states through **Get Indicator State**, and the feedback component shows the look you assigned to that state:

| Node | Off | Good | Warning | Fault |
|---|---|---|---|---|
| Junction | not energized | energized | | node disabled |
| Power Source | no capacity (stopped, scale 0, disabled) | running below 98 % of its capacity | delivering 98 % or more of its capacity | |
| Power Consumer | switched off | Powered | Underpowered (brownout) | Unpowered |
| Switch | closed, not energized | closed and energized | open | |
| Breaker / Fuse | closed, not energized | closed, energized, heat up to 50 % | manually open, or heat above 50 % | Tripped or Blown |
| Battery | | idle, charging or full | discharging | empty |

## Functions

**Apply Preset**, **Get Look For State**, **Rebind** (re-reads the node and the targets; call it after adding components at runtime). A feedback component also waits for a node that is added later and keeps the authored light intensity when it is rebound.
