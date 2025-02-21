# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:38:35 2025

@author: greav
"""

import numpy as np

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