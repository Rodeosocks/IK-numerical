# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:28:30 2025

@author: greav
"""

import numpy as np
import draw
import matplotlib.pyplot as plt

DH = np.array([[10, 0, -90, 0], 
               [2, 10, 0, 0], 
               [0, 5, 90, 0]])
plt.close('all')
draw.draw(DH, deg=True)