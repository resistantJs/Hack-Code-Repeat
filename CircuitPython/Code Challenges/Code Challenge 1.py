import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixel_ring = neopixel.NeoPixel(board.D13, 12, bpp=4)
pixel_ring.brightness = 0.5
last = 0.5
# 0 to 1


# create a digitalinout object for the breadboard wired switch
sw_1 = DigitalInOut(board.D6)
# set as an input with pull up
sw_1.switch_to_input()

# create a digitalinout object for the STEMMA switch
sw_2 = DigitalInOut(board.D5)
# set as an input, no need for a pull becuase the PCB has a pull-up resistor
sw_2.switch_to_input()

# create a digitalinout object for the STEMMA switch
sw_3 = DigitalInOut(board.D9)
# set as an input, no need for a pull becuase the PCB has a pull-up resistor
sw_3.switch_to_input()

# create a digitalinout object for the STEMMA switch
sw_4 = DigitalInOut(board.D10)
# set as an input, no need for a pull becuase the PCB has a pull-up resistor
sw_4.switch_to_input()

# create a digtitalinout object for both onboard LEDs
# these pins have names corresponding to their colors in the board module
red_led = DigitalInOut(board.RED_LED)
red_led.direction = Direction.OUTPUT

blue_led = DigitalInOut(board.BLUE_LED)
blue_led.direction = Direction.OUTPUT


RED = (255, 0, 0, 0)
GREEN = (0, 255, 0, 0)
BLUE = (0, 0, 255, 0)
WHITE = (0, 0, 0, 255)

light_state = False
color = RED
color_ind = 1
# do this forever
while True:

    # read both of the switch inputs
    sw_1_read = sw_1.value
    sw_2_read = sw_2.value
    sw_3_read = sw_3.value
    sw_4_read = sw_4.value

    sw_1_pre = not sw_1_read
    sw_2_pre = not sw_2_read
    # set the values of the output leds to match the values of the switch inputs
    red_led.value = not sw_1_read
    blue_led.value = not sw_2_read
    red_led.value = not sw_3_read
    blue_led.value = not sw_4_read


    if sw_1_read != sw_1_pre:
        # sw1_read is not equal to sw1_pre so the switch state has changed
        # since it changed, lets save the new value to sw1_pre

        sw_1_pre = sw_1_read
        # if the state of the switch is False, it has been pushed down
        if sw_1_read == False:
            # toggle the light variable
            light_state = not light_state
            if light_state is False:
                last = pixel_ring.brightness
                pixel_ring.brightness = 0
            else:
                pixel_ring.brightness = last
                pixel_ring.fill(color)
    #print("last: "  + str(last))

    if color_ind == 1:
        color = RED
        pixel_ring.fill(color)
    if color_ind == 2:
        color = GREEN
        pixel_ring.fill(color)
    if color_ind == 3:
        color = BLUE
        pixel_ring.fill(color)
    if color_ind == 4:
        color = WHITE
        pixel_ring.fill(color)
    #print(color)
    print(light_state)
    if sw_2_pre is not sw_2_read:
        sw_2_pre = sw_2_read
        if sw_2_read is False and color_ind < 4:
            color_ind += 1
        elif sw_2_read is False and color_ind == 4:
            color_ind = 1

    print(color_ind)

    if sw_3_read is False and 0 <= pixel_ring.brightness <= 1 :
        pixel_ring.brightness -= 0.25
    elif sw_4_read is False and 0 <= pixel_ring.brightness <= 1 :
        pixel_ring.brightness += 0.25
    #print(pixel_ring.brightness)
    time.sleep(0.1)
