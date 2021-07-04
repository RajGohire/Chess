def isOppPiece(game, x, y):
    if (game.turn == 'Green'):
        return (game.board[y][x].islower())
    return (game.board[y][x].isupper())

def isDiagonal(ox, oy, fx, fy):
    return (abs(fx-ox) == abs(fy-oy))

# Pawn - Valid Move
def isValidMoveP(game):
    # Move from start position
    if (game.oy == 2 and 0 < game.fy-game.oy < 3):
        return True
    # Move forward 1 space
    elif (game.ox == game.fx and game.fy-game.oy == 1):
        return (not isOppPiece(game, game.fx, game.fy))
    # Attack diagonal piece
    elif (isOppPiece(game, game.fx, game.fy) and game.fy > game.oy \
        and game.fy - game.oy == 1 and isDiagonal(game.ox, game.oy, game.fx, game.fy)):
        return True
    # En passant
    if (game.prevMove != ""):
        pox = 9 - (ord(game.prevMove[0].lower()) - 96)  # Current x coordinate (a-h)
        poy = 9 - int(game.prevMove[1])                 # Current y coordinate (1-8)
        pfx = 9 - (ord(game.prevMove[3].lower()) - 96)  # Final x coordinate (a-h)  
        pfy = 9 - int(game.prevMove[4])                 # Final y coordinate (1-8)  
        if (game.fy > game.oy and game.fy - game.oy == 1 \
            and isOppPiece(game, pfx, pfy) and game.board[pfy][pfx].lower() == 'p ' \
            and poy - pfy == 2 and game.oy == pfy and game.fx == pfx \
            and isDiagonal(game.ox, game.oy, game.fx, game.fy)):
            game.board[pfy][pfx] = '  '
            return True
    return False
    
# Bishop - Valid Move
def isValidMoveB(game):
    if (isDiagonal(game.ox, game.oy, game.fx, game.fy)):
        i = game.ox
        j = game.oy
        if (game.fx < game.ox): i -= 1
        elif (game.fx > game.ox): i += 1
        if (game.fy < game.oy): j -= 1
        elif (game.fy > game.oy): j += 1
        
        while (i != game.fx and j != game.fy):
            if (game.board[j][i] != ''):
                return False
            if (game.fx < game.ox): i -= 1
            elif (game.fx > game.ox): i += 1
            if (game.fy < game.oy): j -= 1
            elif (game.fy > game.oy): j += 1
        return True
    return False

# Knight - Valid Move
def isValidMoveKN(game):
    return ((abs(game.fx - game.ox) == 1 and abs(game.fy - game.oy) == 2) \
        or (abs(game.fx - game.ox) == 2 and abs(game.fy - game.oy) == 1))

# Rook - Valid Move
def isValidMoveR(game):
    # Move Horizontally
    if (game.oy - game.fy == 0):
        for i in range (game.ox-1, game.fx, -1):
            if (game.board[game.oy][i] != ''):
                return False
        return True
    
    # Move Vertically
    elif (game.ox - game.fx == 0):
        if game.oy > game.fy:
            for i in range (game.oy-1, game.fy, -1):
                if (game.board[i][game.ox] != ''):
                    return False
        elif (game.oy < game.fy):
            for i in range (game.oy+1, game.fy):
                if (game.board[i][game.ox] != ''):
                    return False
        return True
    return False

# King - Valid Move
def isValidMoveK(game):
    # Move Horizontally (1 space)
    if (abs(game.ox-game.fx) == 1):
        # Move Diagonnaly (1 space)
        if (abs(game.oy-game.fy) == 1):
            return True
        else:
            return True
    # Move Vertically (1 space)
    elif (abs(game.oy-game.fy) == 1):
        return True
    return False

# Queen - Valid Move
def isValidMoveQ(game):
    return (isValidMoveR(game) or isValidMoveB(game))

def isValidMove(game):
    move = game.move
    if (len(move) == 5):
        # Call respective piece move func if move has current format and valid positions
        if (move[0].isalpha() and move[3].isalpha() \
            and move[1].isdigit() and move[4].isdigit()):
            # Convert move into int values
            ox = game.ox = ord(move[0].lower()) - 96      # Current x coordinate (a-h)
            oy = game.oy = int(move[1])                   # Current y coordinate (1-8)
            fx = game.fx = ord(move[3].lower()) - 96      # Final x coordinate (a-h)
            fy = game.fy = int(move[4])                   # Final y coordinate (1-8)
            
            # If going outside board / Current position is not blank /
            # Using opponent piece / Moving to same position
            if not all (0 < i < 9 for i in [ox, oy, fx, fy]):
                pass
            elif (game.board[oy][ox] == '' or isOppPiece(game, ox, oy) \
                or (move[0] == move[3] and move[1] == move[4])):
                pass            
            else:
                # Move if space is empty or opponent
                if(game.board[fy][fx] == '' or isOppPiece(game, fx, fy)):
                    if (eval("isValidMove" + game.board[oy][ox].upper())(game)):
                        return True
    
    print("Invalid move :(")
    return False
