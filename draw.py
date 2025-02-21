# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:32:29 2025

@author: greav
"""

import numpy as np
import matplotlib.pyplot as plt
import calc_R
import forward_kinematics

# Given a system's DH parameters, plot the orientation
# DH params must be in the order d, a, alpha, theta
# DH params should be in a 2d numpy array, each row being a joint
# alpha and theta should be in radians, unless specified
def draw(DH, deg=False):
    # Convert to floats if not already
    DH = DH / 1.0
    # Convert to radians if not already
    if deg == True:
        DH[:, 2:] = (np.pi/180)*DH[:, 2:]
    # Calculate 0Ri and ri
    R = calc_R.calc_R(DH)
    r = forward_kinematics.forward_kinematics(DH, R)
    # Plot joint locations
    plt.style.use('seaborn-v0_8-ticks')
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(r[0], r[1], r[2], 'k')
    ax.axis('equal')
    # Plot global coordinate frame
    num_joints = np.shape(DH)[0]
    ax.plot([r[0, 0], r[0, 0] + 1], [r[1, 0], r[1, 0]], [r[2, 0], r[2, 0]], 'r', linewidth=5)
    ax.plot([r[0, 0], r[0, 0]], [r[1, 0], r[1, 0] + 1], [r[2, 0], r[2, 0]], 'g', linewidth=5)
    ax.plot([r[0, 0], r[0, 0]], [r[1, 0], r[1, 0]], [r[2, 0], r[2, 0] + 1], 'b', linewidth=5)
    # Plot joint coordinate frame
    for i in range(1, num_joints+1):
        # Calculate local coordinate fram from rotation matrix
        x = R[i-1] @ np.array([[1], [0], [0]])
        y = R[i-1] @ np.array([[0], [1], [0]])
        z = R[i-1] @ np.array([[0], [0], [1]])
        # Plot local coordinate frame
        ax.plot([r[0, i], r[0, i] + x[0, 0]], [r[1, i], r[1, i] + x[1, 0]], [r[2, i], r[2, i] + x[2, 0]], 'r', linewidth=5)
        ax.plot([r[0, i], r[0, i] + y[0, 0]], [r[1, i], r[1, i] + y[1, 0]], [r[2, i], r[2, i] + y[2, 0]], 'g', linewidth=5)
        ax.plot([r[0, i], r[0, i] + z[0, 0]], [r[1, i], r[1, i] + z[1, 0]], [r[2, i], r[2, i] + z[2, 0]], 'b', linewidth=5)