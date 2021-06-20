def isOppPiece(game, x, y):
    if (game.turn == 'Green'):
        return (game.board[y][x].islower())
    return (game.board[y][x].isupper())

def isDiagonal(ox, oy, fx, fy):
    if (fx == ox + 1 or fx == ox - 1):
        if (fy == oy + 1 or fy == oy - 1):
            return True
    return False

# Pawn - Valid Move
def isValidMoveP(game):
    # Move from start position
    if (game.oy == 7 and 0 < game.oy-game.fy < 3):
        return True
    # Move forward 1 space
    elif (game.ox == game.fx and game.oy-game.fy == 1):
        return (not isOppPiece(game, game.fx, game.fy))
    # Attack diagonal piece
    if (game.fy < game.oy and isDiagonal(game.ox, game.oy, game.fx, game.fy) and isOppPiece(game, game.fx, game.fy)):
        print("{} takes {}'s Pawn!".format(game.turn, game.players[game.turn]))
        return True
    return False
    
# Bishop - Valid Move
def isValidMoveB(game):
    return False

# Knight - Valid Move
def isValidMoveKN(game):
    return False

# Rook - Valid Move
def isValidMoveR(game):
    return False

# King - Valid Move
def isValidMoveK(game):
    return False

# Queen - Valid Move
def isValidMoveQ(game):
    return False

def isValidMove(game):
    move = game.move
    if (len(move) == 5):
        # Convert move into int values
        ox = game.ox = ord(move[0].lower()) - 96      # Current x coordinate (a-h)
        oy = game.oy = int(move[1])                   # Current y coordinate (1-8)
        fx = game.fx = ord(move[3].lower()) - 96      # Final x coordinate (a-h)
        fy = game.fy = int(move[4])                   # Final y coordinate (1-8)
        
        # If going outside board / Position is not blank / Using opponent piece / Moving to same position
        if ("0" in move or game.board[oy][ox] == '' or isOppPiece(game, ox, oy) or (move[0] == move[3] and move[1] == move[4])):
            pass
        
        # Call respective piece move func if move has current format and valid positions
        elif (move[0].isalpha() and move[3].isalpha() and move[1].isdigit() and move[4].isdigit()):
            if (ox <= ord('h')-96 and fx <= ord('h')-96 and oy <= 8 and fy <= 8):
                if (eval("isValidMove" + game.board[oy][ox].upper())(game)):
                    return True
    
    print("Invalid move :(")
    return False
