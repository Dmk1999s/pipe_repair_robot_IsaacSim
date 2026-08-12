<!-- source: replicator_tutorials/tutorial_replicator_augmentation.html | title: Data Augmentation — Isaac Sim Documentation -->

# Data Augmentation
Example of using Isaac Sim and Replicator to capture augmented synthetic data.

## Learning Objectives
This tutorial provides examples on how to use omni.replicator augmentations on annotators or writers. The provided examples will showcase how to augment rgb and depth annotator data using warp (GPU) or NumPy (CPU) kernel/filters. The use of warp is particularly advantageous for executing parallelizable tasks, especially if the data already resides in the GPUs memory, thus avoiding memory copies from GPU to CPU.

- For a better understanding of the tutorial, familiarity with omni.replicator , annotators , writers and warp is recommended.

## Scenario
[image: ../_images/isaac_tutorial_replicator_augmentation.png]The depicted figure showcases the example augmentations used throughout the examples. The first image is an illustrative example switching the red and blue channels of the image. The second image is a composed augmentation of converting the rgb data to hsv, adding gaussian noise, and converting back to rgb. The third and forth image are results of applying gaussian noise filters with various sigma values to the depth data.
For the example scenario a red cube is spawned with a camera looking at it from a top view. For the cube a replicator randomization graph is created which will trigger a random rotation for every frame capture.

## Implementation
The tutorial is split into two parts, the first example will showcase how to augment annotators directly, and secondly how to augment writers. Both examples can be run as Standalone Applications or from the UI using the Script Editor .

### Annotator Augmentation
The annotator example will output rgb images with the red and blue channels switched, and two depth images with different gaussian noise levels (saved as grayscale PNGs). The example can switch between using warp or NumPy augmentations.

### Writer Augmentation
The writer example will output gaussian noise augmented RGB and depth annotator data from a writer.
