# Clock module
from my_module import *
import clock_font
import time


# Make separator character as string list
def make_separator(sep, generator_item):
    if sep not in clock_font.print_table:
        sep = ':'

    if sep == '.':
        separator = clock_font.get_symbol_as_strings(' ')
        separator[int(generator_item)] = clock_font.W_BOX + clock_font.B_BOX + clock_font.W_BOX
    else:
        separator = clock_font.get_symbol_as_strings(' ' if (generator_item % 2) == 0 else sep) 
    
    return separator


# Print clock in terminal window
def print_clock(scale, sep):
    clock_display = []
    current_time = time.localtime()
    clock_display.append(clock_font.get_symbol_as_strings(current_time.tm_hour // 10))
    clock_display.append(clock_font.get_symbol_as_strings(current_time.tm_hour % 10))
    clock_display.append(sep)
    clock_display.append(clock_font.get_symbol_as_strings(current_time.tm_min // 10))
    clock_display.append(clock_font.get_symbol_as_strings(current_time.tm_min % 10))
    clock_display.append(sep)
    clock_display.append(clock_font.get_symbol_as_strings(current_time.tm_sec // 10))
    clock_display.append(clock_font.get_symbol_as_strings(current_time.tm_sec % 10))
    
    if scale > 1:
    
        for item in range(len(clock_display)):
            clock_display[item] = clock_font.scale_symbol(clock_display[item], scale)
    
    for item in range(len(clock_display[0])):
        print(clock_display[0][item] + clock_font.W_BOX + clock_display[1][item] +
            clock_font.W_BOX + clock_display[2][item] + clock_font.W_BOX +
            clock_display[3][item] + clock_font.W_BOX + clock_display[4][item] +
            clock_font.W_BOX + clock_display[5][item] + clock_font.W_BOX +
            clock_display[6][item] + clock_font.W_BOX + clock_display[7][item])


# Start clock
def start_clock(scale=1, sep=':', speed=1):

    if not 0 < speed <=10:
        speed = 1 
    
    if not 0 < scale <= 5:
        scale = 1
    
    divider = 0

    while True:
        
        if sep == '.':
            divider = len(clock_font.print_table[1])
            generator = bidirect_generator(divider)
        else:
            divider = 2
            generator = simple_generator(divider)

        for count in generator:
            clr_screen()
            print_clock(scale, make_separator(sep, count))
            time.sleep(2 / (divider * speed))


if __name__ == "__main__":
    print('Clock module')