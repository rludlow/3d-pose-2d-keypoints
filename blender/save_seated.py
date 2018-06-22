import bpy
import numpy as np
import datetime
import pickle

import os

# Get starting time
currentDT = datetime.datetime.now()
time = currentDT.strftime("%m-%d-%H-%M-%S")

bpy.context.scene.layers[0] = True
bpy.data.objects['sit_man'].select = True
bpy.context.scene.objects.active = bpy.data.objects['sit_man']

def max_keyframes():
    a = np.array(bpy.context.object.animation_data.action.fcurves) ##Correct object
    frames = len(a[0].keyframe_points)
    return frames

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

bvh_dict = {}
file = 'riggy'

bpy.ops.object.mode_set(mode='POSE')

max_frames = max_keyframes()
bvh_dict[file] = []

for j in range(0,950):
    if j%1 == 0:
        bpy.context.scene.frame_set(j)
        frame = []
        for j in range(15):
            bone = bpy.context.object.pose.bones[keras_joints[j]]
            t = bone.tail
            x, y, z = t[0], t[2], -t[1] # Note different than axis in blender
            part = [x,y,z]
            frame.append(part)
        bvh_dict[file].append(frame)

SAVE_PATH = '../logs/blender_dicts/'
LOG_FILE = 'Subject86-seated-short.p'
CSV_LOG_PATH = SAVE_PATH + LOG_FILE

pickle.dump( bvh_dict, open(CSV_LOG_PATH, "wb" ) )
