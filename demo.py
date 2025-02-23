# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:28:30 2025

@author: greav
"""

import draw
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk

DH = [[10, 0, -90, 0], 
      [2, 10, 0, 0], 
      [0, 5, 90, 0]]
plt.close('all')
plt.ioff()
fig = plt.figure()

root = tk.Tk()
root.wm_title("IK-numerical")
draw.draw(DH, deg=True, fig=fig)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

# pack_toolbar=False # will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()
entry = tk.Entry(root)

# toolbar.pack(side=tk.BOTTOM, fill=tk.X)
entry.pack()
toolbar.pack()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

root.mainloop()
