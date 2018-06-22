import bpy
import numpy as np
import datetime
import pickle

import os

# Get starting time
currentDT = datetime.datetime.now()
time = currentDT.strftime("%m-%d-%H-%M-%S")

keras_joints = {
    0: "Head",
    1: "Spine",
    2: "RightShoulder",
    3: "RightArm",
    4: "RightForeArm",
    5: "LeftShoulder",
    6: "LeftArm",
    7: "LeftForeArm",
    8: "RHipJoint",
    9: "RightUpLeg",
    10: "RightLeg",
    11: "LHipJoint",
    12: "LeftUpLeg",
    13: "LeftLeg",
    14: "Hips", #root joint
    }

def max_keyframes():
    '''Total animated keyframes for active object'''
    a = np.array(bpy.context.object.animation_data.action.fcurves) ##Correct object
    frames = len(a[0].keyframe_points)
    return frames

'''
def get_3d_points(frame):
    Return 3d coordinates of each joint
    points = []

    return points
'''

if __name__ == "__main__":

    bvh_subjects = [13,14,15,86]

    for subject in bvh_subjects:

        # Retrieve list of bvh files for given subject
        file_list = []
        bvh_directory = 'logs/cmu_files/standardized/{}/'.format(subject)

        for root, dirs, files in os.walk(bvh_directory):
            file_list.extend(files)

        bvh_dict = {}

        for file in file_list:

            # Import bvh file into blender
            import_path = bvh_directory + file
            bpy.ops.import_anim.bvh(filepath=import_path)
            bpy.ops.object.mode_set(mode='POSE')

            max_frames = max_keyframes()
            bvh_dict[file] = []

            # Record 3d points for franes
            for i in range(0,max_frames):
                bpy.context.scene.frame_set(i)

                frame = []
                for j in range(15):
                    bone = bpy.context.object.pose.bones[keras_joints[j]]
                    t = bone.tail
                    x, y, z = t[0], t[2], -t[1] # Note different than axis in blender
                    part = [x,y,z]
                    frame.append(part)
                #frame = get_3d_points(j)
                bvh_dict[file].append(frame)

            # Delete current bvh before looping back
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.delete()

        # Save
        SAVE_PATH = 'logs/blender_dicts/'
        LOG_FILE = 'Subject{}.p'.format(subject)
        CSV_LOG_PATH = SAVE_PATH + LOG_FILE

        pickle.dump( bvh_dict, open(CSV_LOG_PATH, "wb" ) )
