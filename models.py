import keras
from keras.models import Model
from keras.layers import Dense, Activation, Dropout, Input
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint
from keras.models import model_from_json
from keras.layers.merge import Concatenate, Add

def base():
    input1 = Input(shape=(30,))

    x = Dense(30)(input1)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    final = Activation("tanh")(x)


    model = Model(inputs=input1,outputs=final)
    return model


# SIMPLE DROPOUT

def dropout():
    input1 = Input(shape=(30,))

    x = Dense(30)(input1)
    x = Activation("tanh")(x)
    x = Dropout(0.3)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.2)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.2)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    final = Activation("tanh")(x)


    model = Model(inputs=input1,outputs=final)
    return model

# SIMPLE DROPOUT VARIANT

def dropout2():
    input1 = Input(shape=(30,))

    x = Dense(30)(input1)
    x = Activation("tanh")(x)
    x = Dropout(0.2)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.2)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    final = Activation("tanh")(x)

    model = Model(inputs=input1,outputs=final)
    return model


# MULTI-STAGE MODEL

def multi():
    input1 = Input(shape=(30,))

    x = Dense(30)(input1)
    x = Activation("tanh")(x)
    x = Dropout(0.20)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.20)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    final = Activation("tanh")(x)

    model = Model(inputs=input1,outputs=final)
    return model

# MULTI-STAGE MODEL, 5 + 1 stages, more layers in stages

def multi_long():
    input1 = Input(shape=(30,))

    x = Dense(30)(input1)
    x = Activation("tanh")(x)
    x = Dropout(0.20)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Dropout(0.20)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    final = Activation("tanh")(x)

    model = Model(inputs=input1,outputs=final)
    return model

# MULTI-STAGE MODEL, 2 + 1 stages

def multi_short():
    input1 = Input(shape=(30,))

    x = Dense(30)(input1)
    x = Activation("tanh")(x)
    x = Dropout(0.20)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Dropout(0.20)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    final = Activation("tanh")(x)

    model = Model(inputs=input1,outputs=final)
    return model

# MULTI-STAGE MODEL, MAINTAIN 45 NODES FURTHER

def multi45():
    input1 = Input(shape=(30,))

    x = Dense(30)(input1)
    x = Activation("tanh")(x)
    x = Dropout(0.20)(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Dropout(0.20)(x)
    x = Activation("tanh")(x)
    x = Dense(30)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    x = Activation("tanh")(x)

    x = Concatenate()([input1, x])
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dropout(0.10)(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(45)(x)
    x = Activation("tanh")(x)
    x = Dense(15)(x)
    final = Activation("tanh")(x)

    model = Model(inputs=input1,outputs=final)
    return model
