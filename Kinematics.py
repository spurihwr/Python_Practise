import sys
import numpy as np
import matplotlib as plt
import  matplotlib.image as mpimg

class Vehicle():
    def_init_(self):

    #parameters
    # throttle to engine torque
    self.a_0 = 400
    self.a_1 = 0.1
    self.a_2 = -0.002

    #Gear ratio,eff radius, mass+inertia
    self.GR = 0.35
    self.r_e = 0.3
    self.J_e = 10
    self.m =  2000
    self.g = 9.81

    #Aerodynamic and friction coefficient
     self.c_a = 1.36
    self.c_r1 = 0.01

    #Tire force
    self.c = 10000
    self.F_max = 10000

    #State Variables
    self.x = 0
    self.v = 5
    self.a = 0
    self.w_e = 100
    self.w_e_dot = 0

    self.sample_time = 0.01

    def reset(self):
        #reset state variables
    self.x = 0
    self.v = 5
    self.a = 0
    self.w_e = 100
    self.w_e_dot = 0
    