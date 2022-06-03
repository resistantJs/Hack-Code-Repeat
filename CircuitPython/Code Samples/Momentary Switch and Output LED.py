import board
import time
from digitalio import DigitalInOut, Direction, Pull

# create a digitalinout object for the breadboard wired switch
sw_1 = DigitalInOut(board.A1)
# set as an input with pull up
sw_1.switch_to_input(pull=Pull.UP)

# create a digitalinout object for the STEMMA switch
sw_2 = DigitalInOut(board.D5)
# set as an input, no need for a pull becuase the PCB has a pull-up resistor
sw_2.switch_to_input()

# create a digtitalinout object for both onboard LEDs
# these pins have names corresponding to their colors in the board module
red_led = DigitalInOut(board.RED_LED)
red_led.direction = Direction.OUTPUT

blue_led = DigitalInOut(board.BLUE_LED)
blue_led.direction = Direction.OUTPUT

# do this forever
while True:

    # read both of the switch inputs
    sw_1_read = sw_1.value
    sw_2_read = sw_2.value

    # set the values of the output leds to match the values of the switch inputs
    red_led.value = not sw_1_read
    blue_led.value = not sw_2_read
