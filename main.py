from board import *
from moves import *

def main():
    gameOver = False
    board = newBoard()
    printBoard(board)
    while (not gameOver):
        move = input("Enter your next move (original-final):")
        board = updateBoard(board, move)
        printBoard(board)

if __name__ == '__main__':
    main()
