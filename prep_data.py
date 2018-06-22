import numpy as np
import pickle
import datetime
from preprocessing import *

# Get starting time
start = datetime.datetime.now()
time = start.strftime("%d-%H-%M")


def prep_data(subject_num, train=False, duplicates=720, norm_mode='frame', distort=False):

    # Load dictionary of 3d coordinates of action sequences exported from Blender
    blender_file = 'logs/blender_dicts/Subject{}.p'.format(subject_num)
    bvh_logs = pickle.load( open( blender_file, "rb" ) )

    # Merge the arrays from each each action sequence per CMU subject into one numpy array
    merged = merge_arrays(bvh_logs, rows=15)
    print("merged", merged.shape)
    merged = merged[:,0:15,:]

    # Normalize the data to eliminate effects of translation and scale
    normalized = normalize_data(merged, norm_mode)
    print("normalized", normalized.shape)

    # Augment data set with synthetic rotations if prepping for training
    if train == True:
        augmented = augment_rotations(normalized, duplicates)
        final = augmented
        print("augmented", augmented.shape)
        if distort == True:
            # Distort x,y coordinates by Gaussian
            distorted = distort_x_y(augmented)
            final = distorted
        train_test = 'train'

    else:
        final = normalized
        train_test = 'test'

    save_dir = 'logs/train_test/'
    save_name = 'Subject' + str(subject_num) + train_test + norm_mode
    save_file = save_dir + save_name

    np.save(save_file, final)

if __name__ == "__main__":

    # Test sets
    for subject in ['13','14','15']:
        prep_data(subject, train=False, norm_mode='frame')
        prep_data(subject, train=False, norm_mode='sequence')

    # Original training sets
    prep_data('86', train=True, duplicates=720, norm_mode='frame', distort=True)
    prep_data('86', train=True, duplicates=720, norm_mode='sequence', distort=True)

    # Augmented Training sets
    prep_data('86-seated', train=True, duplicates=720, norm_mode='sequence', distort=True)
    prep_data('86-mirror', train=True, duplicates=720, norm_mode='sequence', distort=True)
