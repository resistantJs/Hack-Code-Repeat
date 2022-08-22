## Setup Block ##
import time
import board
import adafruit_mpr121
import neopixel

# create an I2C() object
i2c = board.I2C()

# cretae an object for the mpr121
touch = adafruit_mpr121.MPR121(i2c)

# a neopixel object to visualize the output with the 12 pixel rgbw ring
pixel_ring = neopixel.NeoPixel(board.D13, 12, bpp=4, auto_write=False)

color = (252, 70, 0, 0)

# loop forever
while True:
    ## Input Block ##
    # WE CAN GET THE STATE OF ALL OF THE TOUCH PINS AT ONCE AS A TUPLE!!!
    touches = touch.touched_pins
    print(touches)

    ## output block ##
    # compare the touches tuple to the touches_pre touple
    for index in range(12):
        if touches[index] == True:
            # if a pad is True light up a corresponding neopixel
            pixel_ring[index] = color
        else:
            # otherwise turn it off
            pixel_ring[index] = 0

    # after the for loop is complete, show the new pixels
    pixel_ring.show()

    time.sleep(0.03)
