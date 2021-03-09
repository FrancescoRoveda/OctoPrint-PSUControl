import pyfirmata
from pyfirmata import OUTPUT

board = pyfirmata.Arduino('/dev/ttyUSB1')
board.digital[3].mode = OUTPUT
board.digital[4].mode = OUTPUT
board.digital[5].mode = OUTPUT
board.digital[6].mode = OUTPUT

print("Turning Everything off")
board.digital[3].write(0)
time.sleep(1)
board.digital[4].write(0)
time.sleep(1)
board.digital[5].write(0)
time.sleep(1)
board.digital[6].write(0)
time.sleep(10)
print("Turning Everything on")
board.digital[3].write(1)
time.sleep(1)
board.digital[4].write(1)
time.sleep(1)
board.digital[5].write(1)
time.sleep(1)
board.digital[6].write(1)