import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixel_ring = neopixel.NeoPixel(board.D13, 12, bpp=4)


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


BLUE = (0, 0, 255, 0)
WHITE = (0,0,0,255)

# do this forever
while True:

    # read both of the switch inputs
    sw_1_read = sw_1.value
    sw_2_read = sw_2.value

    # set the values of the output leds to match the values of the switch inputs
    red_led.value = not sw_1_read
    blue_led.value = not sw_2_read


    if sw_2_read is False:
        pixel_ring.fill(BLUE)
        print("blue")
    else:
        pixel_ring.fill(WHITE)
        print("white")
