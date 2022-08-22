## Setup Block ##
import time
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_sh1107
from digitalio import DigitalInOut, Pull

# create digitalio objects for the three switches
sw_a = DigitalInOut(board.D9)
sw_a.switch_to_input(pull=Pull.UP)
sw_b = DigitalInOut(board.D6)
sw_b.switch_to_input(pull=Pull.UP)
sw_c = DigitalInOut(board.D5)
sw_c.switch_to_input(pull=Pull.UP)

# some variables to store the previous values of each switch
sw_a_pre = sw_a.value
sw_b_pre = sw_b.value
sw_c_pre = sw_c.value

# always release displays at the beginning
displayio.release_displays()

# create an I2C() object
i2c = board.I2C()
# create a displayio.I2CDisplay() with the 128x64 featherwing address
d_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# finally create the actual display object called OLED
OLED = adafruit_displayio_sh1107.SH1107(d_bus, width=128, height=64, rotation=0)

# we need a canvas to draw text and objects on
canvas = displayio.Group()
OLED.show(canvas)

# next we need to create a text label to display a message for each switch
sw_a_txt = label.Label(terminalio.FONT, text=''*13, color=0xFFFFFF, x=0, y=5)
# then we append it to our display group
canvas.append(sw_a_txt)
# switch b
sw_b_txt = label.Label(terminalio.FONT, text=''*13, color=0xFFFFFF, x=0, y=31)
# then we append it to our display group
canvas.append(sw_b_txt)
# switch c
sw_c_txt = label.Label(terminalio.FONT, text=''*13, color=0xFFFFFF, x=0, y=57)
# then we append it to our display group
canvas.append(sw_c_txt)

# write the default text to screen
sw_a_txt.text = "sw_A: Not Pressed"
sw_b_txt.text = "sw_B: Not Pressed"
sw_c_txt.text = "sw_C: Not Pressed"

# loop forever
while True:
    ## input block ##
    sw_a_read = sw_a.value
    sw_b_read = sw_b.value
    sw_c_read = sw_c.value

    ## OUTPUT BLOCK ##
    # check for changes in the switches
    # we must do this to prevent writing to the screen over and over again!
    # sw_a
    if sw_a_read != sw_a_pre:
        sw_a_pre = sw_a_read
        # display the new value on the screen
        if sw_a_read:
            sw_a_txt.text = "sw_A: Not Pressed"
        else:
            sw_a_txt.text = "sw_A: Pressed"
    # sw_b
    if sw_b_read != sw_b_pre:
        sw_b_pre = sw_b_read
        # display the new value on the screen
        if sw_b_read:
            sw_b_txt.text = "sw_B: Not Pressed"
        else:
            sw_b_txt.text = "sw_B: Pressed"
    # sw_c
    if sw_c_read != sw_c_pre:
        sw_c_pre = sw_c_read
        # display the new value on the screen
        if sw_c_read:
            sw_c_txt.text = "sw_C: Not Pressed"
        else:
            sw_c_txt.text = "sw_C: Pressed"
