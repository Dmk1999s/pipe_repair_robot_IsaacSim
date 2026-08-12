<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacTimeSplitter.html | title: Isaac Time Splitter — Isaac Sim -->

# Isaac Time Splitter
Spit time values

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Time ( inputs:time ) | ['double', 'float', 'half', 'int', 'int64', 'uint', 'uint64'] | Time (in seconds) | None
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Microseconds ( outputs:microseconds ) | uint | Microseconds [0, 1e6) | None
Milliseconds ( outputs:milliseconds ) | uint | Milliseconds [0, 1e3) | None
Nanoseconds ( outputs:nanoseconds ) | uint | Nanoseconds [0, 1e9) | None
Seconds ( outputs:seconds ) | int | Seconds [INT_MIN, INT_MAX] | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacTimeSplitter
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacTimeSplitter.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Time Splitter
Categories | isaacCore
Generated Class Name | OgnIsaacTimeSplitterDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
