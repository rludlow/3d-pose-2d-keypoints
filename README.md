# 3d Human Pose Estimation from 2d Keypoints



## Overview

While humans can generally estimate with ease the 3d pose of a human in a 2d image, 3d pose estimation remains a challenging problem for machines. This project improves an algorithm that estimates 3d keypoints of human poses with 2d keypoints as the only input.

I pursue three key interventions to improve performance: a) modify the data normalization technique in preprocessing, b) modify the neural network architecture from a simple densely connected network to a multi-stage network modeled after state-of-the-art 2d pose estimation models, and c) generate synthetic data to augment training sets.

Full Paper: [3d Human Pose Estimation from 2d Keypoints](https://github.com/rludlow/3d-pose-2d-keypoints/blob/present/Ludlow_3d_pose_2d_keypoints.pdf) (pdf)

![Before After](https://github.com/rludlow/3d-pose-2d-keypoints/blob/present/utils/pose_before_after_colors.png)

## Dependencies
- [Tensorflow 1.1](https://www.tensorflow.org/)
- [Keras 2.1.5](https://keras.io/)
- Only for prepping data from scratch: [Blender](https://www.blender.org/)

## Training and Testing

### Training
- Run `prep_data.py`
- Run `train.py`, commenting out any model settings you don't want to train. A datetime is appended to these files. To use these in the subsequent step, archive the existing files and remove the datetime suffix of your new files.

### Testing
Test results can be seen in `model_analysis.ipynb`. This notebook is not formatted with the intent of presenting the data (the [research paper](https://github.com/rludlow/3d-pose-2d-keypoints/blob/present/Ludlow_3d_pose_2d_keypoints.pdf) is), but the results can be seen there.

### Prepping Data from Scratch

For the instructions in the sub-sections above, the data has already been downloaded and converted into 3d coordinates. If you want to start from scratch and convert the data from bvh files to 3d coordinates, you can proceed as follows with Blender installed:

- The program uses CMU Motion Capture Subjects 86 for training and 13-15 for testing. Download the following groups of bvh files:       [Subjects 10-14](http://www.mediafire.com/?z6pr5bk3h1o5045),
			[Subjects 15-19](http://www.mediafire.com/?cu0a99w1day8hnr),
			[Subjects 86-94](http://www.mediafire.com/?r6y8sc60mabhneu). ([main site](https://sites.google.com/a/cgspeed.com/cgspeed/motion-capture/cmu-bvh-conversion))



- Unzip and move folders 13, 14, 15, and 86 to directory `logs/cmu_files/raw/`

- Run `standardize_bvh.py` to apply consistent header to each file and keep only one in every ten frames. (saved as .bvh in `logs/cmu_files/standardized/`)

- Run the following to save the 3d coordinates for each frame of each corresponding animation. Blender runs the animations defined in the bvh files in the background to determine the 3d coordinates to save:
    - `blender --background --python blender/save_blender_3d_points.py` #Original training and testing data
    - `blender --background --python blender/save_blender_mirrored.py` #Bilateral mirror of Subject 86 for augmentation
    - `blender logs/blender_animations/seated_animation.blend --background --python save_seated.py` #Animation of seated poses for augmentation
    (saved as pickle dictionary in `logs/blender_dicts/`)

## Reference

	  @InProceedings{Zhao_2017,
	  author = {Ruiqi Zhao, Yan Wang, and Aleix M Martines},
	  title = {A Simple, Fast, and Highly-Accurate Algorithm to Recover 3D Shape from 2D Landmarks on a Single Image},
	  booktitle = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
	  month = {November},
	  year = {2017}
	  }
