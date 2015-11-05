import numpy as np
import math
from math import cos, sin

x = math.pi/2
y = 0
z = math.pi/2

print np.array([x,y,z]).T
rz = np.array([
  [cos(z), -sin(z), 0],
  [sin(z), cos(z), 0],
  [0,0, 1]
])
ry = np.array([
  [cos(y), 0, sin(y)],
  [0,1,0],
  [-sin(y), 0, cos(y)]
])
rx = np.array([
  [1, 0, 0],
  [0,cos(x),-sin(x)],
  [0,sin(x), cos(x)]
])
r = np.dot(np.dot(rz, ry), rx)

print r
