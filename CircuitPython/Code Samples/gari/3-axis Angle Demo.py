## Setup Block ##
import time
import board
import adafruit_lis3dh
import math

# create an I2C() object
i2c = board.I2C()

# cretae an object for the lis3dh
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

# loop forever
while True:
    ## Input Block ##
    # capture all three x y and z values at once
    x, y, z = lis3dh.acceleration

    ## calculation block ##
    x_angle = math.atan2(y, z) * 57.3
    y_angle = math.atan2(-x, math.sqrt(y ** 2 + z ** 2)) * 57.3

    ## Ouput Block ##
    # print the values
    print('X angle is:', x_angle)
    print('Y angle is:', y_angle)
    # print as a tuple for serial plotter
    print((x_angle, y_angle, ))
    print()

    time.sleep(0.01)
