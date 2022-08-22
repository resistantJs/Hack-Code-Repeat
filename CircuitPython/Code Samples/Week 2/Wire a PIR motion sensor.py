import board
import time
from digitalio import DigitalInOut, Direction, Pull

# create a digitalinout object for the breadboard wired switch
pir = DigitalInOut(board.A0)
# set as an input with pull up
pir.switch_to_input()


# create a digtitalinout object for both onboard LEDs
# these pins have names corresponding to their colors in the board module
red_led = DigitalInOut(board.RED_LED)
red_led.direction = Direction.OUTPUT


# do this forever
while True:

    # read both of the switch inputs
    pir_read = pir.value

    # set the values of the output leds to match the values of the switch inputs
    red_led.value = pir_read
