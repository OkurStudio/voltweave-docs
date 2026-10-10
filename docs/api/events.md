# Events

Bind to events instead of polling. Component events fire on the server and on clients (when the replicated state arrives). Events are delivered after an evaluation of the grid has finished, so changing the grid from a handler is safe.

| Where | Event | Parameters |
|---|---|---|
| Any node | **On Energized Changed** | Node, Energized |
| Power Consumer | **On Power State Changed** | Consumer, New State, Old State |
| Power Consumer | **On Power Level Changed** | Consumer, Satisfaction (0 to 1) |
| Power Source | **On Running Changed** | Source, Running |
| Power Source | **On Output Changed** | Source, Output Watts |
| Switch | **On Switch Changed** | Switch, Closed |
| Breaker / Fuse | **On Protection State Changed** | Device, New State, Old State |
| Breaker / Fuse | **On Tripped** | Device |
| Battery | **On Battery State Changed** | Battery, New State, Old State |
| Grid subsystem | **On Network State Changed** | Network (information structure), Previous State |
| Grid subsystem | **On Grid Solved** | none |

**On Power Level Changed** fires when the received fraction of the demand changes by about one percent or more. **On Output Changed** fires when the output of a source changes by about half a watt or more. They do not fire for tiny changes.

## Binding in Blueprints

Select the component, scroll to **Events** in the Details panel and click the **+** next to the event. For the grid subsystem events use **Get Voltweave Grid** and the *Bind Event to On Network State Changed* node.

## Binding in C++

The event handler must be a `UFUNCTION()` with the parameters of the event:

```cpp
Power->OnPowerStateChanged.AddDynamic(this, &AMyPowerDoor::HandlePowerStateChanged);

UFUNCTION()
void HandlePowerStateChanged(UVWVConsumerComponent* Consumer, EVWVConsumerState NewState, EVWVConsumerState OldState);
```

Complete, compiled examples: [C++ guide](../guides/cpp.md).
