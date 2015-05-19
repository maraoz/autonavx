from plot import plot
import math

class UserCode:
    def __init__(self):
        # initialize data you want to store in this object between calls to the measurement_callback() method
        self.maxRotZP = 0
        self.lastRotZ = 0

    def measurement_callback(self, t, dt, navdata):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param navdata: measurements of the quadrotor
        '''

        rotZP = (navdata.rotZ - self.lastRotZ)/dt
        if self.maxRotZP < math.fabs(rotZP):
            self.maxRotZP = math.fabs(rotZP)
        # add your plot commands here
        #plot("rotZ", navdata.rotZ)
        #plot("dt", dt)
        #plot("lastRotZ", self.lastRotZ)
        #plot("rotZ", navdata.rotZ)
        plot("rotZP", rotZP)
        #plot("maxRotZP", self.maxRotZP)

        self.lastRotZ = navdata.rotZ

