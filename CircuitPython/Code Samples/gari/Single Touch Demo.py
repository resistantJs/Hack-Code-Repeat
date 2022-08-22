## Setup Block ##
import time
import board
import adafruit_mpr121

# create an I2C() object
i2c = board.I2C()

# create an object for the mpr121
touch = adafruit_mpr121.MPR121(i2c)

# a variable to track the previous touch value
touch0_pre = False
# a variable to count touch events
touch0_count = 0

# loop forever
while True:
    ## Input Block ##
    # read the true/false touch value for one pin
    touch0 = touch[0].value

    # check for change in the touch value
    if touch0 != touch0_pre:
        # there was a change, reset the previous value
        touch0_pre = touch0
        # check if the change is touch or not touch
        if touch0:
            print('PAD0 was touched')
            touch0_count += 1
            print(touch0_count)
        else:
            print('PAD0 was released')

    ## Output Block ##

    time.sleep(0.01)
