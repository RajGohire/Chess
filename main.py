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
    print("[Enter q to exit game]")
    mode = ''#input("Do you want to play 2-players mode? (y/n) ")
    printBoard(game)
    while (not game.gameOver):
        game.move = input("Enter your next move (original-final): ")
        
        if (game.move == 'q'):
            game.gameOver = True
            continue
        
        if (isValidMove(game)):
            updateBoard(game)
            if (mode == 'y' and not game.gameOver):
                game.turn = game.players[game.turn]
                game.board = rotateBoard(game.board)
            printBoard(game)
    
    print("################# Game Over! #################\n")
    exit()

if __name__ == '__main__':
    main()
