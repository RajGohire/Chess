from board import *
from moves import *

class Game:
    def __init__(self, gameOver, players, turn, board, move="", ox=0, oy=0, fx=0, fy=0):
        self.gameOver = gameOver
        self.players = players
        self.turn = turn
        self.board = board
        self.move = move
        self.ox = ox
        self.oy = oy
        self.fx = fx
        self.fy = fy

def main():
    game = Game(False, {'Red': 'Green', 'Green': 'Red'}, 'Green', newBoard())
    printBoard(game)
    while (not game.gameOver):
        game.move = input("Enter your next move (original-final):")
        if (isValidMove(game)):
            updateBoard(game)
            game.turn = game.players[game.turn]
            game.board = rotateBoard(game.board)
            printBoard(game)

if __name__ == '__main__':
    main()
