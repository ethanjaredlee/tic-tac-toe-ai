class Space():
    # Spaces on a board
    def __init__(self, i):
        self.visited = 'no'
        self.numb = i


    def select(self, player):
        self.visited = player

def draw_board():
    pieces = [Space(i) for i in range(0,9)]
    for piece in pieces:
        print piece.visited, piece.numb

draw_board()
