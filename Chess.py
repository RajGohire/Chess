from Board import *
from Moves import *
from os import get_terminal_size, popen, system, name

class Game:
    def __init__(self, gameOver, checkers, players, turn, board, prevMove="", move="", ox=0, oy=0, fx=0, fy=0):
        self.gameOver = gameOver
        self.checkers = checkers
        self.players = players
        self.turn = turn
        self.board = board
        self.prevMove = prevMove
        self.move = move
        self.ox = ox
        self.oy = oy
        self.fx = fx
        self.fy = fy

def main():
    game = Game(False, False, {'Red': 'Green', 'Green': 'Red'}, 'Green', newBoard())
    print("[Enter q to exit game]")
    mode = ''#input("Do you want to play 2-players mode? (y/n) ")
    printBoard(game)
    while (not game.gameOver):
        game.move = input("Enter your next move (original-final): ")
        
        if (game.move == 'q'):
            game.gameOver = True
            continue
        
        if (isValidMove(game)):
            if (isOppPiece(game, game.fx, game.fy)):
                print("{} took {}'s piece!".format(game.turn, game.players[game.turn]))
            updateBoard(game)
            if (mode == 'y' and not game.gameOver):
                game.turn = game.players[game.turn]
                game.board = rotateBoard(game.board)
            
            # try:
            #     col, row = get_terminal_size()
            # except OSError:
            #     col, row = popen('stty size', 'r').read().split()
            # print("\n"*(int(col)-28))
            cls = lambda: system('cls' if name =='nt' else 'clear')
            cls()
            # os.system('clear')
            
            printBoard(game)
            game.prevMove = game.move
    
    print("################# Game Over! #################\n")
    exit()

if __name__ == '__main__':
    main()
