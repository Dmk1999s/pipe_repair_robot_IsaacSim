<!-- source: replicator_tutorials/tutorial_replicator_overview.html | title: Overview — Isaac Sim Documentation -->

# Overview
Isaac Sim Replicator offers various tools and workflows for synthetic data generation (SDG), with its core functionalities mostly provided by, but not limited to, the omni.replicator extension. This page provides an overview of these tools and extensions, including semantic labeling, sensor visualization, GUI-based data recording, config file-based SDG workflows, and getting started scripts (examples). To enable SDG relevant UI panels you can use the Synthetic Data Generation Layout .

## The Semantics Schema Editor
The Semantics Schema Editor is a GUI-based extension that enables you to view, add, edit, or remove semantic labels on prims in a stage. Semantically labeling prims is necessary for annotators like semantic segmentation or bounding boxes to include semantic information in the synthetic data. You can access the editor through Tools > Replicator > Semantics Schema Editor. To programmatically label prims in a stage, see the following example snippet .
[image: Semantics Schema Editor]

## The Synthetic Data Visualizer
The Synthetic Data Visualizer tool enables sensor output visualization directly in the Viewport window, it can be accessed using the icon and selecting the desired output formats.
[image: Synthetic Data Visualizer]Note

- Cross Correspondence visualization requires a specific two-camera setup explained in the Cross Correspondence section of the annotator details page.

## The Synthetic Data Recorder
The Synthetic Data Recorder is a GUI-based tool that allows you to record synthetic data directly from the editor. It is built on top of `omni.replicator` using `BasicWriter` as its default writer, it is useful for rapid iterations of synthetic data recordings for testing purposes. You can access the recorder via Tools > Replicator > Synthetic Data Recorder.
[image: Synthetic Data Recorder]

## Replicator YAML
Replicator YAML is a configuration file-based workflow built on top of the Replicator API. It allows you to define randomizations and data capture pipelines as configuration files. These configurations are transformed through the Replicator API into an OmniGraph workflow for synthetic data generation. You can access the YAML workflow using Tools > Replicator > Replicator YAML.

## Getting Started Scripts
The Getting Started Scripts provides a starting point for typical Isaac Sim Replicator workflows. These tutorials cover basic topics such as accessing data from annotators or writers , and using Replicator randomizers together with custom USD/Isaac Sim API randomizers triggered independently from the data capture.
