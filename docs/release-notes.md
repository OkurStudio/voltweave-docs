# Release notes

## 0.2.0-rc.2 (release candidate)

Packaging and documentation only. No gameplay features and no solver, component or content changes.

* Publisher and copyright set: every source file carries the copyright line of the legal owner, and the plugin descriptors name the publisher OkurStudio.
* The installation and requirements documents now separate editor use from packaging a game, and state which behaviours are tested and which are still being confirmed.
* The package archives use forward-slash paths.

## 0.2.0-rc.1 (release candidate)

Quality release on top of 0.1.0. No new gameplay features.

* Renamed to **Voltweave** (class prefix `VWV`).
* The demo moved to the optional **Voltweave Demo** plugin. The core plugin no longer depends on Enhanced Input and does not change any input settings.
* New: Map Check validation (unwired nodes, broken cables, feedback without a node or with static lights, inert settings).
* Fault tolerance: invalid numbers (NaN, infinity, negative) are sanitised in the solver; *Initial Connections* that point at Actors spawned later connect when those Actors begin play; cables re-wire recreated nodes; State Feedback waits for a node that is added at runtime and keeps the lights' authored intensity across rebinds.
* Authority warnings from clients are rate limited instead of flooding the log.
* New tutorials; the demo HUD scales with resolution, offers `R` restart and `Esc` quit, with a brighter hall and readable boards.
* 33 automated tests in development (random graph invariants, validation, robustness) plus a server and client replication scenario.

## 0.1.0

First feature-complete build for Unreal Engine 5.8.

* Solver: networks, priority and proportional allocation, all-or-nothing consumers and minimum fraction, redundancy, batteries, protection flow.
* Components: Junction, Power Source, Power Consumer, Switch, Breaker / Fuse, Battery, State Feedback; Cable Actor.
* Grid subsystem with network events, console commands and project settings.
* Server-authoritative replication of all state.
* Editor: wiring visualizer, live runtime state in the Details panel, Voltweave Debugger tab.
* Demo level with six bays and ready-made Blueprint Actors.
