# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:38:41 2025

@author: greav
"""

import numpy as np

# Calculates the absolute position of each joint, with each joint being a column of [[x], [y], [z]] coordinates in r
def forward_kinematics(DH, R, deg=False):
    # Convert to floats if not already
    DH = DH / 1.0
    # Convert to radians if not already
    if deg == True:
        DH[:, 2:] = (np.pi/180)*DH[:, 2:]
    # Initialize helpful variables
    num_joints = np.shape(DH)[0]
    r = np.zeros((num_joints+1, 3))
    d = DH[:, 0]
    a = DH[:, 1]
    # Calculate x, y, and z positions of each joint
    r[1] = np.transpose(d[0] * np.array([[0], [0], [1]]) + a[0] * (R[0] @ np.array([[1], [0], [0]])))
    for i in range(1, num_joints):
        r[i+1] = r[i] + np.transpose(d[i] * (R[i-1] @ np.array([[0], [0], [1]])) + a[i] * (R[i] @ np.array([[1], [0], [0]])))
    return np.transpose(r)