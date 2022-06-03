import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

# create a neopixel object for the 30 pixel RGB strip
pixel_strip = neopixel.NeoPixel(board.D13, 30, bpp=3)

while True:

    # call the .fill method with a color hex code of Red
    pixel_strip.fill(0xff0000)
    time.sleep(1)
    # call the .fill method with a color hex code of Red
    pixel_strip.fill(0x00ff00)
    time.sleep(1)
    # call the .fill method with a color hex code of Red
    pixel_strip.fill(0x0000ff)
    time.sleep(1)
