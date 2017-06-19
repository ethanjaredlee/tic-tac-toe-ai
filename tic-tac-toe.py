class Space():
    # Spaces on a board
    def __init__(self, i):
        self.visited = ""


    def select(self, player):
        self.visited = player

#FIX THIS
def winner(pieces):
    if ((pieces[0] != "" && pieces[0] == pieces[3] && pieces[3] == pieces[6]) || # check horizontal
        (pieces[1] != "" && pieces[1] == pieces[4] && pieces[4] == pieces[7]) ||
        (pieces[2] != "" && pieces[2] == pieces[5] && pieces[5] == pieces[8]) ||
        (pieces[0] != "" && pieces[0] == pieces[1] && pieces[1] == pieces[2]) || # check vertical
        (pieces[3] != "" && pieces[3] == pieces[4] && pieces[4] == pieces[5]) ||
        (pieces[6] != "" && pieces[6] == pieces[7] && pieces[7] == pieces[8]) ||
        (pieces[2] != "" && pieces[2] == pieces[4] && pieces[4] == pieces[6]) || # check diagonal
        (pieces[0] != "" && pieces[0] == pieces[4] && pieces[4] == pieces[8]))



def draw_board():
    pieces = [Space() for i in range(0,9)]

draw_board()

def ai_helper(spot, score):
    if winner(spot) == 'ai':
        return score + 1
    if winner(spot) == 'opponent':
        return score - 1
    for piece in spot:
        if piece.visited = "":
            ai_helper()
