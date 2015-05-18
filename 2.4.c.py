import numpy as np

r = np.array([
  [0,-1],
  [1, 0]
  ])

vg = np.array([
  [0],
  [1.5]
  ])

vl = np.dot(r.T, vg)

print vl
