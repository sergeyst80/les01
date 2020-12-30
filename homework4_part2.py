import os


def clear_screen():
    os.system(["clear", "cls"][os.name == "nt"])


def draw_board():
    clear_screen()
    print("\n {} | {} | {} \n".format(board[0], board[1], board[2])
          + "---+---+---\n"
          + " {} | {} | {} \n".format(board[3], board[4], board[5])
          + "---+---+---\n"
          + " {} | {} | {} \n".format(board[6], board[7], board[8]))


symbols = ["O", "X"]
current_player = False
game_repeat = True

while game_repeat:
    board = [str(i) for i in range(1, 10)]
    clear_screen()

    while True:
        inp = input("Выберите кто начинает игру (\"X\" или \"O\"): ")
        if inp.upper() in symbols:
            current_player = bool(symbols.index(inp.upper()))
            break

    draw_board()

    for step in range(9):
        print("Ход игрока \"{}\"".format(symbols[current_player]))

        while True:
            position = input("Введите номер ячейки: ")
            if position not in symbols and position in board:
                board[int(position)-1] = symbols[current_player]
                break

        draw_board()

        if (board[0] == board[1] == board[2]
                or board[3] == board[4] == board[5]
                or board[6] == board[7] == board[8]
                or board[0] == board[3] == board[6]
                or board[1] == board[4] == board[7]
                or board[2] == board[5] == board[8]
                or board[0] == board[4] == board[8]
                or board[6] == board[4] == board[2]):
            print("Ура!!! Победил игрок \"{}\"!!!".format(symbols[current_player]))
            break

        if step == 8:
            print("Ничья!")

        current_player = not current_player

    if not input("Начать новую игру? (\"Y\" - начать, любой другой символ - выход): ").upper() == "Y":
        game_repeat = False
