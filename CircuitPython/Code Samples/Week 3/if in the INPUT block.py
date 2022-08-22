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
WHITE = (0, 0, 0, 255)

pixel_ring.fill(WHITE)

# create DigitalInOut objects for both STEMMA switches
sw1 = DigitalInOut(board.D5)
sw1.switch_to_input()
# create a digitalio object called sw2
sw2 = DigitalInOut(board.D6)
sw2.switch_to_input()

# variable to track the desired output brightness
brightness = 1.0

# loop forever
while True:
    ## input block ##
    # read sw1 and sw2 inputs into local variables
    sw1_read = sw1.value
    sw2_read = sw2.value
    print('sw1 is:', sw1_read)
    print('sw2 is:', sw2_read)

    # use if elif in the input block to increment and decrement a brightness value
    if sw1_read == False:
        brightness -= 0.01
    elif sw2_read == False:
        brightness += 0.01

    ## Calculation BLock ##
    # constrain the brigtness property to 0 - 1.0
    if brightness > 1:
        brightness = 1
    elif brightness < 0:
        brightness = 0

    ## output block ##
    # use if elif to set four color values on blue_led
    pixel_ring.brightness = brightness

    print()
    time.sleep(0.01)
