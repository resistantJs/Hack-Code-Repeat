## Setup Block ##
import time
import board
from digitalio import DigitalInOut, Pull
import neopixel
import analogio
from simpleio import map_range

# declare a analogio object on board.A0
a1 = analogio.AnalogIn(board.A0)

# create a neopixel object for the 12 pixel RGBW ring
pixel_ring = neopixel.NeoPixel(board.D13, 12, bpp=4)
# for the RGBW ring the parameter bpp=4 must be set!
# this stands for Bytes Per Pixel and the fourth byte is WHITE

# for RGBW neopixels we can only set the colors using Tuples
# this block of code will setup colors as Tuples (RED, GREEN, BLUE, WHITE)
WHITE = (0, 0, 0, 255)

pixel_ring.fill(WHITE)

# loop forever
while True:
    ## Input Block ##
    # gather input values as an integer
    a1_read = a1.value
    print(a1_read)

    ## Calculation Block ##
    scaled_brightness = map_range(a1_read, 0, 65535, 0, 1)
    print(scaled_brightness)

    ## Output Block ##
    pixel_ring.brightness = scaled_brightness
    print() # a space to visualize each loop

    # sleep to see changes in the serial monitor
    time.sleep(0.1)
