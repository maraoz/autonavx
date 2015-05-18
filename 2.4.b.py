import numpy as np

lg = np.array([
    [0,-1,-3],
    [1, 0, 3], 
    [0, 0, 1]
    ])
pl = np.array([[1],[-1],[1]])

print np.dot(lg, pl)


