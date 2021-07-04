# Chess (Single or 2-players)

    [Enter q to exit game]
    
    ---------------------------------------------  
    Green player's turn!
    ---------------------------------------------  
        +----+----+----+----+----+----+----+----+  
    8   | r  | kn | b  | q  | k  | b  | kn | r  |  
        +----+----+----+----+----+----+----+----+  
    7   | p  | p  | p  | p  | p  | p  | p  | p  |  
        +----+----+----+----+----+----+----+----+  
    6   |    |    |    |    |    |    |    |    |  
        +----+----+----+----+----+----+----+----+  
    5   |    |    |    |    |    |    |    |    |  
        +----+----+----+----+----+----+----+----+  
    4   |    |    |    |    |    |    |    |    |  
        +----+----+----+----+----+----+----+----+  
    3   |    |    |    |    |    |    |    |    |  
        +----+----+----+----+----+----+----+----+  
    2   | P  | P  | P  | P  | P  | P  | P  | P  |  
        +----+----+----+----+----+----+----+----+  
    1   | R  | KN | B  | Q  | K  | B  | KN | R  |  
        +----+----+----+----+----+----+----+----+  
    
          a    b    c    d    e    f    g    h     
    
    Enter your next move (original-final):

# How to Run:
- Go to source root
    
        $(base)/Chess> python Chess.py

- To play game input moves in the format (Example: Move the pawn forward two ranks)

        e2 e4

    OR

        e2-e4

# Features in game:
- Single-player mode (No AI)
- Two-player mode (Rotating board)
- Toggle checkers for board
- Quit game ('Q')
- Basic movement
- En passant
- Pawn promotion

# Pending tasks:
- AI for Single player mode
- Castles
- Check/CheckMate
- Resigning
- Dead Position
- Draws
- Flag-fall
- Button GUI

# Future additional features:
- Timer
- Improved AI
- Highlight button with valid moves