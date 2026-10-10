# FAQ

## Setup

**Do I need C++ or Visual Studio?**
You do not write any C++; everything is available from Blueprints and the Details panel. Whether you need a compiler depends on what you do:

* *Using Voltweave in the editor and Play In Editor:* if your copy contains compiled Editor binaries, no compiler is needed. If Unreal asks to rebuild the plugin modules when opening the project (this is what happens with the source package), you need Visual Studio 2022 with the *Game development with C++* workload once.
* *Packaging a game:* in our tests a Blueprint-only project could not load Voltweave in the packaged game ("module could not be found"), and the same project converted to a C++ project could. Plan on a C++ project (add any C++ class with *Tools > New C++ Class*) and a C++ toolchain. We are still confirming whether a copy installed through the Fab launcher behaves differently.

**Which platforms and engine versions are supported?**
Windows 64-bit and Unreal Engine 5.8 only. The code is plain C++ without platform specific parts, but other platforms and engine versions are neither built nor tested.

**Does it need Enhanced Input or change my input settings?**
No. Only the optional demo plugin uses Enhanced Input, and it creates its own mapping in code without touching your project's input settings.

## Using it

**Does it work with my existing Actors?**
Yes. Add components to any Actor Blueprint or placed Actor. The components do not care about the Actor's class.

**Where is the Blueprint node for X?**
Search for "Voltweave" in the Blueprint context menu; everything is under the *Voltweave* categories. The [complete reference](api/reference.md) lists the Blueprint name of every function.

**Is it a real circuit simulation?**
No. It is a power budget model designed for games; see [How the grid works](concepts/how-it-works.md).

**How do I make a door that needs power?** See the [door scenario](scenarios/door.md).

**How do I make an emergency light?** See the [emergency light scenario](scenarios/emergency-light.md).

**How do I model a solar panel?** See the [solar panel scenario](scenarios/solar-panel.md).

**Can I connect more than two things?**
Yes. A node may have any number of wires; use junctions as distribution points.

**Can wires be cut or created while playing?**
Yes, on the server: **Connect To**, **Disconnect From**, **Set Node Enabled**. See [Wiring](guides/wiring.md).

**What happens when I mis-wire something?**
Run **Build > Check Map**. At runtime invalid numbers are treated as zero instead of breaking the grid, and calls from clients log a rate-limited warning. See [Troubleshooting](troubleshooting.md).

**Can I use the Blueprint Actors in my game?**
Yes, they are ordinary Blueprints. Duplicate and change them freely. They use only engine basic shapes and one material.

## Scale and features

**How many nodes can I have?**
In a development benchmark, a network of 2001 nodes with 40 breakers was evaluated in about 1.8 ms on a development PC. Large worlds usually consist of many small networks, which is cheaper. See [Time, updates and authority](concepts/time-and-authority.md).

**Does it support World Partition and streaming?**
Nodes register when they begin play and unregister when they end. Wires to nodes that are not loaded are created when both ends exist (cables retry when an end registers). Networks that span streaming cells were not stress tested.

**Does it save and load?**
There is no built-in save integration in this version. Node state is stored in plain properties on the components (switch positions, battery charge, fuse state and so on), so your own save system can store and restore it.

**Is it multiplayer ready?**
Yes: the grid is server authoritative and the state is replicated. See [Multiplayer](multiplayer.md).
