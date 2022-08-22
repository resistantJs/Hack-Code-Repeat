## Setup Block ##
import board
import time
import adafruit_apds9960.apds9960

# create an I2C() object
i2c = board.I2C()

# create an object for the APDS9960
apds = adafruit_apds9960.apds9960.APDS9960(i2c)

# enable gesture input (gesture requries proximity also)
apds.enable_gesture = True
apds.enable_proximity = True

# a variable to store the previous gesture
pre_gesture = apds.gesture()

# loop forever
while True:
    ## Input Block ##
    # poll the sensor for a gesture
    this_gesture = apds.gesture()

    ## Calculation Block ##

    ## Ouput Block ##
    if this_gesture != pre_gesture:
        pre_gesture = this_gesture
        if this_gesture != 0:
            print(this_gesture)
            if this_gesture == 1:
                print('UP')
            if this_gesture == 2:
                print('DOWN')
            if this_gesture == 3:
                print('LEFT')
            if this_gesture == 4:
                print('RIGHT')

    time.sleep(0.05)
