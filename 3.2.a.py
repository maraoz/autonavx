import numpy as np
import math
from math import cos, sin

import numpy as np

class Pose3D:
  def __init__(self, rotation, translation):
    self.rotation = rotation
    self.translation = translation

  def inv(self):
    '''
    Inversion of this Pose3D object

    :return inverse of self
    '''

    inv_rotation = self.rotation.T
    inv_translation = -1 * self.translation
    return Pose3D(inv_rotation, inv_translation)

  def __mul__(self, other):
    '''
    Multiplication of two Pose3D objects, e.g.:
        a = Pose3D(...) # = self
        b = Pose3D(...) # = other
        c = a * b       # = return value

    :param other: Pose3D right hand side
    :return product of self and other
    '''
    resulting_rotation = np.dot(self.rotation, other.rotation)
    resulting_translation = self.translation + np.dot(resulting_rotation, other.translation)
    ret = Pose3D(resulting_rotation, resulting_translation)
    return ret

  def __str__(self):
    return "rotation:\n" + str(self.rotation) + "\ntranslation:\n" + str(self.translation.transpose())

def compute_quadrotor_pose(twm, tqm):
  '''
  :param global_marker_pose: Pose3D 
  :param observed_marker_pose: Pose3D

  :return global quadrotor pose computed from global_marker_pose and observed_marker_pose
  '''
  tmq = tqm.inv()
  twq = twm * tmq
  return twq


#twq = compute_quadrotor_pose(twm, tqm)

