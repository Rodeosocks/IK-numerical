# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:32:29 2025

@author: greav
"""

import numpy as np
import matplotlib.pyplot as plt

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
    R = calc_R(DH)
    r = forward_kinematics(DH, R)
    ax = plt.figure().add_subplot(projection='3d')
    ax.axis('equal')
    ax.plot(r[0], r[1], r[2])
    
# Calculate absolute rotation matricies from DH parameters
def calc_R(DH, deg=False):
    # Convert to floats if not already
    DH = DH / 1.0
    # Convert to radians if not already
    if deg == True:
        DH[:, 2:] = (np.pi/180)*DH[:, 2:]
    # Initialize helpful variables
    num_joints = np.shape(DH)[0]
    R = np.zeros((num_joints, 3, 3))
    theta = DH[:, 3]
    alpha = DH[:, 2]
    # Calculate (i-1)R(i)
    for i in range(num_joints):
        R[i] = np.array([[np.cos(theta[i]), -np.sin(theta[i])*np.cos(alpha[i]), np.sin(theta[i])*np.sin(alpha[i])], 
                         [np.sin(theta[i]), np.cos(theta[i])*np.cos(alpha[i]), -np.cos(theta[i])*np.sin(alpha[i])], 
                          [0, np.sin(alpha[i]), np.cos(alpha[i])]])
    # Calculate 0R(i)
    for i in range(1, num_joints):
        R[i] = R[i-1] @ R[i]
    return R

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
    
######## TESTING
DH_test = np.array([[1, 1, 0, 90],
               [1, 1, 0, 90]])

draw(DH_test, True)