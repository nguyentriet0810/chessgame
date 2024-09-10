##========================================================
##program by Nguyen Hoang Minh Ttriet - 21151176
##========================================================

"""
This class is responsible for starting the information about the current on a Chessgame.
This will also be responsible for determining the valid moves at the current state.
It will also keep a move log.
"""

##Create a class named GameState
class GameState():

    ##Function is always executed when the class is being initiated
    def __init__(self):

        ##This is a board game
        ##Board game have 8x8 2d list, each elemennt of the list has two charecters
        ##The first charecter represents the color of the piece "black" or "white"
        ##The second charecter represents the name of the piece "Rook", "kNight", "Bishop", "Queen", "King" or "Pawn"
        self.board = [  ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                        ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                        ["==", "==", "==", "==", "==", "==", "==", "=="],
                        ["==", "==", "==", "==", "==", "==", "==", "=="],
                        ["==", "==", "==", "==", "==", "==", "==", "=="],
                        ["==", "==", "==", "==", "==", "==", "==", "=="],
                        ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]    ]
        
        ##The rules white alway the first play 
        self.whiteToMove = True
        
        ##
        self.movelog = []
        