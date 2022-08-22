## Setup Block ##
import time
import board
import adafruit_apds9960.apds9960
from adafruit_apds9960 import colorutility

# create an I2C() object
i2c = board.I2C()

# cretae an object for the APDS9960
apds = adafruit_apds9960.apds9960.APDS9960(i2c)

# enable color input
apds.enable_color = True

# loop forever
while True:
    ## Input Block ##
    this_time = time.monotonic()
    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    print('capture time is:', time.monotonic() - this_time)

    # color data comes in four variables, save them all at once
    r, g, b, c = apds.color_data

    ## Calculation Block ##
    # calculate a color temperature
    color_temp = colorutility.calculate_color_temperature(r, g, b)

    # calculate an ambient lux level
    light_lux = colorutility.calculate_lux(r, g, b)

    ## Ouput Block ##
    # print the values
    print('r,g,b,c values:', (r, g, b, c, ))
    print('color temp is:', color_temp)
    print('lux level is:', light_lux)
    print()
