# Clock module

import clock_font
import time


def print_clock(scale=1, sep=':'):
    if not 0 < scale <= 5:
        scale = 1

    current_time = time.localtime()
    hour_h = clock_font.get_symbol_as_strings(current_time.tm_hour // 10, scale)
    hour_l = clock_font.get_symbol_as_strings(current_time.tm_hour % 10, scale)
    minute_h = clock_font.get_symbol_as_strings(current_time.tm_min // 10, scale)
    minute_l = clock_font.get_symbol_as_strings(current_time.tm_min % 10, scale)
    second_h = clock_font.get_symbol_as_strings(current_time.tm_sec // 10, scale)
    second_l = clock_font.get_symbol_as_strings(current_time.tm_sec % 10, scale)
    
    if sep not in clock_font.print_table:
        sep = ':'
    separator = clock_font.get_symbol_as_strings(sep, scale)

    for item in range(len(hour_h)):
        print(hour_h[item] + '  ' + hour_l[item] + separator[item] +
              minute_h[item] + '  ' + minute_l[item] + separator[item] +
              second_h[item] + '  ' + second_l[item])


if __name__ == "__main__":
    # print_number(1, 1)
    # print()
    # print_number(2, 2)
    pass