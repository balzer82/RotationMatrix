RotationMatrix
==============

Calculate ZYX Rotation Matrix DIN70000 and Quaternion

![](https://raw.githubusercontent.com/balzer82/RotationMatrix/master/Fahrzeug-Koordinatensystem-DIN70000-669x333.png)

Rotation in 3D ist ein ziemlich kompliziertes Ding, weil man viele verschiedene Konventionen und Definitionen hat. Ließt man im Internet nach, steht auf jeder Seite etwas anderes, weil oftmals keine Definition dazu angegeben ist. Da die Roation mit den 3 Euler Winkeln nicht kommutativ ist, ist die Reihenfolge (Konvention) wichtig.

Hier wird nach der in der Automobilindustrie üblichen ZYX Konvention gedreht (d.h. erst gieren, dann nicken, dann wanken). Dazu gibt es noch die Rotation in Quaternionen-Beschreibung.

Klingt zuerst total kompliziert, ist es aber eigentlich gar nicht.

![Rotation](https://raw.githubusercontent.com/balzer82/RotationMatrix/master/Rotation3D.png)

####[IPython Notebook](http://nbviewer.ipython.org/github/balzer82/RotationMatrix/blob/master/RotationMatrix-und-Quaternion.ipynb)

####[Vimeo Video](https://vimeo.com/100209309)

## Rotation einer Punktwolke

Natürlich kann man auch eine [Punktwolke (Pointcloud)](https://raw.githubusercontent.com/balzer82/RotationMatrix/master/Pointcloud00002.pcd) rotieren.

####[IPython Notebook](http://nbviewer.ipython.org/github/balzer82/RotationMatrix/blob/master/RotatePointCloud.ipynb)

####[Vimeo Video](https://vimeo.com/100388235)