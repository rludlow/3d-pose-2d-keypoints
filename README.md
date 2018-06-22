# 3d Human Pose Estimation from 2d Keypoints

## Overview

While humans can generally estimate with ease the 3d pose of a human in a 2d image, 3d pose estimation remains a challenging problem for machines. This project improves an algorithm that estimates 3d keypoints of human poses with 2d keypoints as the only input.

I pursue three key interventions to improve performance: a) modify the data normalization technique in preprocessing, b) modify the neural network architecture from a simple densely connected network to a multi-stage network modeled after state-of-the-art 2d pose estimation models, and c) generate synthetic data to augment training sets.

![Before After](https://github.com/rludlow/3d-pose-2d-keypoints/blob/present/utils/pose_before_after.png)

## Dependencies
- [Tensorflow 1.1] (https://www.tensorflow.org/)
- [Keras 2.1.5] (https://keras.io/)  

## Training

`prep_data.py`
`train.py`
