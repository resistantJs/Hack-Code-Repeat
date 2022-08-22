## Setup Block ##
import board
import time
import rotaryio
from digitalio import DigitalInOut, Pull
import neopixel

# declare an output neopixel object for the pixel ring on D13
pixel_ring = neopixel.NeoPixel(board.D13, 12, bpp=4, auto_write=False)

# color constants for the pixels
GREEN = (0, 255, 0, 0)
YELLOW = (128, 127, 0, 0)
ORANGE = (192, 63, 0, 0)
RED = (255, 0, 0, 0)

# a variable to store a current color value and a last_color value
this_color = GREEN
last_color = GREEN

# declare a rotaryio object for the rotary encoder on D6 an D9
encoder = rotaryio.IncrementalEncoder(board.D6, board.D9)

# create a digitalinout object for the encoder push switch on D5
sw1 = DigitalInOut(board.D5)
# set as an input with pull up
sw1.switch_to_input(pull=Pull.UP)

# a variable to remember the previous switch value
sw1_pre = sw1.value

# a varible to increment when the switch is pressed
sw_count = 0

# a variable to remember the current and last pixels lit
this_pixel = 0
last_pixel = 0

# clear the pixels
pixel_ring.fill(0)
# write the color value to this_pixel
pixel_ring[this_pixel] = this_color
# show the pixels
pixel_ring.show()

# loop forever
while True:
    ## Input Block ##
    # read and print the encoder's position property
    encoder_position = encoder.position
    print(encoder_position)

    # gather input from the encoder switch
    sw1_read = sw1.value

    # compare the previous sw1 state to the current state with if
    if sw1_read != sw1_pre:
        # sw1_read is not equal to sw1_pre so the switch state has changed
        # since it changed, lets save the new value to sw1_pre
        sw1_pre = sw1_read
        # if the state of the switch is False, it has been pushed down
        if sw1_read == False:
            print("The switch was pressed")
            sw_count += 1
        else:
            print("The switch was released")
    # print the sw_count to see changes
    print(sw_count)

    ## Calculation Block ##
    # calculate a pixel to light using modulo
    this_pixel = encoder_position % 12
    print(this_pixel)

    # calculate color_mod from sw_count
    color_mod = sw_count % 4
    print(color_mod)

    # select a color using if... elif... and color_mod
    if color_mod == 0:
        this_color = GREEN
    elif color_mod == 1:
        this_color = YELLOW
    elif color_mod == 2:
        this_color = ORANGE
    elif color_mod == 3:
        this_color = RED
    # print this color to see changes in the serial
    print(this_color)

    ## Ouput Block ##
    # check if this_pixel or this_color has changed
    if this_pixel != last_pixel or this_color != last_color:
        # save this_pixel to last_pixel and this_color to last_color
        last_pixel = this_pixel
        last_color = this_color
        # clear the pixels
        pixel_ring.fill(0)
        # write the color value to this_pixel
        pixel_ring[this_pixel] = this_color
        # show the pixels
        pixel_ring.show()

    time.sleep(0.02)
