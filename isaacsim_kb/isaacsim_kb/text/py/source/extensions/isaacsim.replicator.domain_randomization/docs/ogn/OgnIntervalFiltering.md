<!-- source: py/source/extensions/isaacsim.replicator.domain_randomization/docs/ogn/OgnIntervalFiltering.html | title: Interval Filter — Isaac Sim -->

# Interval Filter
Outputs indices if their frame count is a multiple of the interval

## Installation
To use this node enable isaacsim.replicator.domain_randomization in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | exec | None
Frame Counts ( inputs:frameCounts ) | int[] | the current frame number for every environment | []
Ignore Interval ( inputs:ignoreInterval ) | bool | if true, will just pass indices to downstream node | False
Indices ( inputs:indices ) | int[] | a list of indices to use in case of ignoring interval | []
Interval ( inputs:interval ) | int | randomization will take place once every interval frames | 0
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | exec | None
Indices ( outputs:indices ) | int[] | the indices that are at the interval and need to be randomized | None
On Reset ( outputs:on_reset ) | bool | indicates whether an on_reset context triggered the execution | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.replicator.domain_randomization.OgnIntervalFiltering
Version | 1
Extension | isaacsim.replicator.domain_randomization
Has State? | False
Implementation Language | Python
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Interval Filter
Categories | Replicator
__categoryDescriptions | Replicator,Write Attribute
Generated Class Name | OgnIntervalFilteringDatabase
Python Module | isaacsim.replicator.domain_randomization
[/TABLE]
