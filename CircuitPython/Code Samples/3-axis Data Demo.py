## Setup Block ##
import time
import board
import adafruit_lis3dh

# create an I2C() object
i2c = board.I2C()

# cretae an object for the lis3dh
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

# cretae an object for the lis3dh
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

# loop forever
while True:
    ## Input Block ##
    # capture all three x y and z values at once
    x, y, z = lis3dh.acceleration

    ## Ouput Block ##
    # print the values
    print('X accl is:', x)
    print('Y accl is:', y)
    print('Z accl is:', z)
    # print as a tuple for serial plotter
    print((x, y, z, ))
    print()

    time.sleep(0.1)
