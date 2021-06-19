from board import isOppPiece

def isOppPiece(board, fx, fy):
    if (board[fy][fx].islower()):
        return True

def isDiagonal():
    pass

def isValidMoveP(board, move, ox, oy, fx, fy):
    # Move from start position
    if (oy == 7 and 0 < oy-fy < 3):
        print("is Valid")
        return True
    # Move forward 1 space
    elif (oy-fy == 1):
        print("is Valid")
        return True
    # Attack diagonal piece
    elif (isOppPiece(board, ox, oy, fx, fy)):
        pass
    
def isValidMoveB(move):
    pass
def isValidMoveKn(move):
    pass
def isValidMoveR(move):
    pass
def isValidMoveK(move):
    pass
def isValidMoveQ(move):
    pass

def isValidMove(board, move, ox, oy, fx, fy):
    valid = False
    if (len(move) == 5):
        if (move[0] == move[3] and move[1] == move[4]):
            return False
        for i in range (0, 5, 3):
            if (move[i].isalpha() and move[i+1].isdigit()):
                if (ord(move[i]) <= ord('h') and int(move[i+1]) <= 8):
                    valid = True
                else:
                    valid = False
    if (not valid):
        print("Invalid move:(")
    valid = isValidMoveP(board, move)
    return valid
