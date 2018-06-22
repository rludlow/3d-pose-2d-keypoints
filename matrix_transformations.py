import numpy as np


# Translation Matrix

def translation_vector_to_matrix(t): # t = 3d point
    """
    Generate translation matrix from 1x3 translation vector
    """
    return np.array([
        [1,0,0,t[0]],
        [0,1,0,t[1]],
        [0,0,1,t[2]],
        [0,0,0,1]
    ])

# Rotation Matrices

def cos(a):
    """
    Convenience function, return cosine from angle in degrees
    """
    return np.cos(np.radians(a))

def sin(a):
    """
    Convenience function, return sine from angle in degrees
    """
    return np.sin(np.radians(a))

def X_mat(a):
    """
    Matrix for rotation of angle a around x axis
    """
    return np.array([
        [1,0,0],
        [0,cos(a),-sin(a)],
        [0,sin(a),cos(a)],
    ])

def Y_mat(b):
    """
    Matrix for rotation of angle b around y axis
    """
    return np.array([
        [cos(b),0, sin(b)],
        [0,1,0],
        [-sin(b),0,cos(b)],
    ])

def Z_mat(c):
    """
    Matrix for rotation of angle c around z axis
    """
    return np.array([
        [cos(c),-sin(c),0],
        [sin(c),cos(c),0],
        [0,0,1],
    ])

def rot_mat(a, b, c):
    """
    Combined rotation matrix for rotation around all three axis
    """
    XY = X_mat(a).dot(Y_mat(b))
    XYZ = XY.dot(Z_mat(c))
    return XYZ

def rot_mat4(a, b, c):
    return matrix_3d_to_4d(rot_mat(a, b, c))

def matrix_3d_to_4d(M):
    B = np.array(np.identity(4))
    B[:-1,:-1] = M
    return B

# Combined rotation and translation
def External_M(cam,a,b,c):
    t = [0,0,-cam]
    T = T_mat4(t)
    R = rot_mat4(a,b,c)
    RT = T.dot(R)
    return RT
