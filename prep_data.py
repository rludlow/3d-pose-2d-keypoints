import numpy as np
import pickle
import datetime
import preprocessing as pre

# Get starting time
start = datetime.datetime.now()
time = start.strftime("%d-%H-%M")


def prep_data(subject_num, train=False, duplicates=720, norm_mode='frame', distort=False):
    """ Accepts dictionary of file names (keys) and 3d coordinates (values) then performs all preprocessing to output a numpy array ready for training or testing."""
    # Load dictionary of 3d coordinates of action sequences exported from Blender
    blender_file = 'logs/blender_dicts/Subject{}.p'.format(subject_num)
    bvh_logs = pickle.load( open( blender_file, "rb" ) )

    # Merge the arrays from each each action sequence per CMU subject into one numpy array
    merged = pre.merge_arrays(bvh_logs, rows=15)
    print("merged", merged.shape)
    merged = merged[:,0:15,:]

    # Normalize the data to eliminate effects of translation and scale
    normalized = pre.normalize_data(merged, norm_mode)
    print("normalized", normalized.shape)

    # Augment data set with synthetic rotations if prepping for training
    if train == True:
        augmented = pre.augment_rotations(normalized, duplicates)
        final = augmented
        print("augmented", augmented.shape)
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
    prep_data('86', train=True, duplicates=720, norm_mode='frame')
    prep_data('86', train=True, duplicates=720, norm_mode='sequence')

    # Augmented Training sets
    prep_data('86-seated', train=True, duplicates=720, norm_mode='sequence')
    prep_data('86-mirror', train=True, duplicates=720, norm_mode='sequence')
