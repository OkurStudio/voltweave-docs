# Blueprint function library

C++ class `UVWVBlueprintLibrary`. The functions are available in every Blueprint graph under the category **Voltweave**.

| Function | Description |
|---|---|
| **Get Voltweave Grid** | The [grid subsystem](grid-subsystem.md) of the current world. |
| **Find Grid Node** | The first node of a given class on an Actor. Pass `Voltweave Junction` to get the first node of any kind. |
| **Get Grid Nodes** | All nodes of an Actor. |
| **Add Grid Node To Actor** | Adds a node component of a given class to an existing Actor and returns it. Server only. The component replicates when the Actor replicates. |
| **Connect Actors** | Wires the first node of one Actor to the first node of another. Server only. Returns whether it succeeded. |
| **Disconnect Actors** | Removes the wire between two Actors. Server only. Returns whether it succeeded. |
| **Is Actor Powered** | True if any consumer of the Actor has power, or any other node of the Actor is energized. |
| **Consumer State To Text**, **Network State To Text**, **Protection State To Text**, **Battery State To Text** | Readable names for your interface. |
| **Format Watts** | Formats a power value for display, for example `1500` becomes `1.5 kW`. |

## C++ example

```cpp title="MyLibraryUsage.cpp"
--8<-- "MyLibraryUsage.cpp"
```

The header of this example is `MyLibraryUsage.h` in the [documentation repository's snippets](../guides/cpp.md#how-the-examples-are-verified).

See also: [Wiring](../guides/wiring.md), [complete reference](reference.md).
