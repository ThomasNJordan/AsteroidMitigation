import pyfirmata
import time

board = pyfirmata.Arduino('COMP4')

while True:
    board.digital[11].write(1)
    time.sleep(1)
    board.digital[11].write(0)
    time.sleep(1)
