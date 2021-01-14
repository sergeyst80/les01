import os


# Clear terminal window function
def clr_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Simple generator function. Generate sequence (0, 1, ... , val-1)
def simple_generator(val):
    out = 0
    while out < val:    
        yield out
        out += 1


# Bidirectional generator function. Generate sequence (val-1, ... , 1, 0, 1, ... , val-1)
def bidirect_generator(val):
    temp = val
    while val > 0:
       val -= 1
       yield val
        
    while val < temp:
        yield val
        val += 1


if __name__ == "__main__":
    print('My functions module')
