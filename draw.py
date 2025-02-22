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
def draw(DH, deg=False, arrows=False):
    # Convert to floats if not already
    DH = DH / 1.0
    # Convert to radians if not already
    if deg == True:
        DH[:, 2:] = (np.pi/180)*DH[:, 2:]
    # Calculate 0Ri and ri
    R = calc_R.calc_R(DH)
    r = forward_kinematics.forward_kinematics(DH, R)
    # Set plotting style preferences
    plt.style.use('seaborn-v0_8-ticks')
    ax = plt.figure().add_subplot(projection='3d')
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.zaxis.set_ticks_position('none')
    plt.figtext(0.18, 0.05, 'x', color='r', fontweight='bold')
    plt.figtext(0.195, 0.05, 'y', color='g', fontweight='bold')
    plt.figtext(0.21, 0.05, 'z', color='b', fontweight='bold')
    plt.figtext(0.05, 0.05, 'Axis Colors:', fontweight='bold')
    # Plot joint locations
    ax.plot(r[0], r[1], r[2], 'k')
    ax.axis('equal')
    # Plot coordinate frames
    num_joints = np.shape(DH)[0]
    if arrows == True:
        # Plot global coordinate frame
        ax.quiver(r[0, 0], r[1, 0], r[2, 0], 1, 0, 0, color='r', linewidth=3)
        ax.quiver(r[0, 0], r[1, 0], r[2, 0], 0, 1, 0, color='g', linewidth=3)
        ax.quiver(r[0, 0], r[1, 0], r[2, 0], 0, 0, 1, color='b', linewidth=3)
        # Plot joint coordinate frames
        for i in range(1, num_joints+1):
            # Calculate local coordinate fram from rotation matrix
            x = R[i-1] @ np.array([[1], [0], [0]])
            y = R[i-1] @ np.array([[0], [1], [0]])
            z = R[i-1] @ np.array([[0], [0], [1]])
            # Plot local coordinate frame
            ax.quiver(r[0, i], r[1, i], r[2, i], x[0, 0], x[1, 0], x[2, 0], color='r', linewidth=3)
            ax.quiver(r[0, i], r[1, i], r[2, i], y[0, 0], y[1, 0], y[2, 0], color='g', linewidth=3)
            ax.quiver(r[0, i], r[1, i], r[2, i], z[0, 0], z[1, 0], z[2, 0], color='b', linewidth=3)
    else:
        # Plot global coordinate frame
        ax.plot([r[0, 0], r[0, 0] + 1], [r[1, 0], r[1, 0]], [r[2, 0], r[2, 0]], 'r', linewidth=3)
        ax.plot([r[0, 0], r[0, 0]], [r[1, 0], r[1, 0] + 1], [r[2, 0], r[2, 0]], 'g', linewidth=3)
        ax.plot([r[0, 0], r[0, 0]], [r[1, 0], r[1, 0]], [r[2, 0], r[2, 0] + 1], 'b', linewidth=3)
        # Plot joint coordinate frames
        for i in range(1, num_joints+1):
            # Calculate local coordinate fram from rotation matrix
            x = R[i-1] @ np.array([[1], [0], [0]])
            y = R[i-1] @ np.array([[0], [1], [0]])
            z = R[i-1] @ np.array([[0], [0], [1]])
            # Plot local coordinate frame
            ax.plot([r[0, i], r[0, i] + x[0, 0]], [r[1, i], r[1, i] + x[1, 0]], [r[2, i], r[2, i] + x[2, 0]], 'r', linewidth=3)
            ax.plot([r[0, i], r[0, i] + y[0, 0]], [r[1, i], r[1, i] + y[1, 0]], [r[2, i], r[2, i] + y[2, 0]], 'g', linewidth=3)
            ax.plot([r[0, i], r[0, i] + z[0, 0]], [r[1, i], r[1, i] + z[1, 0]], [r[2, i], r[2, i] + z[2, 0]], 'b', linewidth=3)
    