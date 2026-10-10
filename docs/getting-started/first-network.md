# Your first power network

In about five minutes you build a generator that powers a lamp, using only the ready-made Actors. No Blueprint scripting and no C++ is needed.

**Before you start:** the plugin is [installed and enabled](installation.md) and *Show Plugin Content* is on.

## 1. Place the Actors

1. Open any level, or create a new one.
2. In the Content Browser open `Voltweave Content/Blueprints`.
3. Drag **BP_VWV_Generator** into the level.
4. Drag **BP_VWV_Lamp** into the level, a few meters away.

## 2. Connect them with a cable

1. Drag **BP_VWV_Cable** into the level.
2. Select the cable. In the Details panel set **Start > Actor** to the generator and **End > Actor** to the lamp. Use the picker (the eyedropper) and click each Actor in the viewport.
3. Leave *Component Name* empty. Each ready-made Actor has exactly one node.

The cable connects the two nodes when the game starts and draws itself between them.

## 3. Play

Press **Play**. The lamp lights up and the cable turns green.

Now watch the grid work:

* While playing, select the lamp in the **World Outliner** and select its *PowerConsumer* component. In the Details panel open **Voltweave | Runtime State**: *Power State* is `Powered` and *Granted Watts* is 100.
* Select the generator's *PowerSource* component and untick **Running**. The lamp goes dark and its *Power State* becomes `Unpowered`. Tick it again and the lamp comes back.
* Open the console (the tilde key) and enter `Voltweave.Debug.Draw 1` to see every node, wire and state drawn in the world.

## 4. Make it bigger

* Change the lamp's **Requested Watts** to 1500, which is more than the generator's 1000 W. The lamp is now `Underpowered` and dims.
* Add a second **BP_VWV_Generator** and connect it to the lamp with another cable. The power adds up and the lamp is `Powered` again.
* Put a **BP_VWV_Switch** between generator and lamp: connect the generator to the switch and the switch to the lamp (two cables). Closing and opening the switch while playing cuts and restores the power.

!!! tip "Not sure why something stays dark?"
    Run **Build > Check Map**. Voltweave reports nodes that are connected to nothing, cables with a missing end, lights that cannot change at runtime and similar mistakes. See [Troubleshooting](../troubleshooting.md).

## Where to go next

* [The ready-made Actors and how to build your own](../guides/blueprint.md)
* [Example scenarios](../scenarios/index.md): a door that needs power, an emergency light, a solar panel, a fuse box
* [How the grid works](../concepts/how-it-works.md)
