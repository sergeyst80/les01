# font definition
B_BOX = '\u2588\u2588'
W_BOX = '  '

print_table = {
    1: [[W_BOX, B_BOX, W_BOX],
        [B_BOX, B_BOX, W_BOX],
        [W_BOX, B_BOX, W_BOX],
        [W_BOX, B_BOX, W_BOX],
        [B_BOX, B_BOX, B_BOX]], 
    2: [[B_BOX, B_BOX, B_BOX],
        [W_BOX, W_BOX, B_BOX],
        [W_BOX, B_BOX, W_BOX],
        [B_BOX, W_BOX, W_BOX],
        [B_BOX, B_BOX, B_BOX]],
    3: [[B_BOX, B_BOX, B_BOX],
        [W_BOX, W_BOX, B_BOX],
        [B_BOX, B_BOX, B_BOX],
        [W_BOX, W_BOX, B_BOX],
        [B_BOX, B_BOX, B_BOX]],
    4: [[B_BOX, W_BOX, B_BOX],
        [B_BOX, W_BOX, B_BOX],
        [B_BOX, B_BOX, B_BOX],
        [W_BOX, W_BOX, B_BOX],
        [W_BOX, W_BOX, B_BOX]],
    5: [[B_BOX, B_BOX, B_BOX],
        [B_BOX, W_BOX, W_BOX],
        [B_BOX, B_BOX, B_BOX],
        [W_BOX, W_BOX, B_BOX],
        [B_BOX, B_BOX, B_BOX]],
    6: [[B_BOX, B_BOX, B_BOX],
        [B_BOX, W_BOX, W_BOX],
        [B_BOX, B_BOX, B_BOX],
        [B_BOX, W_BOX, B_BOX],
        [B_BOX, B_BOX, B_BOX]],
    7: [[B_BOX, B_BOX, B_BOX],
        [W_BOX, W_BOX, B_BOX],
        [W_BOX, B_BOX, W_BOX],
        [B_BOX, W_BOX, W_BOX],
        [B_BOX, W_BOX, W_BOX]],
    8: [[B_BOX, B_BOX, B_BOX],
        [B_BOX, W_BOX, B_BOX],
        [B_BOX, B_BOX, B_BOX],
        [B_BOX, W_BOX, B_BOX],
        [B_BOX, B_BOX, B_BOX]],
    9: [[B_BOX, B_BOX, B_BOX],
        [B_BOX, W_BOX, B_BOX],
        [B_BOX, B_BOX, B_BOX],
        [W_BOX, W_BOX, B_BOX],
        [B_BOX, B_BOX, B_BOX]],
    0: [[B_BOX, B_BOX, B_BOX],
        [B_BOX, W_BOX, B_BOX],
        [B_BOX, W_BOX, B_BOX],
        [B_BOX, W_BOX, B_BOX],
        [B_BOX, B_BOX, B_BOX]],
    ':': [[W_BOX, W_BOX, W_BOX],
          [W_BOX, B_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX],
          [W_BOX, B_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX]],
    '-': [[W_BOX, W_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX],
          [W_BOX, B_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX]],
    '.': [[W_BOX, W_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX],
          [W_BOX, B_BOX, W_BOX]],
    ' ': [[W_BOX, W_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX],
          [W_BOX, W_BOX, W_BOX]]}


# symbol convertion function
# input data:
#   number - numbers (0..9) and symbols (':', '-', '.')
#   scale - scaling factor (1..5)
# output data: list of strings
def get_symbol_as_strings(number_symbol, scale):
    out_strings = []

    for symbol_row in print_table[number_symbol]:
        string = ''

        for elem in symbol_row:
            string += elem*scale

        for count in range(scale):
            out_strings.append(string)

    return out_strings
