import numpy as np
from scipy import spatial
import datetime

# Get starting time
start = datetime.datetime.now()
time = start.strftime("%m-%d-%H-%M-%S")

import models

model_dict = {
    'base': models.base(),
    'dropout': models.dropout(),
    'multi': models.multi(),
}

import keras
from keras import backend as K

def euc_dist_keras(y_true, y_pred):
    """Loss function to be used in training."""
    return K.sqrt(K.sum(K.square(y_true - y_pred), axis=-1, keepdims=True))

from keras.models import Model
from keras.layers import Dense, Activation, Dropout, Input
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint
from keras.models import model_from_json
from keras.layers.merge import Concatenate, Add

def train_network(norm_mode, model_name, augment=False):
    # Get training data
    file = 'logs/train_test/Subject86train{}.npy'.format(norm_mode)
    data = np.load(file)
    print(data.shape)
    if augment:
        # Concatenate each dataset from list to original
        for entry in augment:
            print(entry)
            augmented_file = 'logs/train_test/Subject86{}.npy'.format(entry)
            augmented_data = np.load(augmented_file)
            data = np.concatenate((data, augmented_data))
            print(data.shape)
        augment = "-".join(augment) # more convenient name to add to weight file name

    # Shuffle
    np.random.seed(30)
    np.random.shuffle(data)

    # Split into inputs and targets
    y_train = data[:,:,2]
    X_data = data[:,:,0:2]
    X_train = X_data.reshape(X_data.shape[0], X_data.shape[1] *  X_data.shape[2])

    # Training parameters
    BATCH_SIZE = 1024
    PATIENCE = 10
    SHUFFLE = True

    # Save weights with best validation loss
    checkpointer = ModelCheckpoint(filepath='logs/weights/{0}-{1}-{2}-{3}.hdf5'.format(norm_mode, model_name, augment, time), verbose=1, save_best_only=True)

    # Stop training if validation doesnt improve for designated number of epochs
    early_stop=keras.callbacks.EarlyStopping(monitor='val_loss', patience=PATIENCE, verbose=0, mode='auto')

    # Compile and train
    model = model_dict[model_name]
    model.compile(loss=euc_dist_keras, optimizer='rmsprop')
    model.fit(X_train, y_train, nb_epoch=200, validation_split=0.2, shuffle=SHUFFLE, batch_size=BATCH_SIZE,callbacks=[checkpointer, early_stop],  verbose=1)

if __name__ == "__main__":

    settings = [
    # (normalization mode, network, optional augmented data)
    ('frame', 'base'),
    ('sequence', 'base'),
    ('frame', 'dropout'),
    ('sequence', 'dropout'),
    ('frame', 'multi'),
    ('sequence', 'multi'),
    ('sequence', 'multi', ['seated']),
    ('sequence', 'multi', ['-seated-short'])
    ('sequence', 'multi', ['mirror']),
    ('sequence', 'multi', ['seated', 'mirror']),
    ]

    for run in settings:
        train_network(*run)
