from colorama import Fore, Style

def newBoard():
    board = [['', '', '', '', '', '', '', '', '', ''],
            ['', 'r ', 'kn', 'b ', 'q ', 'k ', 'b ', 'kn', 'r ', ''],
            ['', 'p ', 'p ', 'p ', 'p ', 'p ', 'p ', 'p ', 'p ', ''],
            ['', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', ''],
            ['', 'P ', 'P ', 'P ', 'P ', 'P ', 'P ', 'P ', 'P ', ''],
            ['', 'R ', 'KN', 'B ', 'Q ', 'K ', 'B ', 'KN', 'R ', ''],
            ['', '', '', '', '', '', '', '', '', '']]
    return board

def printBoard(game):
    print("\n---------------------------------------------")
    print("{} player's turn!".format(game.turn))
    print("---------------------------------------------\n" \
        + "    +----+----+----+----+----+----+----+----+")
    for x in range (1,9):
        print(x, end = "   | ")
        for y in range (1,9):
            if (game.board[x][y] == ''):
                print('   | ', end = "")
                continue
            if (game.board[x][y].isupper()):
                print(f'{Fore.GREEN}{game.board[x][y]}{Style.RESET_ALL}' + ' | ', end = "")
            else:
                print(f'{Fore.RED}{game.board[x][y]}{Style.RESET_ALL}' + ' | ', end = "")
        print("\n    +----+----+----+----+----+----+----+----+")
    print()

    for j in range (8):
        if (j == 0):
           print("{0:6s}".format(""), end="")
        print(chr(97 + j), end="{:4s}".format(""))  # Use ord() for char to int
    print("\n")

def updateBoard(game):
    if (game.board[game.fy][game.fx].lower().strip() == 'k'):
        game.gameOver = True
    game.board[game.fy][game.fx] = game.board[game.oy][game.ox]
    game.board[game.oy][game.ox] = ''

def rotateBoard(board):
    tempBoard = newBoard()
    for x in range (10):
        for y in range (10):
            tempBoard[x][y] = board[9-x][9-y]
    return tempBoard
