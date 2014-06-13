# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# <codecell>

%pylab inline --no-import-all

# <headingcell level=1>

# Drehung nach Z, Y', X'' Konvention

# <markdowncell>

# In der Fahrzeugtechnik (Luftfahrt: DIN 9300; Automobilbau : DIN 70000; Schifffahrt) ist die (z,y',x'')-Konvention gebräuchlich. In den Normen sind die Verwendung der Formelzeichen $\Psi$, $\Theta$ und $\Phi$ und die Namen Gier-, Nick- und Roll-Winkel (engl. yaw, pitch and roll angle) für die drei Eulerwinkel vorgeschrieben.
# 
# Durch die drei Drehungen wird das erdfeste System (engl. world frame) xyz in das körperfeste Koordinatensystem (engl. body frame) XYZ oder umgekehrt gedreht.
# 
# ![](http://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Plane.svg/440px-Plane.svg.png)

# <headingcell level=2>

# Rotationsmatrix berechnen

# <codecell>

def Rypr(y, p, r):
    '''
    Rotationsmatrix für y=yaw, p=pitch, r=roll in degrees
    '''
   
    y = y*np.pi/180.0
    p = p*np.pi/180.0
    r = r*np.pi/180.0        
    
    Rr = np.matrix([[1.0, 0.0, 0.0],[0.0, np.cos(r), np.sin(r)],[0.0, -np.sin(r), np.cos(r)]])
    Rp = np.matrix([[np.cos(p), 0.0, -np.sin(p)],[0.0, 1.0, 0.0],[np.sin(p), 0.0, np.cos(p)]])
    Ry = np.matrix([[np.cos(y), np.sin(y), 0.0],[-np.sin(y), np.cos(y), 0.0],[0.0, 0.0, 1.0]])
    
    return Rr*Rp*Ry

# <markdowncell>

# $\begin{align}
# R & =   
#  \begin{pmatrix}
#     1 & 0          & 0          \\
#     0 & \cos \Phi   & \sin \Phi \\
#     0 & - \sin \Phi & \cos \Phi
#   \end{pmatrix}
#   \begin{pmatrix}
#     \cos \Theta & 0 & - \sin \Theta \\
#     0           & 1 & 0             \\
#     \sin \Theta & 0 & \cos \Theta
#   \end{pmatrix}
#    \begin{pmatrix}
#     \cos \Psi   & \sin \Psi & 0 \\
#     - \sin \Psi & \cos \Psi & 0 \\
#     0           & 0         & 1
#   \end{pmatrix} 
# \end{align}$

# <codecell>

gieren = 10.0
nicken = 0.0
wanken = 0.0

R = Rypr(gieren, nicken, wanken)
R

# <headingcell level=2>

# Rotation eines Vektors

# <codecell>

g = np.matrix([[1.0], [0.0], [0.0]])

# <markdowncell>

# $v_B = R \cdot g$

# <codecell>

vB = R*g
vB

# <headingcell level=2>

# Rücktransformation

# <markdowncell>

# $g = R^T \cdot v_B$

# <codecell>

RT = np.transpose(R)
RT

# <codecell>

g2 = RT*vB
g2

# <headingcell level=2>

# Plot it

# <codecell>

def plotvek3Dpersp(x, y, z):
    hor = (0, 90, 45)
    vert= (90, 0, 45)
    tit = ('Seitenansicht', 'Draufsicht', '3D')
    fig = plt.figure(figsize=(15,4.5))
    for subplotnumber in range(3):
        ax = fig.add_subplot(1,3, subplotnumber, projection='3d')
        
        ax.plot([0, x], [0, y], [0, z], label='$v_B$')
        ax.plot([0, g[0]], [0, g[1]], [0, g[2]], label='$g$')
        
        ax.scatter(0,0,0, color='k')
        
        ax.axis('equal')
        ax.view_init(hor[subplotnumber], vert[subplotnumber])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        plt.title(tit[subplotnumber] + '\nG: %i, N: %i, W: %i' % (gieren, nicken, wanken))
        ax.set_zlim3d(-1, 1)
        plt.legend(loc='best');
        plt.tight_layout()
    return plt

# <codecell>

x, y, z = vB
plotvek3Dpersp(x, y, z);

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <markdowncell>

# Thanks to [Jake Vanderplas](http://jakevdp.github.io/blog/2012/11/24/simple-3d-visualization-in-matplotlib/), who wrote a Quaternion Class

# <codecell>


