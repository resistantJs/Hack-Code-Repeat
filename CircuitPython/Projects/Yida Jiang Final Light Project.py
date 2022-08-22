## Setup Block ##
import time
import board
import adafruit_lis3dh
import digitalio
import neopixel
import math

# create a neopixel object for the 12 pixel RGBW ring
pixel_ring = neopixel.NeoPixel(board.D13, 12, bpp=4)
# for the RGBW ring the parameter bpp=4 must be set!
# this stands for Bytes Per Pixel and the fourth byte is WHITE

# for RGBW neopixels we can only set the colors using Tuples
# this block of code will setup colors as Tuples (RED, GREEN, BLUE, WHITE)
RED = (200, 0, 0, 50)
GREEN = (0, 200, 0, 50)
BLUE = (0, 0, 250, 50)
YELLOW = (255, 255, 100,0)
CYAN = (102,255,255,0)
color = [RED,GREEN,BLUE,YELLOW,CYAN]
BLACK = (0,0,0,0)
ENGRAM = (229 , 0 , 255 , 0)
fillcolor = CYAN
i = 0
# create an I2C() object
i2c = board.I2C()
int1 = digitalio.DigitalInOut(board.D5)  # Set this to the correct pin for the interrupt!

# cretae an object for the lis3dh
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)


lis3dh.set_tap(2, 45)
# call the .fill method with a color hex code of Purple
pixel_ring.fill(ENGRAM)


STATIC = 0
ROLLING = 1
PAUSE = 3
mode = STATIC

roll_ttl = 1
pre_mono = 1

pre_angle_total = 0

# loop forever
while True:

#PAUSE
    if lis3dh.tapped and mode is PAUSE:
        print("Tapped")
        mode = STATIC
        pixel_ring.fill(ENGRAM)
        time.sleep(0.1)
    elif lis3dh.tapped and (mode is STATIC or mode is ROLLING):
        print("Tapped!")
        mode = PAUSE
        pixel_ring.fill((0,0,0,0))
        time.sleep(0.1 )

#ROLLING
    ## Input Block ##
    # capture all three x y and z values at once
    x, y, z = lis3dh.acceleration

    ## calculation block ##
    x_angle = math.atan2(y, z) * 57.3
    y_angle = math.atan2(-x, math.sqrt(y ** 2 + z ** 2)) * 57.3

    ## Ouput Block ##
    # print the values
    #print('X angle is:', x_angle)
    #print('Y angle is:', y_angle)
    # print as a tuple for serial plotter
    #print((x_angle, y_angle, ))
    #print()

    #calculation of angle_total and angle_light_percent
    if (y_angle < 80) and (abs(x_angle) > 0):
        angle_total = abs(y_angle) + abs(x_angle)
        angle_light_percent = angle_total / 260 #max total when y < 80
    elif (y_angle >=80):
        angle_total = abs(y_angle)
        angle_light_percent = angle_total / 90 #solely determined by y when y > 80

    if angle_light_percent < 0.2:
        angle_light_percent = 0.2

    angle_total_delta = abs(angle_total - pre_angle_total)
    #print(angle_total_delta)

    if (angle_total_delta > 5) and (mode is not PAUSE):
        mode = ROLLING
        roll_ttl = time.monotonic() + 3

    if (time.monotonic() >= roll_ttl) and (roll_ttl != 0) and (mode is ROLLING):
        mode = STATIC
        roll_ttl = 0

    # save the angle_total for next time
    pre_angle_total = angle_total

#STATIC
    #print(time.monotonic())

    if (mode is STATIC) and pre_mono <= time.monotonic():
        i+= 1

        pre_mono = time.monotonic() + 2
        print(i)
    if i >= 5 :
        i = 0
        print("zeroed")






    if mode is PAUSE:
        pixel_ring.fill((0,0,0,0))
        i = 0
        #pass
        time.sleep(0.1)
        print("pausing")
    elif mode is ROLLING:
        i = 0
        pixel_ring.fill(ENGRAM)
        print("brightness is: "  + str(round(angle_light_percent,2)) + " %")
        pixel_ring.brightness= round(angle_light_percent,2)
    elif mode is STATIC:
        pixel_ring.fill(color[i])
        #print(color[i])

    time.sleep(0.05)
