import os

clear_board = """
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
"""
clr_str = ["clear", "cls"][os.name == "nt"]
symbols = ["O", "X"]
current_player = False
game_repeat = True

while game_repeat:
    board = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    os.system(clr_str)

    while True:
        inp = input("Выберите кто начинает игру (\"X\" или \"O\"): ")
        if inp.upper() in symbols:
            current_player = bool(symbols.index(inp.upper()))
            break

    os.system(clr_str)
    print(clear_board)

    for step in range(9):
        print("Ход игрока \"{}\"".format(symbols[current_player]))

        while True:
            position = input("Введите номер ячейки: ")
            if len(position) == 1 and "0" < position <= "9":
                if type(board[position]) == int:
                    board[position] = symbols[current_player]
                    break

        os.system(clr_str)
        print("\n {} | {} | {} \n".format(board['1'], board['2'], board['3'])
              + "---+---+---\n"
              + " {} | {} | {} \n".format(board['4'], board['5'], board['6'])
              + "---+---+---\n"
              + " {} | {} | {} \n".format(board['7'], board['8'], board['9']))

        if (board['1'] == board['2'] == board['3']
                or board['4'] == board['5'] == board['6']
                or board['7'] == board['8'] == board['9']
                or board['1'] == board['4'] == board['7']
                or board['2'] == board['5'] == board['8']
                or board['3'] == board['6'] == board['9']
                or board['1'] == board['5'] == board['9']
                or board['7'] == board['5'] == board['3']):
            print("Ура!!! Победил игрок \"{}\"!!!".format(symbols[current_player]))
            break
        if step == 8:
            print("Ничья!")

        current_player = not current_player

    if not input("Начать новую игру? (\"Y\" - начать, любой другой символ - выход): ").upper() == "Y":
        game_repeat = False
