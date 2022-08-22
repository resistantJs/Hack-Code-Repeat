## Setup Block ##
import time
import board
import adafruit_lis3dh

# create an I2C() object
i2c = board.I2C()

# cretae an object for the lis3dh
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_4_G

# a varible to count shake detections
shake_count = 0

# loop forever
while True:
    ## Input Block ##
    # see if the sensor is shaken (higher thresholds require more forceful shake)
    is_shaken = lis3dh.shake(shake_threshold=10)

    ## Ouput Block ##
    # print the values
    if is_shaken:
        shake_count += 1
        print('The sensor was shaken:', shake_count)
    # print()

    time.sleep(0.01)
