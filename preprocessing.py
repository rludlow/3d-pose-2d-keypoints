import numpy as np

def normalize_data(data, mode):
    """
    Calculate mean for x, y (and z if present), and standard deviation for x and y in given frame,. Subtract respective mean from each point, then divide by avg of std of x and y.
    """

    if mode == 'frame':
        for num, frame in enumerate(data):
            denom = (frame[:,0].std() + frame[:,1].std()) / 2
            if denom == 0:
                print(num, denom)

            if frame.shape[1] == 3:
                means = [frame[:,0].mean(), frame[:,1].mean(),frame[:,2].mean()]
            elif frame.shape[1] == 2:
                means = [frame[:,0].mean(), frame[:,1].mean()]
            else:
                print('We have the wrong data')
            frame -= means
            frame /= denom
        return data

    elif mode == 'sequence':
        print(data.shape)


        denom = data[0,:,1].std()
        # Note - we are hard-coding in the known std(y) for the subject in a T-pose just for this data set
        denom = 8.132629175342606

        for num, frame in enumerate(data):
            if denom == 0:
                print(num, denom)

            if frame.shape[1] == 3:
                means = [frame[:,0].mean(), frame[:,1].mean(),frame[:,2].mean()]
            elif frame.shape[1] == 2:
                means = [frame[:,0].mean(), frame[:,1].mean()]
            else:
                print('We have the wrong data')
            frame -= means
            frame /= denom

        return data

    else:
        print("Error - must include a valid processing mode.")


def distort_x_y(data):
    """
    Randomly distort 2d points so model can train on inperfect inputs.
    """

    for frame in data:
        for point in frame:
            x_rand = np.random.normal(0, .05) + 1
            y_rand = np.random.normal(0, .05) + 1
            point[0] *= x_rand
            point[1] *= y_rand

        return data

def augment_rotations(data, duplicates=720):
    """
    Generate defined number of augmented points by rotating the 3d coordinates.
    """

    a_range = [-20, 20] # a - rotation around x-axis (camera pointing down or up)
    #b_range = [0,360] #b - rotation around y-axis (camera moving around subject)
    c_range = [-20,20] #c - rotation around z-axis (camera tilted)

    #a_range = [a_range[0] * np.random.normal(0, .2) + 1, a_range[1] * np.random.normal(0, .2) + 1]
    #c_range = [a_range[0] * np.random.normal(0, .2) + 1, a_range[1] * np.random.normal(0, .2) + 1]
    variants = np.zeros((duplicates, data.shape[0], data.shape[1], data.shape[2]))

    a  = a_range[0]
    b = 0
    c = a_range[0]
    for i in range(duplicates):
        #print("rotation", i)
        a += (a_range[1] - a_range[0]) / duplicates
        b += 1
        c += (c_range[1] - c_range[0]) / duplicates
        R = rotation_matrix(a,b,c)
        for j in range(data.shape[0]):
            variants[i][j] = R.dot(data[j].T).T
    full = variants.reshape((variants.shape[0] * variants.shape[1], variants.shape[2], variants.shape[3]))
    data = np.concatenate((data,full))


    return data

def hip_relative(data):
    """
    Return all joint coordinates as relative to the hip joint.
    """
    for frame in data:
        frame -= frame[14]
    return data

def merge_arrays(dict, rows=15):
    """
    Take dictionary of arrays and merge into single array.
    """
    merged_logs = np.zeros((1,rows,3))
    for key, value in dict.items():
        #value = np.array(value)
        #print(value.shape)
        merged_logs = np.concatenate((merged_logs,value))

    final = merged_logs[1:]

    return final

def rotation_matrix(a_degrees, b_degrees, c_degrees):
    """
    Accepts rotations about each axis in degrees, returns rotation matrix.
    """

    a = np.radians(a_degrees)
    b = np.radians(b_degrees)
    c = np.radians(c_degrees)

    X_mat = np.array([
        [1,0,0],
        [0,np.cos(a),-np.sin(a)],
        [0,np.sin(a),np.cos(a)]
        ])

    Y_mat = np.array([
        [np.cos(b),0, np.sin(b)],
        [0,1,0],
        [-np.sin(b),0,np.cos(b)],
    ])

    Z_mat = np.array([
        [np.cos(c),-np.sin(c),0],
        [np.sin(c),np.cos(c),0],
        [0,0,1],
    ])

    XY = X_mat(a).dot(Y_mat(b))
    XYZ = XY.dot(Z_mat(c))
    return XYZ
