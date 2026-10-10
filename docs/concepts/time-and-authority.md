# Time, updates and authority

## Event driven

The grid is **event driven**. Any change (a switch, a wire, a request, a battery becoming full) re-evaluates the affected network right away. The grid only advances in time, in fixed steps of *Solver Frequency Hz*, while something needs it: a battery is charging or discharging, a protection device is heating or cooling, or an auto-reset timer is running. An idle grid costs nothing per frame.

Component events are delivered **after** an evaluation has finished, so it is safe to change the grid from inside an event handler.

## Authority

Only the **server** (or a standalone game) simulates the grid and may change it. Everything a client needs to *show* the grid is replicated, and the component events fire on clients too when the replicated state arrives. See [Multiplayer](../multiplayer.md).

## Performance

The evaluation runs on the game thread. Its cost grows linearly with the number of nodes and wires, and each protection device additionally walks its network once. In an automated benchmark during development, a distribution tree of 2001 nodes with 40 breakers was evaluated in about 1.8 ms on a development PC (Development build, the solver only; reading the data from the components adds a little). **Get Last Solve Time Ms** on the [grid subsystem](../api/grid-subsystem.md) shows the real number for your own grid. Large worlds usually consist of many small networks, which is cheaper than one huge one.
