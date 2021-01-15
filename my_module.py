import os


# Clear terminal window function
def clr_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    print('My functions module')
