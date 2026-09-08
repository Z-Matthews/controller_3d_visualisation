class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get(self):
        return self.x, self.y, self.z


from math import cos, sin, pi, radians
import numpy as np
class Position:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        # self.yaw = 0
        # self.pitch = 0
        # self.roll = 0

        # theta[0] = joint angle in degrees
        # theta[1] = dh table modifier (angle in degrees)
        # theta[2] = total (angle in radians)
        # etc
        self.theta =    [0, 0, 0]
        self.d =        [0, 0, 0]
        self.r =        [0, 0, 0]
        self.alpha =    [0, 0, 0]

        self.homogeneous_transformation = None
        self.resultant_homogen = None
        self.calculate_transform()

    def update_dh_mods(self, theta_mod=None, d_mod=None, r_mod=None, alpha_mod=None):
        if theta_mod is not None:
            self.theta[1] = theta_mod
            self.theta[2] = radians(self.theta[0] + self.theta[1])
        if d_mod is not None:
            self.d[1] = d_mod
            self.d[2] = self.d[0] + self.d[1]
        if r_mod is not None:
            self.r[1] = r_mod
            self.r[2] = self.r[0] + self.r[1]
        if alpha_mod is not None:
            self.alpha[1] = alpha_mod
            self.alpha[2] = radians(self.alpha[0] + self.alpha[1])

        self.calculate_transform()

    def update_dh(self, theta=None, d=None, r=None, alpha=None):
        if theta is not None:
            self.theta[0] = theta
            self.theta[2] = radians(self.theta[0] + self.theta[1])
        if d is not None:
            self.d[0] = d
            self.d[2] = self.d[0] + self.d[1]
        if r is not None:
            self.r[0] = r
            self.r[2] = self.r[0] + self.r[1]
        if alpha is not None:
            self.alpha[0] = alpha
            self.alpha[2] = radians(self.alpha[0] + self.alpha[1])

        self.calculate_transform()

    def calculate_transform(self):
        self.homogeneous_transformation = [[cos(self.theta[2]),     -1*sin(self.theta[2])*cos(self.alpha[2]),       sin(self.theta[2])*sin(self.alpha[2]),          self.r[2]*cos(self.theta[2])],
                                           [sin(self.theta[2]),     cos(self.theta[2])*cos(self.alpha[2]),          -1*cos(self.theta[2])*sin(self.alpha[2]),       self.r[2]*sin(self.theta[2])],
                                           [0,                      sin(self.alpha[2]),                             cos(self.alpha[2]),                             self.d[2]],
                                           [0,                      0,                                              0,                                              1]]
        self.homogeneous_transformation = np.array(self.homogeneous_transformation)
        self.x = self.homogeneous_transformation[0][3]
        self.y = self.homogeneous_transformation[1][3]
        self.z = self.homogeneous_transformation[2][3]

    def calculate_resultant_homogen(self, previous_homogen):
        self.resultant_homogen = previous_homogen @ self.homogeneous_transformation
        self.x = self.resultant_homogen[0][3]
        self.y = self.resultant_homogen[1][3]
        self.z = self.resultant_homogen[2][3]

    def get_relative_coordinate(self):
        return self.x, self.y, self.z