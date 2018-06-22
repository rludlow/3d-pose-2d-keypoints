# 3d Human Pose Estimation from 2d Keypoints



## Overview

While humans can generally estimate with ease the 3d pose of a human in a 2d image, 3d pose estimation remains a challenging problem for machines. This project improves an algorithm that estimates 3d keypoints of human poses with 2d keypoints as the only input.

I pursue three key interventions to improve performance: a) modify the data normalization technique in preprocessing, b) modify the neural network architecture from a simple densely connected network to a multi-stage network modeled after state-of-the-art 2d pose estimation models, and c) generate synthetic data to augment training sets.

Full Paper: [3d Human Pose Estimation from 2d Keypoints](https://github.com/rludlow/3d-pose-2d-keypoints/blob/present/Ludlow_3d_pose_2d_keypoints.pdf) (pdf)

![Before After](https://github.com/rludlow/3d-pose-2d-keypoints/blob/present/utils/pose_before_after_colors.png)

## Dependencies
- [Tensorflow 1.1](https://www.tensorflow.org/)
- [Keras 2.1.5](https://keras.io/)  

## Using

###Training and Testing
Run `prep_data.py`
Run `train.py`. A datetime is appended to these files. To use these in the subsequent step, archive the existing files and remove the datetime suffix of your new files.

###Testing Only
Run `prep_data.py`, commenting out
`train.py`

## Reference

	  @InProceedings{Zhao_2017,
	  author = {Ruiqi Zhao, Yan Wang, and Aleix M Martines},
	  title = {A Simple, Fast, and Highly-Accurate Algorithm to Recover 3D Shape from 2D Landmarks on a Single Image},
	  booktitle = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
	  month = {November},
	  year = {2017}
	  }
