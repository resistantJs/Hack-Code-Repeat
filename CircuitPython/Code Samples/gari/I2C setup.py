## Setup Block ##
import board
import time
import adafruit_apds9960.apds9960

# create an I2C() object
i2c = board.I2C()

# create an object for the APDS9960
apds = adafruit_apds9960.apds9960.APDS9960(i2c)
