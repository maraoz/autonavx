import numpy as np
import math
from math import cos, sin
position = np.array([[0], [0]])

class NavData(object):
  pass
navdata = NavData()
navdata.rotX = math.pi/4
navdata.rotY = math.pi/4
navdata.rotZ = math.pi/4
navdata.vx = 10
navdata.vy = 20

yaw = navdata.rotZ

r = np.array([
  [cos(yaw), -sin(yaw)],
  [sin(yaw), cos(yaw)],
  [0,0]
])
t = np.array([
  [navdata.vx],
  [navdata.vy],
  [1]
])

T = np.hstack((r, t))

local = np.vstack((np.copy(position), np.array([1])))
position = np.dot(T, local)

print T
print local
print position
