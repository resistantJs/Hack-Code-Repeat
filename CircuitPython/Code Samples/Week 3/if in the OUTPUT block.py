
## Setup Block ##
# import modules
import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

# create a neopixel object for the 12 pixel RGBW ring
pixel_ring = neopixel.NeoPixel(board.D13, 12, bpp=4)
# for the RGBW ring the parameter bpp=4 must be set!
# this stands for Bytes Per Pixel and the fourth byte is WHITE

# for RGBW neopixels we can only set the colors using Tuples
# this block of code will setup colors as Tuples (RED, GREEN, BLUE, WHITE)
RED = (255, 0, 0, 0)
GREEN = (0, 255, 0, 0)
BLUE = (0, 0, 255, 0)
WHITE = (0, 0, 0, 255)

# create DigitalInOut objects for both STEMMA switches
sw1 = DigitalInOut(board.D5)
sw1.switch_to_input()
# create a digitalio object called sw2
sw2 = DigitalInOut(board.D6)
sw2.switch_to_input()

# loop forever
while True:
    ## input block ##
    # read sw1 and sw2 inputs into local variables
    sw1_read = sw1.value
    sw2_read = sw2.value
    print('sw1 is:', sw1_read)
    print('sw2 is:', sw2_read)

    ## output block ##
    # use if elif to set four color values on blue_led
    if sw1_read == True and sw2_read == True:
        print('color set to OFF')
        pixel_ring.fill(0)
    elif sw1_read == False and sw2_read == False:
        print('color set to RED')
        pixel_ring.fill(RED)
    elif sw1_read == False and sw2_read == True:
        print('color set to GREEN')
        pixel_ring.fill(GREEN)
    elif sw1_read == True and sw2_read == False:
        print('color set to BLUE')
        pixel_ring.fill(BLUE)

    print()
    time.sleep(0.1)
