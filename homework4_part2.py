import os

clear_board = """
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
"""

board = [1,2,3,4,5,6,7,8,9]
symbols = ["O", "X"]
current_player = False

os.system(["clear","cls"][os.name=="nt"])

while True:
    inp = input("Выберите кто начинает игру ('X' или 'O'): ")
    if inp.upper() in symbols:
        current_player = bool(symbols.index(inp.upper()))
        break

os.system(["clear","cls"][os.name=="nt"])
print(clear_board)

for step in range(9):
    print("Ход игрока \"{}\"".format(symbols[current_player]))

    while True:
        inp = input("Введите номер ячейки: ")
        if len(inp) == 1 and inp > "0" and inp <= "9":
            position = int(inp) - 1
            if type(board[position]) == int:
                board[position] = symbols[current_player]
                break

    os.system(["clear","cls"][os.name=="nt"])
    print("\n {} | {} | {} \n".format(board[0], board[1], board[2])
         +"---+---+---\n"
         +" {} | {} | {} \n".format(board[3], board[4], board[5])
         +"---+---+---\n"
         +" {} | {} | {} \n".format(board[6], board[7], board[8]))

    if (board[0]==board[1]==board[2]
     or board[3]==board[4]==board[5]
     or board[6]==board[7]==board[8]
     or board[0]==board[3]==board[6]
     or board[1]==board[4]==board[7]
     or board[2]==board[5]==board[8]
     or board[0]==board[4]==board[8]
     or board[6]==board[4]==board[2]):
        print("Ура!!! Победил игрок \"{}\"!!!".format(symbols[current_player]))
        break
    if step == 8:
        print("Ничья!")

    current_player = not current_player