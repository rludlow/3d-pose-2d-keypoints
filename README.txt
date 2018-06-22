
SOFTWARE AND LIBRARIES USED
Blender (https://www.blender.org/download/) - only needed if you want to replicate the process of exporting from raw files to 3d coordinates.
Keras, Tensorflow and common computational Python libraries - Numpy, Pandas, Matplotlib, Scipy, Pickle, Datetime.

USING THIS SOFTWARE

The steps below show how to replicate the end-to-end process. Note that all files are already included EXCEPT the train_test files created in step B1, due to size. Although the file outputs are large, running step B1 should take only a couple of minutes.

If you want to start with 3d coordinates that are ready to pre-process and train, skip to Section B.

Otherwise, you can replicate the preliminary data prep in Section A. Step A4 requires having blender (https://www.blender.org/download/) installed, and assumes you established 'blender' as a shortcut to run the program from the command line, as is common convention.

A. Download Source Data and Process in Blender

  1. Download bvh files (main site: https://sites.google.com/a/cgspeed.com/cgspeed/motion-capture/cmu-bvh-conversion)

      Download locations:
        http://www.mediafire.com/?z6pr5bk3h1o5045
        http://www.mediafire.com/?cu0a99w1day8hnr
        http://www.mediafire.com/?r6y8sc60mabhneu

  2. Unzip and move folders 13, 14, 15, and 86 to directory 'logs/cmu_files/raw/'

  3. Run standardize_bvh.py to apply consistent header to each file and keep only one in every ten frames. (saved as .bvh in cmu_files/standardized/)

  4. Run the following to save the 3d coordinates for each frame of each corresponding animation. Blender runs the animations defined in the bvh files in the background to determine the 3d coordinates to save:
    blender --background --python save_blender_3d_points.py #Original training and testing data
    blender --background --python save_blender_mirrored.py #Bilateral mirror of Subject 86 for augmentation
    blender logs/seated_animation.blend --background --python save_seated.py #Animation of seated poses for augmentation
    (saved as pickle dictionary in logs/blender_dicts/)
    Note: A datetime is appended to these files. To use these in the subsequent step, archive the existing files and remove the datetime suffix.

B. Preprocess and Train

  1. Run prep_data.py to preprocess the testing and training data (saved as .npy logs/train_test/ ). Notes:
      The output files for Subject86 and Subject86-mirror are ~3GB each, Subject86-seated is 600MB, and the others are substantially smaller.

  2. Run train.py to train models with each of the defined parameters (weights saved in logs/weights)
      A datetime is appended to these files. To use these in the subsequent step, archive the existing files and remove the datetime suffix of your new files.

C. Testing

Test results can be seen in model_analysis.ipynb. This notebook is not formatted with the intent of presenting the data, but the results can be seen there. Note that if you want to run it with weights you generated, you should remove the datetime from the weight file name.
