# font definition

# Black box character
B_BOX = '\u2588\u2588'
# White space character
W_BOX = '  '
# White space character
MOVE_DOT = W_BOX + B_BOX + W_BOX

# Font table
print_table = {
    1: [W_BOX + B_BOX + W_BOX,
        B_BOX + B_BOX + W_BOX,
        W_BOX + B_BOX + W_BOX,
        W_BOX + B_BOX + W_BOX,
        B_BOX + B_BOX + B_BOX],

    2: [B_BOX + B_BOX + B_BOX,
        W_BOX + W_BOX + B_BOX,
        W_BOX + B_BOX + W_BOX,
        B_BOX + W_BOX + W_BOX,
        B_BOX + B_BOX + B_BOX],

    3: [B_BOX + B_BOX + B_BOX,
        W_BOX + W_BOX + B_BOX,
        B_BOX + B_BOX + B_BOX,
        W_BOX + W_BOX + B_BOX,
        B_BOX + B_BOX + B_BOX],

    4: [B_BOX + W_BOX + B_BOX,
        B_BOX + W_BOX + B_BOX,
        B_BOX + B_BOX + B_BOX,
        W_BOX + W_BOX + B_BOX,
        W_BOX + W_BOX + B_BOX],

    5: [B_BOX + B_BOX + B_BOX,
        B_BOX + W_BOX + W_BOX,
        B_BOX + B_BOX + B_BOX,
        W_BOX + W_BOX + B_BOX,
        B_BOX + B_BOX + B_BOX],

    6: [B_BOX + B_BOX + B_BOX,
        B_BOX + W_BOX + W_BOX,
        B_BOX + B_BOX + B_BOX,
        B_BOX + W_BOX + B_BOX,
        B_BOX + B_BOX + B_BOX],

    7: [B_BOX + B_BOX + B_BOX,
        W_BOX + W_BOX + B_BOX,
        W_BOX + B_BOX + W_BOX,
        B_BOX + W_BOX + W_BOX,
        B_BOX + W_BOX + W_BOX],

    8: [B_BOX + B_BOX + B_BOX,
        B_BOX + W_BOX + B_BOX,
        B_BOX + B_BOX + B_BOX,
        B_BOX + W_BOX + B_BOX,
        B_BOX + B_BOX + B_BOX],

    9: [B_BOX + B_BOX + B_BOX,
        B_BOX + W_BOX + B_BOX,
        B_BOX + B_BOX + B_BOX,
        W_BOX + W_BOX + B_BOX,
        B_BOX + B_BOX + B_BOX],

    0: [B_BOX + B_BOX + B_BOX,
        B_BOX + W_BOX + B_BOX,
        B_BOX + W_BOX + B_BOX,
        B_BOX + W_BOX + B_BOX,
        B_BOX + B_BOX + B_BOX],

    ':': [W_BOX + W_BOX + W_BOX,
          W_BOX + B_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX,
          W_BOX + B_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX],

    '-': [W_BOX + W_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX,
          W_BOX + B_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX],

    '.': [W_BOX + W_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX,
          W_BOX + B_BOX + W_BOX],

    '/': [W_BOX + W_BOX + W_BOX,
          W_BOX + W_BOX + B_BOX,
          W_BOX + B_BOX + W_BOX,
          B_BOX + W_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX],
          
    ' ': [W_BOX + W_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX,
          W_BOX + W_BOX + W_BOX]}


# Conversion character to a string list function
def get_symbol_as_strings(number_symbol):
    out_strings = []

    for symbol_row in print_table[number_symbol]:
        out_strings.append(''.join(symbol_row))

    return out_strings


# character scaling function
def scale_symbol(symbol, scale):
    new_symbol = []
        
    for elem in symbol:
        string = ''
    
        for i in elem:
            string += i*scale

        for count in range(scale):
            new_symbol.append(string)
   
    return new_symbol


if __name__ == "__main__":
    print('Clock font module')
