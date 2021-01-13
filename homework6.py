# Home work 6

import clock
import time
import os

def clr_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
     
toggle = True

while True:
    clr_screen()
    if toggle:
        sep = ':'
    else:
        sep = ' '
    clock.print_clock(2, sep)
    time.sleep(1)
    toggle = not toggle
