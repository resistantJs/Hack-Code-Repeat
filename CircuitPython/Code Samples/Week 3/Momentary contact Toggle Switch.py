## Setup Block ##
import time
import board
from digitalio import DigitalInOut, Pull
import neopixel

# declare a DigitalInOut for a STEMMA switch
sw1 = DigitalInOut(board.D5)
sw1.switch_to_input()

# declare a neopixel object for the pixel ring wired to D13
pixel_ring = neopixel.NeoPixel(board.D13, 12, bpp=4)

# declare a color constant to fill the pixels with
WHITE = (0, 0, 0, 255)

# variable to track the previous value of the switch
sw1_pre = sw1.value

# variable to track the desired output state
light = False

# loop forever
while True:
    ## Input Block ##
    # gather input values as an integer
    sw1_read = int(sw1.value)

    # compare the previous sw1 state to the current state with if
    if sw1_read != sw1_pre:
        # sw1_read is not equal to sw1_pre so the switch state has changed
        # since it changed, lets save the new value to sw1_pre
        sw1_pre = sw1_read
        # if the state of the switch is False, it has been pushed down
        if sw1_read == False:
            print("The switch was pressed")
            # toggle the light variable
            light = not light
        else:
            print("The switch was released")

    ## Output Block ##
    if light == True:
        pixel_ring.fill(WHITE)
    else:
        pixel_ring.fill(0)

    # sleep to see changes in the serial monitor
    time.sleep(0.1)
