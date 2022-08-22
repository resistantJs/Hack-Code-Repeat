# do this forever
import board
import time
from digitalio import DigitalInOut, Direction, Pull
import pwmio

# create a pwmOut object at
pwm_led = pwmio.PWMOut(board.D5)

# create a variable to store a duty_cycle
# the value of the PWM duty_cycle is 16-bits long
# 16 bit values fall in the integer range of 1 to 65535

# we can also use exponents of 2 to set these values
# change the value of exponent here between 0 and 15 to set the pwm_dc below
exponent = 1

pwm_dc = 2 ** exponent

# do this forever
while True:

    # print the exponent pwm_dc value to see it in serial
    print(pwm_dc)
    # now set the pwm_led duty_cycle property to the pwm_dc value
    pwm_led.duty_cycle = pwm_dc

    # increment the exponent value with compound addition assignment
    exponent += 1

    # then use the modulo 15 of that value to set a new pwm_dc value
    pwm_dc = 2 ** (exponent % 16)
    print(pwm_dc)

    # sleep for a bit to keep the serial from acting weird
    time.sleep(0.1)
