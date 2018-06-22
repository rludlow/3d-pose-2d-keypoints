def rotation_matrix(a_degrees, b_degrees, c_degrees):
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
