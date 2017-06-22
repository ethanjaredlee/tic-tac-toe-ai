'''

Quick notation:
    * 0 + n*2 stands for ai turn
    * 1 + n*2 stands for opponent turn

Future development:
    * don't let players choose a move that's already been taken
    * create a more graphical game -- not just playing in command line
    * simplify into a one-move helper
'''

#IMPROVE THIS
def winner(pieces):
    if (pieces[0] != "" and pieces[0] == pieces[3] and pieces[3] == pieces[6]):
        return pieces[0] # check horizontal
    if (pieces[1] != "" and pieces[1] == pieces[4] and pieces[4] == pieces[7]):
        return pieces[1]
    if (pieces[2] != "" and pieces[2] == pieces[5] and pieces[5] == pieces[8]):
        return pieces[2]
    if (pieces[0] != "" and pieces[0] == pieces[1] and pieces[1] == pieces[2]):
        return pieces[0]
    if (pieces[3] != "" and pieces[3] == pieces[4] and pieces[4] == pieces[5]):
        return pieces[3]
    if (pieces[6] != "" and pieces[6] == pieces[7] and pieces[7] == pieces[8]):
        return pieces[6]
    if (pieces[2] != "" and pieces[2] == pieces[4] and pieces[4] == pieces[6]):
        return pieces[2]
    if (pieces[0] != "" and pieces[0] == pieces[4] and pieces[4] == pieces[8]):
        return pieces[0]
    return "no winner"

def check_full(array):
    for element in array:
        if element == "":
            return False
    return True

def scoring(array):
    if winner(array) == 'o':
        return 10
    if winner(array) == 'x':
        return -10
    else:
        return 0

def best_choice(array):
# returns index of the best move

    scores = [-1000] * 9

    for i in range(0,9):
        if array[i] == "":
            array[i] = "o"
            scores[i] = best_choice_helper(array, 1)
            array[i] = ""

    return scores.index(max(scores))

def best_choice_helper(array, turn):
    # recurses and finds the score of each move in best_choice

    if check_full(array):
        return scoring(array)

    if scoring(array) != 0:
        return scoring(array)

    # check whose turn it is
    if (turn % 2 == 0): # ai turn

        score = -1000

        # checks every possible move
        for i in range(0,9):
            if array[i] == "":
                array[i] = "o"
                score = max(score, best_choice_helper(array, turn + 1))
                array[i] = ""

    if (turn % 2 == 1): # opponent turn

        score = 1000

        # checks every possible move
        for i in range(0,9):
            if array[i] == "":
                array[i] = "x"
                score = min(score, best_choice_helper(array, turn + 1))
                array[i] = ""

    return score

def findBestMove(board):
    bestVal = -1000
    bestSpot = -1
    for i in range(0,9):
        if board[i] == "":
            board[i] = "o"
            moveVal = best_choice_helper(board, 1)
            board[i] = ""

            if moveVal > bestVal:
                bestSpot = i
                bestVal = moveVal

    return bestSpot

def draw_board(pieces):

    copy = pieces[:]
    for i in range(0,9):
        if copy[i] == "":
            copy[i] = " "

    for i in range(0, 3):
        print "| " + copy[3*i] + " | " + copy[3*i+1] + " | " + copy [3*i+2] + " |"

def main():

    pieces = [""] * 9

    while True:

        draw_board(pieces)

        playerMove = int(raw_input("Enter a position: "))
        pieces[playerMove] = "x"

        if scoring(pieces) == -10:
            print "player wins!"
            draw_board(pieces)
            break

        if check_full(pieces) and scoring(pieces) == 0:
            print "tie game!"
            draw_board(pieces)
            break

        draw_board(pieces)

        aiMove = best_choice(pieces)
        pieces[aiMove] = "o"

        if scoring(pieces) == 10:
            print "ai wins!"
            draw_board(pieces)
            break

        if check_full(pieces) and scoring(pieces) == 0:
            print "tie game!"
            draw_board(pieces)
            break

        print pieces

if __name__ == '__main__':
    main()
