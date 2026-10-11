# Using Voltweave in C++

You do not need C++ to use Voltweave, but everything is available from it. The examples on this page are real files: each one is compiled against the plugin headers whenever the documentation is built (see [How the examples are verified](#how-the-examples-are-verified)).

## Setup

Add the module to your game module's `Build.cs`:

```csharp title="MyGame.Build.cs"
--8<-- "MyGameBuild.cs"
```

Include the headers you need, for example `Components/VWVConsumerComponent.h` for a consumer, `VWVGridSubsystem.h` for the grid subsystem and `VWVBlueprintLibrary.h` for the helper functions. Every class has the prefix `VWV`: `UVWVNodeComponent` (the base of all nodes), `UVWVSourceComponent`, `UVWVConsumerComponent`, `UVWVSwitchComponent`, `UVWVProtectionComponent`, `UVWVBatteryComponent`, `UVWVFeedbackComponent`, `AVWVCableActor` and `UVWVGridSubsystem`.

!!! note "Server only"
    Functions that change the grid have an effect only on the server (or in a standalone game). On a client they log a warning and do nothing. `HasGridAuthority()` on a node tells you where you are. Read-only functions work everywhere.

## A node on your own Actor

An Actor class with a power consumer, reacting to its state. The event handler runs on the server and on clients, so it is the right place for visuals.

```cpp title="MyPowerDoor.h"
--8<-- "MyPowerDoor.h"
```

```cpp title="MyPowerDoor.cpp"
--8<-- "MyPowerDoor.cpp"
```

The consumer is created like any other component (`CreateDefaultSubobject`), and the Actor replicates so clients receive the state. Wire the door to a generator with a cable Actor or with *Initial Connections*, as in Blueprints.

## Add nodes and wires at runtime

On the server, `UVWVBlueprintLibrary::AddGridNodeToActor` adds a node component to an Actor that already exists and returns it. Use the setters (`SetMaxOutputWatts`, `SetRequestedWatts`) after registration so that the grid learns about the change, and `ConnectTo` to wire.

```cpp title="MyGridBootstrap.h"
--8<-- "MyGridBootstrap.h"
```

```cpp title="MyGridBootstrap.cpp"
--8<-- "MyGridBootstrap.cpp"
```

## Watch whole networks

The world subsystem `UVWVGridSubsystem` knows every network. Its totals exist only where the grid is simulated, so check `IsSimulating()` first.

```cpp title="MyGridWatcher.h"
--8<-- "MyGridWatcher.h"
```

```cpp title="MyGridWatcher.cpp"
--8<-- "MyGridWatcher.cpp"
```

## Redo wiring when a node is recreated

When an Actor's construction script runs again while playing, its node components are recreated and wires made with `ConnectTo` are lost. The subsystem announces every node that registers through a native (non-Blueprint) delegate, so you can connect again.

```cpp title="MyGridRewirer.h"
--8<-- "MyGridRewirer.h"
```

```cpp title="MyGridRewirer.cpp"
--8<-- "MyGridRewirer.cpp"
```

Wires made with a Cable Actor or with *Initial Connections* need none of this: they re-wire themselves.

## Let a player act on the grid

Component functions are not RPCs. In multiplayer a client asks the server to act through an Actor it owns, usually its pawn. Always validate on the server.

```cpp title="MyGridPlayer.h"
--8<-- "MyGridPlayer.h"
```

```cpp title="MyGridPlayer.cpp"
--8<-- "MyGridPlayer.cpp"
```

More on this on the [Multiplayer](../multiplayer.md) page.

## The solver on its own

The allocation algorithm and the thermal protection model are plain C++ without Unreal objects (`VWVSolver` and `VWVProtectionModel` in the `Solver` folder of the public headers), so they can be used or unit tested in isolation.

## How the examples are verified

The code blocks above are included from the `snippets` folder of the documentation repository. The script `tools/verify_snippets.ps1` copies them into a UE 5.8 project that contains the plugin and builds it, so a changed or removed API breaks the verification instead of the reader. The examples on this page were verified against Voltweave 0.2.0-rc.3. They show compilation against the real API; they are not full game code (the door has no mesh asset assigned, for example). The examples use `MYGAME_API` as the export macro: use your own module's macro.
