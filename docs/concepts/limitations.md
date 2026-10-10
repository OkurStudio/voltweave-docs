# Limitations

Voltweave 0.2 is a power budget model for games. It deliberately does not do some things:

* **No electrical quantities.** There is no voltage, frequency or phase, and wires have no capacity of their own: a cable carries any amount of power. Use breakers and fuses to limit a line.
* **Protection flow in meshed networks.** A protection device measures flow exactly in radial networks. In networks with loops it reports the sum of the deficits of the parts it separates.
* **Network totals on clients.** Statistics of whole networks (**Get Networks**, **Get Network Info** on the subsystem) exist only where the grid is simulated. Clients can still read every node's own values, its *Network Id* and its *Energized* flag.
* **No save and load integration.** Node state is stored in ordinary properties on the components, so your own save system can store and restore it.
* **Re-running a construction script while playing** recreates its node components. Cables and *Initial Connections* re-wire automatically; wiring you made yourself with **Connect To** has to be made again. In C++ use the native hook described in the [C++ guide](../guides/cpp.md).
* **Platform and engine version.** Windows 64-bit and Unreal Engine 5.8 only. Other platforms and versions are neither built nor tested.
* **Not stress tested:** networks that span World Partition streaming cells.
