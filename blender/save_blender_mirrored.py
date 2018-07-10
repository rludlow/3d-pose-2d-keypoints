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

pairs = [["RightArm", "LeftArm"], ["RightForeArm", "LeftForeArm"], ["RightUpLeg", "LeftUpLeg"], ["RightLeg", "LeftLeg"], ["LeftShoulder", "RightShoulder"]]

twist = ["LowerBack", "Spine",  "Neck", "Neck1", "Head"]

def bilateral():
    for j in range(0,max_frames):
        bpy.context.scene.frame_set(j)
        for combo in pairs:
            mirror.pose.bones[combo[0]].rotation_euler[0] = main.pose.bones[combo[1]].rotation_euler[0]
            mirror.pose.bones[combo[0]].rotation_euler[1] = main.pose.bones[combo[1]].rotation_euler[1] * -1
            mirror.pose.bones[combo[0]].rotation_euler[2] = main.pose.bones[combo[1]].rotation_euler[2] * -1
            mirror.pose.bones[combo[1]].rotation_euler[0] = main.pose.bones[combo[0]].rotation_euler[0]
            mirror.pose.bones[combo[1]].rotation_euler[1] = main.pose.bones[combo[0]].rotation_euler[1] * -1
            mirror.pose.bones[combo[1]].rotation_euler[2] = main.pose.bones[combo[0]].rotation_euler[2] * -1
            mirror.pose.bones[combo[0]].keyframe_insert(data_path = 'rotation_euler', frame=j)
            mirror.pose.bones[combo[1]].keyframe_insert(data_path = 'rotation_euler', frame=j)

        for joint in twist:
            mirror.pose.bones[joint].rotation_euler[1] = main.pose.bones[joint].rotation_euler[1] * -1
            mirror.pose.bones[joint].rotation_euler[2] = main.pose.bones[joint].rotation_euler[2] * -1
            mirror.pose.bones[joint].keyframe_insert(data_path = 'rotation_euler', frame=j)

def get_3d_points(armature):
    points = []
    for j in range(15):
        bone = armature.pose.bones[keras_joints[j]]
        t = bone.tail
        x, y, z = t[0], t[2], -t[1] # Note different than axis in blender
        part = [x,y,z]
        points.append(part)
    return points


if __name__ == "__main__":

    bvh_subjects = [86]

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
            bpy.context.object.name = "main"
            main = bpy.data.objects['main']
            bpy.ops.object.mode_set(mode='POSE')
            bpy.ops.import_anim.bvh(filepath=import_path)
            bpy.context.object.name = "mirror"
            mirror= bpy.data.objects['mirror']
            bpy.ops.object.mode_set(mode='POSE')

            max_frames = max_keyframes()
            bvh_dict[file] = []



            bilateral()
            #rotate_joints()

            # Record 3d points for franes
            for j in range(0,max_frames):
                bpy.context.scene.frame_set(j)

                #frame_main = get_3d_points(main)
                frame_mirror = get_3d_points(mirror)

                #bvh_dict[file].append(frame_main)
                bvh_dict[file].append(frame_mirror)

            # Delete current bvh before looping back
            main.select = True
            mirror.select = True

            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.delete()

            # Save
            SAVE_PATH = '../logs/blender_dicts/'
            LOG_FILE = 'Subject{}-mirrortest.p'.format(subject)
            CSV_LOG_PATH = SAVE_PATH + LOG_FILE

            pickle.dump( bvh_dict, open(CSV_LOG_PATH, "wb" ) )
