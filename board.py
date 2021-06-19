from colorama import Fore, Style
from moves import isValidMove

def newBoard():
    board = [['','', '', '', '', '', '', '', ''],
            ['','r ', 'kn', 'b ', 'k ', 'q ', 'b ', 'kn', 'r '],
            ['','p ', 'p ', 'p ', 'p ', 'p ', 'p ', 'p ', 'p '],
            ['','', '', '', '', '', '', '', ''],
            ['','', '', '', '', '', '', '', ''],
            ['','', '', '', '', '', '', '', ''],
            ['','', '', '', '', '', '', '', ''],
            ['','P ', 'P ', 'P ', 'P ', 'P ', 'P ', 'P ', 'P '],
            ['','R ', 'KN', 'B ', 'K ', 'Q ', 'B ', 'KN', 'R '],]
    return board

def printBoard(board):
    print("\n---------------------------------------------")
    for x in range (1,9):
        print(x, end = "\t")
        for y in range (1,9):
            if (board[x][y] == ''):
                print('_', end = "{:4s}".format(""))
                continue
            if (board[x][y].isupper()):
                print(f'{Fore.GREEN}{board[x][y]}{Style.RESET_ALL}', end = "{:3s}".format(""))
            else:
                print(f'{Fore.RED}{board[x][y]}{Style.RESET_ALL}', end = "{:3s}".format(""))
        print("\n")
    
    for j in range (8):
        if (j == 0):
           print("", end="\t")
        print(chr(97 + j), end="{:4s}".format(""))  # Use ord() for char to int
    
    print("\n")

def updateBoard(board, move):
    ox = ord(move[0].lower()) - 96
    oy = int(move[1])
    fx = ord(move[3].lower()) - 96
    fy = int(move[4])
    if (isValidMove(board, move, ox, oy, fx, fy)):
        board[fy][fx] = board[oy][ox]
        board[oy][ox] = ''
    return board
