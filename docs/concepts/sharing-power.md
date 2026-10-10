# Sharing power

When demand is larger than supply, the **allocation policy** decides who gets what. You choose it in the [project settings](../components/settings.md).

* **Priority** (default): consumers are served by their *Priority*, where 0 comes first. Consumers with the same priority share what is left proportionally.
* **Proportional**: everybody receives the same fraction of their demand.

## Refining it per consumer

* **Allow Partial Power** off: the consumer is **all-or-nothing**. It is shed completely if its full demand cannot be met. Good for machines.
* **Min Operating Fraction**: below this fraction of its demand the consumer gets nothing, so the power goes to others instead of being wasted on something that cannot run.

A consumer is `Off` (not requesting), `Unpowered` (requesting, receiving nothing), `Underpowered` (a brownout) or `Powered`.

## Sources and batteries

* Sources share the load in proportion to their capacity.
* Batteries only discharge when the sources cannot cover the demand, and only charge from surplus. A battery never charges and discharges at the same time.

!!! example "See it in the demo"
    Bay 4 of the [demo hall](../demo.md) offers 500 W for 600 W of demand: the critical lamp and the machine are served first and the two low-priority lamps brown out. See also the [priorities scenario](../scenarios/priorities-and-brownouts.md).
