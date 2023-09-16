# В данной задаче использованы две парадигмы - структурная и процедурная. Процедурная - так как решение оформлено в виде фукций. Структурная - так как код внутри функции выполняется с использованием циклов.

# -*- coding: utf-8 -*-
from random import randint

game_board = list(range(1,10))
used_cell = []
user_choise = None


def start_game():
    global used_cell
    global game_board
    used_cell = []
    game_board = list(range(1,10))
    print(f"------------------- \n | {game_board[0]} | {game_board[1]} | {game_board[2]} | \n | {game_board[3]} | {game_board[4]} | {game_board[5]} | \n | {game_board[6]} | {game_board[7]} | {game_board[8]} | \n -------------------\n ")


def x_choise():
    global user_choise
    global game_board
    user_choise = int(input("Куда поставишь Х? Отправь номер клетки: "))
    check()
    if not (who_wins(game_board)):
        bot_turn()
        who_wins(game_board)

def check():
    global game_board
    global user_choise
    if user_choise not in used_cell:
        game_board[user_choise - 1] = "X"
        used_cell.append(user_choise)
        print(f"------------------- \n | {game_board[0]} | {game_board[1]} | {game_board[2]} | \n | {game_board[3]} | {game_board[4]} | {game_board[5]} | \n | {game_board[6]} | {game_board[7]} | {game_board[8]} | \n ------------------- ")
    else:
        print("Клетка занята")
        x_choise()

def bot_turn():
    valid = 0
    while valid == 0:
        bot_step = randint(1,9)
        if bot_step not in used_cell:
            game_board[bot_step - 1] = "O"
            used_cell.append(bot_step)
            valid = 1
            print(f"------------------- \n | {game_board[0]} | {game_board[1]} | {game_board[2]} | \n | {game_board[3]} | {game_board[4]} | {game_board[5]} | \n | {game_board[6]} | {game_board[7]} | {game_board[8]} | \n ------------------- ")
            x_choise()

def who_wins(game_board):
    win = False
    if len(used_cell) < 9:
        win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for i in win_coord:
            if game_board[i[0]] == game_board[i[1]] == game_board[i[2]]:
                print(f"Победил игрок {game_board[i[0]]}. Сыграем еще?")
                win = True
    elif len(used_cell) == 9:
        win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for i in win_coord:
            if game_board[i[0]] == game_board[i[1]] == game_board[i[2]]:
                print(f"Победил игрок {game_board[i[0]]}. Сыграем еще?")
                win = True
        if not win:
            print("Ничья. Сыграем еще?")
            exit
    return win

start_game()
x_choise()