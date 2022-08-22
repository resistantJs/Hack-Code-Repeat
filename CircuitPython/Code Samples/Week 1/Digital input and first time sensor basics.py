# import modules and libraries
import board
from digitalio import DigitalInOut, Pull
import time

# declare a DigitalInOut object and configure it as an input
sw = DigitalInOut(board.SWITCH)
sw.switch_to_input(pull=Pull.UP)

# repeat this code forever
while True:

    # "read" the switch value by saving its value to a new variable
    sw_read = sw.value

    # print the switch value reading
    print(sw_read)

    # pause for a bit so we can see the serial prints
    time.sleep(0.1)
