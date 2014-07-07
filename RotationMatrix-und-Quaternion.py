# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Rotation im Raum (3D)

# <codecell>

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from IPython.html.widgets import interact
from IPython.html import widgets

# <codecell>

%matplotlib inline

# <headingcell level=1>

# Drehung nach Z, Y', X'' Konvention

# <markdowncell>

# In der Fahrzeugtechnik (Luftfahrt: DIN 9300; Automobilbau : DIN 70000; Schifffahrt) ist die (z,y',x'')-Konvention gebräuchlich. In den Normen sind die Verwendung der Formelzeichen $\Psi$, $\Theta$ und $\Phi$ und die Namen Gier-, Nick- und Roll-Winkel (engl. yaw, pitch and roll angle) für die drei Eulerwinkel vorgeschrieben.
# 
# Durch die drei Drehungen wird das erdfeste System (engl. world frame) xyz in das körperfeste Koordinatensystem (engl. body frame) XYZ oder umgekehrt gedreht.
# 
# ![DIN70000](http://mechlab-engineering.de/wordpress/wp-content/uploads/2014/03/Fahrzeug-Koordinatensystem-DIN70000-669x333.png)

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
    
    Rr = np.matrix([[1.0, 0.0, 0.0],[0.0, np.cos(r), -np.sin(r)],[0.0, np.sin(r), np.cos(r)]])
    Rp = np.matrix([[np.cos(p), 0.0, np.sin(p)],[0.0, 1.0, 0.0],[-np.sin(p), 0.0, np.cos(p)]])
    Ry = np.matrix([[np.cos(y), -np.sin(y), 0.0],[np.sin(y), np.cos(y), 0.0],[0.0, 0.0, 1.0]])
    
    return Rr*Rp*Ry

# <markdowncell>

# $\begin{align}
# R & =   
#  \begin{pmatrix}
#     1 & 0          & 0          \\
#     0 & \cos \phi   & -\sin \phi \\
#     0 & \sin \phi & \cos \phi
#   \end{pmatrix}
#   \begin{pmatrix}
#     \cos \theta & 0 & \sin \theta \\
#     0           & 1 & 0             \\
#     -\sin \theta & 0 & \cos \theta
#   \end{pmatrix}
#    \begin{pmatrix}
#     \cos \psi   & -\sin \psi & 0 \\
#     \sin \psi & \cos \psi & 0 \\
#     0           & 0         & 1
#   \end{pmatrix} 
# \end{align}$

# <codecell>

gieren = 00.0
nicken = 45.0
wanken = 00.0

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
        plt.title(tit[subplotnumber] + '\nW: %i, N: %i, G: %i' % (wanken, nicken, gieren))
        ax.set_zlim3d(-1, 1)
        plt.legend(loc='best');
        plt.tight_layout()
    return plt

# <codecell>

x, y, z = vB
plotvek3Dpersp(x, y, z);

# <headingcell level=2>

# Let's make it interactive

# <markdowncell>

# IPython Notebook muss lokal ausgeführt werden (Download), um die Interaktivität zu ermöglichen

# <codecell>

@interact
def plotrot3Dpersp(wanken = widgets.FloatSliderWidget(min=-180.0, max=180.0, step=1.0, value=0.0, description=""), \
                   nicken = widgets.FloatSliderWidget(min=-180.0, max=180.0, step=1.0, value=0.0, description=""), \
                   gieren = widgets.FloatSliderWidget(min=-180.0, max=180.0, step=1.0, value=0.0, description="")):
    
    R = Rypr(gieren, nicken, wanken)
    x, y, z = R*g
    
    hor = (0, 90, 45)
    vert= (90, 0, 45)
    tit = ('Seitenansicht', 'Draufsicht', '3D')
    fig = plt.figure(figsize=(15,4.5))
    for subplotnumber in range(3):
        ax = fig.add_subplot(1,3, subplotnumber, projection='3d')
        
        ax.plot([0, x], [0, y], [0, z], label='$g \cdot R$')
        ax.plot([0, g[0]], [0, g[1]], [0, g[2]], label='$g$')
        
        ax.scatter(0,0,0, color='k')
        
        ax.axis('equal')
        ax.view_init(hor[subplotnumber], vert[subplotnumber])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        plt.title(tit[subplotnumber] + '\nW: %i, N: %i, G: %i' % (wanken, nicken, gieren))
        ax.set_zlim3d(-1, 1)
        plt.legend(loc='best');
        plt.tight_layout()

# <headingcell level=1>

# Drehung in der Quaternion

# <markdowncell>

# Bei der Beschreibung der Drehung mit 3 Euler Winkel, gibt es Probleme bei bestimmten Konstellationen ("[Gimbal-Lock](http://de.wikipedia.org/wiki/Gimbal_Lock)").
# 
# "_Physikalisch-anschaulich äußert sich das Unbestimmtheitsproblem beispielsweise bei einem senkrecht nach unten ausgerichteten Flugzeug durch das Zusammenfallen der erdfesten z- und der flugzeugfesten x-Achse. Sowohl ein „Gieren um die z-Achse als auch ein Rollen mit um die x-Achse führen jetzt zur gleichen Bewegung um die senkrechte Flugzeuglängsachse (Gimbal Lock).
# Zur Lösung des Problems kann man in der Lagedifferenzialgleichung als Zustandsgrößen statt der drei Lagewinkel [Φ Θ Ψ ] die vier Komponenten einer Quaternion [ a b c d ] verwenden._" - Buchholz, J. J. (2013). [Vorlesungsmanuskript Regelungstechnik und Flugregler](http://www.grin.com/de/e-book/82818/regelungstechnik-und-flugregler)
# 
# $\mathbb{H}$ - nach ihrem Entdecker [W. R. Hamilton](http://de.wikipedia.org/wiki/William_Rowan_Hamilton)
# 
# Ähnlich wie bei den komplexen Zahlen, die als Summe aus Real- und Imaginärteil beschrieben werden ($Z = a\cdot 1 + b \cdot \mathrm{i}$), wird die Quaternion als Linearkombination aus 3 Imaginärteilen und einem Realteil konstruiert: $q = a\cdot 1 + b \cdot \mathrm{i} + c \cdot \mathrm{j} + d \cdot \mathrm{k}$.
# 
# [Mehr auf WolframMathWorld...](http://mathworld.wolfram.com/Quaternion.html)

# <markdowncell>

# Die Quaternion muss außerdem als Einheitsquaternion ausgedrückt werden (normiert):
# $|q| = \sqrt{a^2+b^2+c^2+d^2}$
# 
# $q^0 = \frac{q}{|q|} = \frac{a}{|q|}+\frac{b}{|q|}\cdot\mathrm{i}+\frac{c}{|q|}\cdot\mathrm{j}+\frac{d}{|q|}\cdot\mathrm{k}$

# <codecell>

def normQ(q):
    '''Calculates the normalized Quaternion
    a is the real part
    b, c, d are the complex elements'''
    # Source: Buchholz, J. J. (2013). Vorlesungsmanuskript Regelungstechnik und Flugregler.
    # GRIN Verlag. Retrieved from http://www.grin.com/de/e-book/82818/regelungstechnik-und-flugregler
    a, b, c, d = q
   
    # Betrag
    Z = np.sqrt(a**2+b**2+c**2+d**2)
    
    return np.array([a/Z,b/Z,c/Z,d/Z])

# <markdowncell>

# Bei der Beschreibung der 3D-Drehung mit der Quaternion, wird mit den imaginären Elementen $b$, $c$ und $d$ ein Vektor definiert, um den mit $a$ gedreht wird.
# ![Quaternion Rotation](http://www.opengl-tutorial.org/wp-content/uploads/2012/08/quaternion.png)
# Quelle: http://www.opengl-tutorial.org/intermediate-tutorials/tutorial-17-quaternions/
# 
# Dabei berechnet sich der Drehwinkel $w=2\arccos(a)$
# 
# und die 3 Vektorkoordinaten der Rotationsaxe $n_R=\left[\begin{matrix}\cfrac{b}{\sin(\frac{w}{2})} \\ \cfrac{c}{\sin(\frac{w}{2})} \\ \cfrac{d}{\sin(\frac{w}{2})}\end{matrix}\right]$

# <codecell>

def Q2DuD(q):
    '''Calculates the Rotation Angle and Rotation Axis from Quaternion'''
    # Source: Buchholz, J. J. (2013). Vorlesungsmanuskript Regelungstechnik und Flugregler.
    # GRIN Verlag. Retrieved from http://www.grin.com/de/e-book/82818/regelungstechnik-und-flugregler
    a, b, c, d = q
    
    
    w = 2.0*np.arccos(a) # rotation angle
    s = np.sin(w/2.0)
    n = np.array([b/s, c/s, d/s]) # rotation axis
    return w, n

# <markdowncell>

# Die Rotationsmatrix kann aus der Quaternion berechnet werden.
# 
# $R = \left[\begin{matrix}(a^2+b^2-c^2-d^2) & 2(bc+ad) & 2(bd-ac) \\ 2(bc-ad) & (a^2-b^2+c^2-d^2) & 2(cd+ab) \\ 2(bd+ac) & 2(cd-ab) & (a^2-b^2-c^2+d^2)\end{matrix}\right]$

# <codecell>

def QtoR(q):
    '''Calculates the Rotation Matrix from Quaternion
    a is the real part
    b, c, d are the complex elements'''
    # Source: Buchholz, J. J. (2013). Vorlesungsmanuskript Regelungstechnik und Flugregler.
    # GRIN Verlag. Retrieved from http://www.grin.com/de/e-book/82818/regelungstechnik-und-flugregler
    q = normQ(q)
    
    a, b, c, d = q
    
    R11 = (a**2+b**2-c**2-d**2)
    R12 = 2.0*(b*c+a*d)
    R13 = 2.0*(b*d-a*c)
    R21 = 2.0*(b*c-a*d)
    R22 = a**2-b**2+c**2-d**2
    R23 = 2.0*(c*d+a*b)
    R31 = 2.0*(b*d+a*c)
    R32 = 2.0*(c*d-a*b)
    R33 = a**2-b**2-c**2+d**2
    return np.matrix([[R11, R12, R13],[R21, R22, R23],[R31, R32, R33]])

# <codecell>

@interact
def plotrot3Dpersp(a = widgets.FloatSliderWidget(min=-1.0, max=1.0, step=0.01, value=0.0, description=""), \
                   b = widgets.FloatSliderWidget(min=-1.0, max=1.0, step=0.1, value=1.0, description=""), \
                   c = widgets.FloatSliderWidget(min=-1.0, max=1.0, step=0.1, value=0.0, description=""), \
                   d = widgets.FloatSliderWidget(min=-1.0, max=1.0, step=0.1, value=0.0, description="")):

    q = np.array([a, b, c, d])
    R = QtoR(q)
    
    print('Rotationsmatrix\n%s' % R)
    
    x, y, z = R*g

    hor = (0, 90, 45)
    vert= (90, 0, 45)
    tit = ('Seitenansicht', 'Draufsicht', '3D')
    fig = plt.figure(figsize=(15,4.5))
    for subplotnumber in range(3):
        ax = fig.add_subplot(1,3, subplotnumber, projection='3d')
        
        ax.plot([0, x], [0, y], [0, z], label='$g \cdot R$')
        ax.plot([0, g[0]], [0, g[1]], [0, g[2]], label='$g$')
        
        # Drehachse einzeichnen
        w, n = Q2DuD(q)
        ax.plot([0, n[0]], [0, n[1]], [0, n[2]], label='$n_R$')
        
        ax.scatter(0,0,0, color='k')
        
        ax.axis('equal')
        ax.view_init(hor[subplotnumber], vert[subplotnumber])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        plt.title(tit[subplotnumber])
        ax.set_zlim3d(-1, 1)
        plt.legend(loc='best');
        plt.tight_layout()

# <codecell>


