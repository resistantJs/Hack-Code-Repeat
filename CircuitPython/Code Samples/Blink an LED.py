import board
import time
from digitalio import DigitalInOut, Direction

# instantiate the DigitalInOut object
led = DigitalInOut(board.D3)

# set the ext_led object to an output
led.switch_to_output()

while True:
	# turn the led on
	led.value = True
	# wait a second
	time.sleep(1)
	# turn the led off again
	led.value = False
	# wait a second again
	time.sleep(1)
	# the loop will do this over and over again
