from colorama import Fore, Back, Style

def newBoard():
    board = [['', '', '', '', '', '', '', '', '', ''],
            ['', 'R ', 'KN', 'B ', 'Q ', 'K ', 'B ', 'KN', 'R ', ''],
            ['', 'P ', 'P ', 'P ', 'P ', 'P ', 'P ', 'P ', 'P ', ''],
            ['', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', ''],
            ['', 'p ', 'p ', 'p ', 'p ', 'p ', 'p ', 'p ', 'p ', ''],
            ['', 'r ', 'kn', 'b ', 'q ', 'k ', 'b ', 'kn', 'r ', ''],
            ['', '', '', '', '', '', '', '', '', '']]
    return board

def printBoard(game):
    print("\n---------------------------------------------")
    print("{} player's turn!".format(game.turn))
    print("---------------------------------------------\n" \
        + "    +----+----+----+----+----+----+----+----+")
    for x in range (8,0,-1):
        print(x, end = "   | ")
        for y in range (1,9):
            if (game.board[x][y] == ''):
                if (game.checkers and abs(x-y) % 2 == 0):
                    print(f'{Back.LIGHTBLACK_EX}  {Style.RESET_ALL}' + ' | ', end = "")
                else:
                    print('   | ', end = "")
                continue
            if (game.board[x][y].isupper()):
                if (game.checkers and abs(x-y) % 2 == 0):
                    print(f'{Fore.GREEN}{Back.LIGHTBLACK_EX}{game.board[x][y]}{Style.RESET_ALL} | ', end = "")
                else:
                    print(f'{Fore.GREEN}{game.board[x][y]}{Style.RESET_ALL} | ', end = "")
            else:
                if (game.checkers and abs(x-y) % 2 == 0):
                    print(f'{Fore.RED}{Back.LIGHTBLACK_EX}{game.board[x][y]}{Style.RESET_ALL} | ', end = "")
                else:
                    print(f'{Fore.RED}{game.board[x][y]}{Style.RESET_ALL} | ', end = "")
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
    
    # Pawn Promotion
    if (game.fy == 8 and game.board[game.fy][game.fx].lower() == 'p '):
        new = ''
        while (new not in ['Q', 'R', 'B', 'KN']):
            new = input("Choose what the pawn should promoted to? (Q/R/B/KN): ").upper()
        if game.turn == 'Green':
            game.board[game.fy][game.fx] = new.upper() + ' '
        else:
            game.board[game.fy][game.fx] = new.lower() + ' '

def rotateBoard(board):
    tempBoard = newBoard()
    for x in range (10):
        for y in range (10):
            tempBoard[x][y] = board[9-x][9-y]
    return tempBoard
