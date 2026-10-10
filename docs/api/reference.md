# Complete reference

Generated from the public headers of Voltweave 0.2.0-rc.2. Every name on this page exists in that version.

Blueprint names are the display names Unreal shows in the editor. *Server only* means the call has an effect only where the grid is simulated (the server or a standalone game); on a client it logs a warning and does nothing.

## Enumerations

### `EVWVAllocationPolicy`

How available power is shared between consumers.

| Value | Meaning |
|---|---|
| `Priority` | Consumers with a lower Priority value are served first. |
| `Proportional` | Every consumer receives the same fraction of its demand. |

### `EVWVBatteryState`

State of a battery.

| Value | Meaning |
|---|---|
| `Idle` | Neither charging nor discharging. |
| `Charging` | Storing surplus power from the network. |
| `Discharging` | Supplying power to the network. |
| `Empty` | No stored energy is left. |
| `Full` | Fully charged. |

### `EVWVConsumerState`

How a consumer is currently supplied.

| Value | Meaning |
|---|---|
| `Off` | The consumer does not request power (switched off or zero demand). |
| `Unpowered` | The consumer requests power but receives none. |
| `Underpowered` | The consumer receives only part of the requested power (brownout). |
| `Powered` | The consumer receives all requested power. |

### `EVWVFeedbackPreset`

Ready-made look configurations.

| Value | Meaning |
|---|---|
| `Custom` | You configure every state yourself. |
| `Lamp` | A lamp: lights up while powered, dims and flickers during a brownout, dark otherwise. |
| `IndicatorLED` | A status LED: green = good, amber = warning, red = fault, dark = off. |

### `EVWVIndicatorState`

Simplified health of any node, meant for indicator lights and UI.

| Value | Meaning |
|---|---|
| `Off` | Inactive, switched off or without a function right now. |
| `Good` | Working normally. |
| `Warning` | Working but stressed, partially supplied or manually opened. |
| `Fault` | Failed: no power, tripped, blown or empty. |

### `EVWVNetworkState`

Health of an isolated electrical network.

| Value | Meaning |
|---|---|
| `Idle` | No demand and no supply. |
| `Healthy` | All demand is satisfied. |
| `Deficit` | Supply exists but demand exceeds it. |
| `Blackout` | Consumers request power but nothing can supply it. |

### `EVWVProtectionKind`

Kind of protection device.

| Value | Meaning |
|---|---|
| `Breaker` | Trips on overload and can be reset any number of times. |
| `Fuse` | Blows on overload and must be replaced. |

### `EVWVProtectionState`

State of a protection device.

| Value | Meaning |
|---|---|
| `Closed` | Conducting. |
| `Open` | Manually opened (breaker only). |
| `Tripped` | Opened automatically because of an overload (breaker). |
| `Blown` | Destroyed because of an overload (fuse). |

## Voltweave Cable (`AVWVCableActor`)

Derives from `AActor`. Header: `VWVCableActor.h`.

Wires two nodes together and draws a cable between them. The cable lights up while both ends carry power. Place it in the level, pick the two Actors and it connects them when the game starts.

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Start (`Start`) | `FVWVConnectionTarget` |  | First end of the cable. *(editable)* |
| End (`End`) | `FVWVConnectionTarget` |  | Second end of the cable. *(editable)* |
| Thickness (`Thickness`) | `float` | `4.f` | Cable diameter in centimeters. *(editable)* |
| Live Color (`LiveColor`) | `FLinearColor` | `FLinearColor(0.1f, 1.f, 0.25f)` | Color while power flows through the cable. *(editable)* |
| Dead Color (`DeadColor`) | `FLinearColor` | `FLinearColor(0.03f, 0.03f, 0.03f)` | Color while the cable is dead. *(editable)* |
| Cable Material (`CableMaterial`) | `TObjectPtr<UMaterialInterface>` |  | Material of the cable. It should expose the vector parameters "Color" and "Emissive". Uses a plain engine material when empty. *(editable)* |
| Connect On Begin Play (`bConnectOnBeginPlay`) | `bool` | `true` | If true the cable creates the electrical connection itself when the game starts. Disable it if you wire the nodes in another way. *(editable)* |
| Cable Mesh (`CableMesh`) | `TObjectPtr<UStaticMeshComponent>` |  | The visible cable, stretched between the two ends. *(runtime state)* |

**Functions**

| Blueprint name | C++ signature | Description |
|---|---|---|
| Refresh Cable | `void RefreshCable()` | Recomputes the cable geometry from the two end points. |
| Is Live *(pure)* | `bool IsLive() const` | True while both ends are connected and energized. |

## FVWVConnectionTarget (`FVWVConnectionTarget`)

Designer-time reference to another node: an Actor and, if it has several nodes, the name of one of its node components.

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Actor (`Actor`) | `TSoftObjectPtr<AActor>` |  | Actor that owns the node to connect to. *(editable)* |
| Component Name (`ComponentName`) | `FName` |  | Name of the node component on that Actor. Leave empty to use its first node. *(editable)* |

## FVWVFeedbackLook (`FVWVFeedbackLook`)

How lights and materials look in one indicator state.

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Color (`Color`) | `FLinearColor` | `FLinearColor::White` | Color of lights and of the material color/emissive parameters. *(editable)* |
| Light Intensity (`LightIntensity`) | `float` | `1.f` | Multiplier of the design-time intensity of affected lights. 0 turns them off. *(editable)* |
| Emissive (`Emissive`) | `float` | `1.f` | Multiplier of the emissive material parameter. 0 means not glowing. *(editable)* |

## FVWVNetworkInfo (`FVWVNetworkInfo`)

Aggregated information about one isolated network (a set of connected, conducting nodes).

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Network Id (`NetworkId`) | `int32` | `INDEX_NONE` | Stable while the network keeps its lowest node. Not a persistent identifier. *(read only)* |
| State (`State`) | `EVWVNetworkState` | `EVWVNetworkState::Idle` | Overall state of the network. *(read only)* |
| Node Count (`NodeCount`) | `int32` | `0` | Number of nodes in the network. *(read only)* |
| Supply Capacity Watts (`SupplyCapacityWatts`) | `float` | `0.f` | Maximum watts all sources of the network can deliver. *(read only)* |
| Demand Watts (`DemandWatts`) | `float` | `0.f` | Watts requested by all consumers. *(read only)* |
| Delivered Watts (`DeliveredWatts`) | `float` | `0.f` | Watts granted to consumers. *(read only)* |
| Battery Discharge Watts (`BatteryDischargeWatts`) | `float` | `0.f` | Power currently drawn from batteries. *(read only)* |
| Battery Charge Watts (`BatteryChargeWatts`) | `float` | `0.f` | Power currently going into batteries. *(read only)* |
| Energized (`bEnergized`) | `bool` | `false` | True if anything in the network can currently supply power. *(read only)* |

## Voltweave Battery (`UVWVBatteryComponent`)

Derives from `UVWVNodeComponent`. Header: `VWVBatteryComponent.h`.

Stores energy. Charges from surplus power and discharges when the sources of its network cannot cover the demand. Energy is measured in watt-seconds (joules): a 100 W load drains 6000 Ws in one minute.

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Capacity Watt Seconds (`CapacityWattSeconds`) | `float` | `60000.f` | Total capacity in watt-seconds. *(editable)* |
| Initial Charge Fraction (`InitialChargeFraction`) | `float` | `1.f` | Charge level the battery starts with, as a fraction of its capacity. *(editable)* |
| Max Charge Watts (`MaxChargeWatts`) | `float` | `500.f` | Maximum power drawn from the network while charging. *(editable)* |
| Max Discharge Watts (`MaxDischargeWatts`) | `float` | `1000.f` | Maximum power the battery can deliver. *(editable)* |
| Charge Efficiency (`ChargeEfficiency`) | `float` | `0.9f` | Fraction of the drawn charging power that ends up stored (1 = lossless). *(editable)* |
| Charging Allowed (`bChargingAllowed`) | `bool` | `true` | If false the battery never charges. *(editable)* |
| Discharging Allowed (`bDischargingAllowed`) | `bool` | `true` | If false the battery never discharges (it only stores). *(editable)* |
| Stored Watt Seconds (`StoredWattSeconds`) | `float` | `0.f` | Live value in watt-seconds, read only. *(runtime state)* |
| Battery State (`BatteryState`) | `EVWVBatteryState` | `EVWVBatteryState::Idle` | Live value, read only. *(runtime state)* |
| Power Watts (`PowerWatts`) | `float` | `0.f` | Live value in watts (positive = discharging), read only. *(runtime state)* |

**Events**

| Name | Parameters | Description |
|---|---|---|
| On Battery State Changed (`OnBatteryStateChanged`) | `UVWVBatteryComponent* Battery`, `EVWVBatteryState NewState`, `EVWVBatteryState OldState` | Fires on server and clients when the battery changes between charging, discharging, full and empty. |

**Functions**

| Blueprint name | C++ signature | Description |
|---|---|---|
| Set Charging Allowed | `void SetChargingAllowed(bool bAllowed)` | Allows or forbids charging from surplus power. Server only. |
| Set Discharging Allowed | `void SetDischargingAllowed(bool bAllowed)` | Allows or forbids discharging into the network. Server only. |
| Set Stored Energy | `void SetStoredEnergy(float NewStoredWattSeconds)` | Sets the stored energy directly (watt-seconds). Server only. |
| Get Stored Energy *(pure)* | `float GetStoredEnergy() const` | Stored energy in watt-seconds. |
| Get Charge Fraction *(pure)* | `float GetChargeFraction() const` | Charge level in [0..1]. |
| Get Battery State *(pure)* | `EVWVBatteryState GetBatteryState() const` | Current state: idle, charging, discharging, full or empty. |
| Get Power Watts *(pure)* | `float GetPowerWatts() const` | Power flowing right now: positive = discharging into the network, negative = charging. |
| Get Seconds Until Empty *(pure)* | `float GetSecondsUntilEmpty() const` | Estimated seconds until empty at the current discharge rate, or -1 if not discharging. |

## UVWVBlueprintLibrary (`UVWVBlueprintLibrary`)

Derives from `UBlueprintFunctionLibrary`. Header: `VWVBlueprintLibrary.h`.

Blueprint helpers for working with the Voltweave without touching components directly.

**Functions**

| Blueprint name | C++ signature | Description |
|---|---|---|
| Get Voltweave Grid *(pure)* | `static UVWVGridSubsystem* GetVoltweaveGrid(const UObject* WorldContextObject)` | The grid of the world the context object lives in. |
| Find Grid Node *(pure)* | `static UVWVNodeComponent* FindGridNode(AActor* Actor, TSubclassOf<UVWVNodeComponent> NodeClass)` | Returns the first node of the given type found on an Actor. |
| Get Grid Nodes *(pure)* | `static TArray<UVWVNodeComponent*> GetGridNodes(AActor* Actor)` | Returns every grid node on an Actor. |
| Add Grid Node To Actor | `static UVWVNodeComponent* AddGridNodeToActor(AActor* Actor, TSubclassOf<UVWVNodeComponent> NodeClass, FName ComponentName = NAME_None)` | Makes an existing Actor part of the grid by adding a node component to it at runtime. Server only. Returns the new node. |
| Connect Actors | `static bool ConnectActors(AActor* ActorA, AActor* ActorB)` | Wires the first node of Actor A to the first node of Actor B. Server only. |
| Disconnect Actors | `static bool DisconnectActors(AActor* ActorA, AActor* ActorB)` | Removes the wire between the first nodes of the two Actors. Server only. |
| Is Actor Powered *(pure)* | `static bool IsActorPowered(AActor* Actor)` | True if any grid node of the Actor receives power. Works for consumers (powered or brownout) and passive nodes (energized). |
| Consumer State To Text *(pure)* | `static FText ConsumerStateToText(EVWVConsumerState State)` | Readable name of a consumer state, for UI. |
| Network State To Text *(pure)* | `static FText NetworkStateToText(EVWVNetworkState State)` | Display text for a network state, for example for a HUD. |
| Protection State To Text *(pure)* | `static FText ProtectionStateToText(EVWVProtectionState State)` | Display text for a protection device state. |
| Battery State To Text *(pure)* | `static FText BatteryStateToText(EVWVBatteryState State)` | Display text for a battery state. |
| Format Watts *(pure)* | `static FText FormatWatts(float Watts)` | Formats watts for UI, e.g. 1500 -> "1.5 kW". |

## Voltweave Power Consumer (`UVWVConsumerComponent`)

Derives from `UVWVNodeComponent`. Header: `VWVConsumerComponent.h`.

Draws power from the grid (light, machine, door, turret...).

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Requested Watts (`RequestedWatts`) | `float` | `100.f` | Power the consumer wants in watts while switched on. *(editable)* |
| Switched On (`bSwitchedOn`) | `bool` | `true` | Whether the consumer is switched on and asks for power. *(editable)* |
| Priority (`Priority`) | `int32` | `0` | Lower values are served first when power is short (0 = most important). Only used with the Priority allocation policy. *(editable)* |
| Allow Partial Power (`bAllowPartialPower`) | `bool` | `true` | If false the consumer only runs with its full demand satisfied (it is shed completely otherwise). If true it can brown out. *(editable)* |
| Min Operating Fraction (`MinOperatingFraction`) | `float` | `0.f` | Fraction of the demand below which the consumer gets no power at all (it could not operate anyway). *(editable)* |
| Power State (`PowerState`) | `EVWVConsumerState` | `EVWVConsumerState::Off` | Live value, read only. *(runtime state)* |
| Granted Watts (`GrantedWatts`) | `float` | `0.f` | Live value in watts, read only. *(runtime state)* |

**Events**

| Name | Parameters | Description |
|---|---|---|
| On Power State Changed (`OnPowerStateChanged`) | `UVWVConsumerComponent* Consumer`, `EVWVConsumerState NewState`, `EVWVConsumerState OldState` | Fires on server and clients when the power state changes. |
| On Power Level Changed (`OnPowerLevelChanged`) | `UVWVConsumerComponent* Consumer`, `float Satisfaction` | Fired when the received fraction changes noticeably (at least 1 percent). |

**Functions**

| Blueprint name | C++ signature | Description |
|---|---|---|
| Set Switched On | `void SetSwitchedOn(bool bNewSwitchedOn)` | Switches the consumer on or off. Server only. |
| Set Requested Watts | `void SetRequestedWatts(float NewRequestedWatts)` | Changes the requested power. Server only. |
| Get Power State *(pure)* | `EVWVConsumerState GetPowerState() const` | Current state: off, unpowered, underpowered (brownout) or powered. |
| Get Granted Watts *(pure)* | `float GetGrantedWatts() const` | Power currently received in watts. |
| Get Satisfaction *(pure)* | `float GetSatisfaction() const` | Received / requested power in [0..1]. 1 when powered, 0 when off or unpowered. |
| Is Powered *(pure)* | `bool IsPowered() const` | True while the consumer receives its full demand. |
| Has Power *(pure)* | `bool HasPower() const` | True when the consumer receives any power (Powered or Underpowered). |

## Voltweave State Feedback (`UVWVFeedbackComponent`)

Derives from `UActorComponent`. Header: `VWVFeedbackComponent.h`.

Makes an Actor visibly react to the state of one of its grid nodes, without any Blueprint scripting. Drives lights (color, intensity) and mesh materials (color and emissive parameters) and works on the server and on clients, because it only reads replicated state.

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Node (`Node`) | `FComponentReference` |  | The node to watch. Leave empty to use the first grid node found on this Actor. *(editable)* |
| Targets (`Targets`) | `TArray<FComponentReference>` |  | Lights and meshes to drive. Leave empty to drive every light of the Actor. *(editable)* |
| Preset (`Preset`) | `EVWVFeedbackPreset` | `EVWVFeedbackPreset::IndicatorLED` | Applies one of the ready-made looks to the four states below. *(editable)* |
| Off Look (`OffLook`) | `FVWVFeedbackLook` |  | Look while the node is off or unpowered. *(editable)* |
| Good Look (`GoodLook`) | `FVWVFeedbackLook` |  | Look while the node is working normally. *(editable)* |
| Warning Look (`WarningLook`) | `FVWVFeedbackLook` |  | Look while the node is in a brownout or overheating. *(editable)* |
| Fault Look (`FaultLook`) | `FVWVFeedbackLook` |  | Look while the node is in blackout or tripped. *(editable)* |
| Flicker On Warning (`bFlickerOnWarning`) | `bool` | `false` | Flicker while the node is in the warning state (a brownout for consumers). *(editable)* |
| Scale By Satisfaction (`bScaleBySatisfaction`) | `bool` | `false` | For consumers: additionally scale light intensity and emissive by the received fraction of the demand. *(editable)* |
| Color Parameter Name (`ColorParameterName`) | `FName` | `TEXT("Color")` | Name of the vector material parameter that receives the color. *(editable)* |
| Emissive Parameter Name (`EmissiveParameterName`) | `FName` | `TEXT("Emissive")` | Name of the vector material parameter that receives color times emissive strength. *(editable)* |
| Emissive Strength (`EmissiveStrength`) | `float` | `4.f` | Global multiplier of the emissive strength. *(editable)* |
| Blend Speed (`BlendSpeed`) | `float` | `10.f` | How quickly looks blend from one state to the next (higher = faster). *(editable)* |

**Functions**

| Blueprint name | C++ signature | Description |
|---|---|---|
| Apply Preset | `void ApplyPreset(EVWVFeedbackPreset NewPreset)` | Overwrites the four looks with the values of a preset. |
| Get Look For State *(pure)* | `FVWVFeedbackLook GetLookForState(EVWVIndicatorState State) const` | The look for a given state. |
| Rebind | `void Rebind()` | Re-reads the node and the target list. Call this after adding components at runtime. |

## UVWVGridSubsystem (`UVWVGridSubsystem`)

Derives from `UTickableWorldSubsystem`. Header: `VWVGridSubsystem.h`.

Owns the electrical simulation of one world. Nodes register themselves on BeginPlay. The subsystem is event driven: it re-solves right away when something changes and only keeps stepping in time while batteries or overheating protection devices need it. Only the server (or a standalone game) solves; clients receive replicated results.

**Events**

| Name | Parameters | Description |
|---|---|---|
| On Network State Changed (`OnNetworkStateChanged`) | `const FVWVNetworkInfo& Network`, `EVWVNetworkState PreviousState` | Fired when a network changes its health state, e.g. becomes a blackout. |
| On Grid Solved (`OnGridSolved`) |  | Fired after every solve. |

**Functions**

| Blueprint name | C++ signature | Description |
|---|---|---|
| Solve Now | `void SolveNow()` | Solves immediately instead of waiting for the next tick. Server only. |
| Get Networks | `TArray<FVWVNetworkInfo> GetNetworks() const` | All networks found by the last solve. Server only. |
| Get Network Info | `bool GetNetworkInfo(int32 NetworkId, FVWVNetworkInfo& OutInfo) const` | Information about the network a node belongs to. Server only. |
| Get All Nodes | `TArray<UVWVNodeComponent*> GetAllNodes() const` | All nodes currently registered in this world. |
| Get Node Count | `int32 GetNodeCount() const` | Number of nodes registered in this world. |
| Get Last Solve Time Ms | `float GetLastSolveTimeMs() const` | Duration of the last solve in milliseconds. |
| Is Simulating | `bool IsSimulating() const` | True if this world instance runs the simulation (server or standalone). |

## Voltweave Junction (`UVWVNodeComponent`)

Derives from `USceneComponent`. Header: `VWVNodeComponent.h`.

Base of all electrical components and a plain junction/terminal by itself. Add one of the Voltweave components to any Actor (Blueprint or C++) to make it part of the grid. Nodes are wired together with ConnectTo / InitialConnections. The grid is solved on the server only; the results are replicated, so the owning Actor must have replication enabled in multiplayer games.

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Initial Connections (`InitialConnections`) | `TArray<FVWVConnectionTarget>` |  | Nodes this node is wired to when the game starts. Links are bidirectional. *(editable)* |
| Node Enabled (`bNodeEnabled`) | `bool` | `true` | Whether the node takes part in the network. Replicated. *(editable)* |
| Energized (`bEnergized`) | `bool` | `false` | Live value, read only. *(runtime state)* |
| Network Id (`NetworkId`) | `int32` | `INDEX_NONE` | Live value, read only. *(runtime state)* |

**Events**

| Name | Parameters | Description |
|---|---|---|
| On Energized Changed (`OnEnergizedChanged`) | `UVWVNodeComponent* Node`, `bool bEnergized` | Fires on server and clients when the node gains or loses power from its network. |

**Functions**

| Blueprint name | C++ signature | Description |
|---|---|---|
| Connect To | `bool ConnectTo(UVWVNodeComponent* Other)` | Wires this node to another one. Server only. Returns false if invalid or already connected. |
| Disconnect From | `bool DisconnectFrom(UVWVNodeComponent* Other)` | Removes the wire between this node and another one. Server only. |
| Disconnect All | `void DisconnectAll()` | Removes every wire of this node. Server only. |
| Is Connected To *(pure)* | `bool IsConnectedTo(const UVWVNodeComponent* Other) const` | True if a wire connects this node directly to Other. |
| Get Connections *(pure)* | `TArray<UVWVNodeComponent*> GetConnections() const` | All nodes this node is directly wired to. Available on server and clients. |
| Set Node Enabled | `void SetNodeEnabled(bool bEnabled)` | A disabled node does not conduct, like a cut wire. Server only. |
| Is Node Enabled *(pure)* | `bool IsNodeEnabled() const` | False while the node is disabled and acts like a cut wire. |
| Is Energized *(pure)* | `bool IsEnergized() const` | True if this node belongs to a network that has supply available. Available on server and clients. |
| Get Network Id *(pure)* | `int32 GetNetworkId() const` | Identifier of the network this node currently belongs to. Available on server and clients. |
| Get Network Info *(pure)* | `bool GetNetworkInfo(FVWVNetworkInfo& OutInfo) const` | Aggregated information about this node's network. Server only (returns false on clients). |
| Has Grid Authority *(pure)* | `bool HasGridAuthority() const` | True where the grid is simulated: the server or a standalone game. |
| Get Debug Label *(pure)* | `virtual FString GetDebugLabel() const` | Short human readable description of the current state, used by debug drawing and logs. |
| Get Indicator State *(pure)* | `virtual EVWVIndicatorState GetIndicatorState() const` | Simplified state for indicator lights and UI. Available on server and clients. |

## Voltweave Breaker / Fuse (`UVWVProtectionComponent`)

Derives from `UVWVNodeComponent`. Header: `VWVProtectionComponent.h`.

Circuit breaker or fuse. Sits in series in the network and measures the power flowing through it. When the flow exceeds the rating for long enough (inverse-time curve) it opens and cuts off everything behind it.

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Kind (`Kind`) | `EVWVProtectionKind` | `EVWVProtectionKind::Breaker` | Breakers can be reset, fuses must be replaced. *(editable)* |
| Rated Watts (`RatedWatts`) | `float` | `1000.f` | Power that may flow through the device continuously. 0 disables the protection. *(editable)* |
| Time To Trip At Double Load (`TimeToTripAtDoubleLoad`) | `float` | `3.f` | Seconds until the device opens when it carries twice its rating. Smaller overloads take longer, bigger ones are faster. *(editable)* |
| Instant Trip Ratio (`InstantTripRatio`) | `float` | `4.f` | Flow as a multiple of the rating at or above which the device opens instantly (short circuit). 0 disables. *(editable)* |
| Cooling Time Seconds (`CoolingTimeSeconds`) | `float` | `10.f` | Seconds the device needs to cool down completely. *(editable)* |
| Auto Reset Delay Seconds (`AutoResetDelaySeconds`) | `float` | `0.f` | Breakers only: seconds after a trip until the breaker closes by itself. 0 = never. *(editable)* |
| State (`State`) | `EVWVProtectionState` | `EVWVProtectionState::Closed` | Initial state. Use Open to start with an opened breaker. *(editable)* |
| Flow Watts (`FlowWatts`) | `float` | `0.f` | Live value in watts, read only. *(runtime state)* |
| Heat (`Heat`) | `float` | `0.f` | Live value in [0..1], read only. The device opens at 1. *(runtime state)* |

**Events**

| Name | Parameters | Description |
|---|---|---|
| On Protection State Changed (`OnProtectionStateChanged`) | `UVWVProtectionComponent* Device`, `EVWVProtectionState NewState`, `EVWVProtectionState OldState` | Fires on server and clients when the device closes, trips or blows. |
| On Tripped (`OnTripped`) | `UVWVProtectionComponent* Device` | Fired when the device opened because of an overload. |

**Functions**

| Blueprint name | C++ signature | Description |
|---|---|---|
| Open Breaker | `bool OpenBreaker()` | Manually opens a breaker. Server only. Fuses cannot be opened. |
| Close Breaker | `bool CloseBreaker()` | Manually closes a breaker or resets a tripped one. Server only. Fails for blown fuses. |
| Replace Fuse | `bool ReplaceFuse()` | Replaces a blown fuse with a new one. Server only. |
| Force Trip | `bool ForceTrip()` | Forces the device to trip (breaker) or blow (fuse). Server only. |
| Get Protection State *(pure)* | `EVWVProtectionState GetProtectionState() const` | Current state: closed, tripped or blown. |
| Is Tripped Or Blown *(pure)* | `bool IsTrippedOrBlown() const` | True if the device was opened by an overload. |
| Get Flow Watts *(pure)* | `float GetFlowWatts() const` | Power currently flowing through the device. |
| Get Load Ratio *(pure)* | `float GetLoadRatio() const` | Flow relative to the rating (1 = at the limit). |
| Get Heat *(pure)* | `float GetHeat() const` | Accumulated heat in [0..1]. The device opens at 1. |

## Voltweave (`UVWVSettings`)

Derives from `UDeveloperSettings`. Header: `VWVSettings.h`.

Project-wide settings of the Voltweave plugin (Project Settings > Plugins > Voltweave).

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Solver Frequency Hz (`SolverFrequencyHz`) | `float` | `20.f` | How many times per second the network is re-evaluated while something time dependent is happening (battery, overheating protection). Topology and state changes are always solved immediately. *(editable)* |
| Allocation Policy (`AllocationPolicy`) | `EVWVAllocationPolicy` | `EVWVAllocationPolicy::Priority` | How available power is shared when there is not enough for everyone. *(editable)* |
| Max Cascade Iterations (`MaxCascadeIterations`) | `int32` | `8` | Upper bound of re-solves caused by protection devices tripping within one evaluation (cascading trips). *(editable)* |
| Draw Debug By Default (`bDrawDebugByDefault`) | `bool` | `false` | Draw nodes, links and their state in the world while playing (also toggled by the console variable Voltweave.Debug.Draw). *(editable)* |
| Log Network Events (`bLogNetworkEvents`) | `bool` | `false` | Writes network changes (blackouts, trips) to the log. *(editable)* |

## Voltweave Power Source (`UVWVSourceComponent`)

Derives from `UVWVNodeComponent`. Header: `VWVSourceComponent.h`.

Produces power (generator, solar panel, mains connection...).

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Max Output Watts (`MaxOutputWatts`) | `float` | `1000.f` | Maximum power the source can deliver in watts. *(editable)* |
| Running (`bRunning`) | `bool` | `true` | Whether the source is running. *(editable)* |
| Output Scale (`OutputScale`) | `float` | `1.f` | Scales the capacity between 0 and 1, for example to model a throttled generator or the sun's angle. *(editable)* |
| Output Watts (`OutputWatts`) | `float` | `0.f` | Live value in watts, read only. *(runtime state)* |

**Events**

| Name | Parameters | Description |
|---|---|---|
| On Running Changed (`OnRunningChanged`) | `UVWVSourceComponent* Source`, `bool bRunning` | Fires on server and clients when the source is started or stopped. |
| On Output Changed (`OnOutputChanged`) | `UVWVSourceComponent* Source`, `float OutputWatts` | Fires on server and clients when the delivered output changes noticeably. |

**Functions**

| Blueprint name | C++ signature | Description |
|---|---|---|
| Set Running | `void SetRunning(bool bNewRunning)` | Starts or stops the source. Server only. |
| Set Max Output Watts | `void SetMaxOutputWatts(float NewMaxOutputWatts)` | Changes the maximum output. Server only. |
| Set Output Scale | `void SetOutputScale(float NewScale)` | Changes the capacity scale in [0..1]. Server only. |
| Get Available Watts *(pure)* | `float GetAvailableWatts() const` | Capacity the source offers right now (0 if stopped or disabled). |
| Get Output Watts *(pure)* | `float GetOutputWatts() const` | Power the source currently delivers. |
| Get Load Fraction *(pure)* | `float GetLoadFraction() const` | Current output relative to the available capacity [0..1]. |

## Voltweave Switch (`UVWVSwitchComponent`)

Derives from `UVWVNodeComponent`. Header: `VWVSwitchComponent.h`.

A manual switch. Power flows through it only while it is closed.

**Properties**

| Name | Type | Default | Description |
|---|---|---|---|
| Closed (`bClosed`) | `bool` | `true` | Initial position and current state. A closed switch conducts. *(editable)* |

**Events**

| Name | Parameters | Description |
|---|---|---|
| On Switch Changed (`OnSwitchChanged`) | `UVWVSwitchComponent* Switch`, `bool bClosed` | Fires on server and clients when the switch opens or closes. |

**Functions**

| Blueprint name | C++ signature | Description |
|---|---|---|
| Set Closed | `void SetClosed(bool bNewClosed)` | Opens or closes the switch. Server only. |
| Toggle | `bool Toggle()` | Flips the switch. Server only. Returns the new state (true = closed). |
| Is Closed *(pure)* | `bool IsClosed() const` | True while the switch conducts. |

