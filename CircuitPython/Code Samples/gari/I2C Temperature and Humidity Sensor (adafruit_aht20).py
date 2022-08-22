## Setup Block ##
import time
import board
import adafruit_ahtx0

# create an I2C() object
i2c = board.I2C()

# cretae an object for the aht20 sensor
aht20 = adafruit_ahtx0.AHTx0(i2c)

# loop forever
while True:
    ## Input Block ##
    this_temp = aht20.temperature
    this_hum = aht20.humidity

    ## Ouput Block ##
    # print the values
    print('Temperature is:', this_temp)
    print('Humidity is:', this_hum)
    # print as a tuple for serial plotter
    print((this_temp, this_hum,))
    print()

    time.sleep(0.01)
