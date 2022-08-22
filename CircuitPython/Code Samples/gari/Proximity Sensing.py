## Setup Block ##
import board
import time
import adafruit_apds9960.apds9960

# create an I2C() object
i2c = board.I2C()

# cretae an object for the APDS9960
apds = adafruit_apds9960.apds9960.APDS9960(i2c)

# enable proximity input
apds.enable_proximity = True

# loop forever
while True:
    ## Input Block ##
    # poll the sensor for a proximity value
    this_prox = apds.proximity

    ## Calculation Block ##

    ## Ouput Block ##
    # print the proximity value
    print(this_prox)

    time.sleep(0.05)
