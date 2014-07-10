# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# 3D Rotation of a Point Cloud

# <codecell>

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from IPython.html.widgets import interact
from IPython.html import widgets
import pandas as pd

# <codecell>

%matplotlib inline
np.set_printoptions(suppress=True, precision=3) # to avoid 1e-17 expressions in rotation matrix

# <headingcell level=2>

# Read Point Cloud Library File

# <markdowncell>

# Following Scene was generated with [BlenSor](http://www.blensor.org/) and a [Point Cloud Library](http://pointclouds.org/) File (*.pcd) was exported.
# 
# ![Scene](Pointcloud00002.png)

# <codecell>

pc = pd.read_csv('Pointcloud00002.pcd', names=['x','y','z','rgb'], skiprows=11, sep=' ')
pc=pc[['x','y','z']]
pc.head(3)

# <headingcell level=3>

# Quick Look

# <codecell>

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(pc.x.values, pc.y.values, pc.z.values)
plt.xlabel('x');
plt.ylabel('y');

# <markdowncell>

# Look's like it is in local sensor coordinate system. If we rotate the point cloud like the scanner was rotated, we might get the correct obstacle.

# <headingcell level=2>

# Now let's Rotate it

# <markdowncell>

# Z-Y-X-Konvention

# <codecell>

def Rypr(y, p, r):
    '''
    Rotationsmatrix für y=yaw, p=pitch, r=roll in degrees
    '''
    # from Degree to Radians
    y = y*np.pi/180.0
    p = p*np.pi/180.0
    r = r*np.pi/180.0
    
    Rr = np.matrix([[1.0, 0.0, 0.0],[0.0, np.cos(r), -np.sin(r)],[0.0, np.sin(r), np.cos(r)]])
    Rp = np.matrix([[np.cos(p), 0.0, np.sin(p)],[0.0, 1.0, 0.0],[-np.sin(p), 0.0, np.cos(p)]])
    Ry = np.matrix([[np.cos(y), -np.sin(y), 0.0],[np.sin(y), np.cos(y), 0.0],[0.0, 0.0, 1.0]])
    
    return Ry*Rp*Rr

# <markdowncell>

# You need to download the IPython Notebook and run it locally, to enable interactivity

# <codecell>

@interact
def plotrot3Dpersp(gieren = widgets.FloatSliderWidget(min=-180.0, max=180.0, step=1.0, value=-120.0, description=""), \
                   nicken = widgets.FloatSliderWidget(min=-180.0, max=180.0, step=1.0, value=0.0, description=""), \
                   wanken = widgets.FloatSliderWidget(min=-180.0, max=180.0, step=1.0, value=60.0, description=""), \
                   kippen = widgets.FloatSliderWidget(min=0.0, max=90.0, step=1.0, value=2.0, description=""), \
                   rotieren = widgets.FloatSliderWidget(min=-180.0, max=180.0, step=1.0, value=100.0, description="")):
    
    R = Rypr(gieren, nicken, wanken)
    print('%s' % R)

    x, y, z = R * np.array([pc.values]).T
    
    fig = plt.figure(figsize=(14,6))
    ax = Axes3D(fig)
    ax.scatter(x.tolist(), y.tolist(), z.tolist())
    ax.axis('equal')
    ax.set_zlim3d(-6.0, 1.0)
    plt.xlabel('x');
    plt.ylabel('y');
    plt.title('\nG: %i, N: %i, W: %i' % (gieren, nicken, wanken))
    ax.view_init(kippen, rotieren)

# <codecell>

print('Nice!')

