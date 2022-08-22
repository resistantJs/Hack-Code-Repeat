## Setup Block ##
import time
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_sh1107

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

# next we need to create a text label to display a message
txt_msg = label.Label(terminalio.FONT, text=''*15, color=0xFFFFFF, x=0, y=5)
## The text=''*20 argument above creates space for 15 characters
# all messages in this label must be 15 characters or less
# then we append it to our display group
canvas.append(txt_msg)
# to see text on the screen we simply modify the .text property of the label
txt_msg.text = 'Hello World!!!'

# loop forever
while True:
    ## OUTPUT BLOCK ##
    # flash back and forth between two messages while moving them!
    txt_msg.y = 4
    txt_msg.text = 'Hello World!!!'
    time.sleep(1)
    txt_msg.y = 58
    txt_msg.text = 'Goodbye World!'
    time.sleep(1)
