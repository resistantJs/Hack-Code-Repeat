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

while True:

    # call the .fill method with a color TUPLE of Red
    pixel_ring.fill(RED)
    print("red")
    time.sleep(1)
    # call the .fill method with a color hex code of Green
    pixel_ring.fill(GREEN)
    print("green")
    time.sleep(1)
    # call the .fill method with a color hex code of Blue
    pixel_ring.fill(BLUE)
    print("blue")
    time.sleep(1)
    # call the .fill method with a color hex code of White
    pixel_ring.fill(WHITE)
    print("white")
    time.sleep(1)
