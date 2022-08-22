## Setup Block ##
import board
import time
import analogio

# declare a analogio object on board.A0 and board.A1
a1 = analogio.AnalogIn(board.A0)
a2 = analogio.AnalogIn(board.A1)

# loop forever
while True:
    ## input block ##
    # read a1 and a2 into variables
    a1_read = a1.value
    a2_read = a2.value

    ## output block ##
    print("Analog in 1 is:", a1_read)
    print("Analog in 2 is:", a2_read)
    print()

    time.sleep(0.01)
