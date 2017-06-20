'''

Quick notation:
    * 0 + n*2 stands for ai turn
    * 1 + n*2 stands for opponent turn

'''

#IMPROVE THIS
def winner(pieces):
    if (pieces[0] != "" && pieces[0] == pieces[3] && pieces[3] == pieces[6]):
        return pieces[0] # check horizontal
    if (pieces[1] != "" && pieces[1] == pieces[4] && pieces[4] == pieces[7]):
        return pieces[1]
    if (pieces[2] != "" && pieces[2] == pieces[5] && pieces[5] == pieces[8]):
        return pieces[2]
    if (pieces[0] != "" && pieces[0] == pieces[1] && pieces[1] == pieces[2]):
        return pieces[0]
    if (pieces[3] != "" && pieces[3] == pieces[4] && pieces[4] == pieces[5]):
        return pieces[3]
    if (pieces[6] != "" && pieces[6] == pieces[7] && pieces[7] == pieces[8]):
        return pieces[6]
    if (pieces[2] != "" && pieces[2] == pieces[4] && pieces[4] == pieces[6]):
        return pieces[2]
    if (pieces[0] != "" && pieces[0] == pieces[4] && pieces[4] == pieces[8]):
        return pieces[0]
    return "no winner"

def scoring(array):
    if winner(array) == 'ai':
        return 10
    if winner(array) == 'opponent':
        return -10
    else:
        return 0


def best_choice(array):
    finalScores = best_choice_helper(array, [0] * 9, 0)
    return finalScores.index(max(finalScores))

def best_choice_helper(array, scores, turn):
    # recurses and finds the scores of all possible options
    copy = array[:]
    empty = False

    # check whose turn it is
    if (turn % 2 == 0): # ai turn

        for i in range(0,9):
            if copy[i] == "":
                copy[i] = "o"
                scores[i] = scores[i] + scoring(copy)
                best_choice(copy, scores, turn + 1)
                copy[i] = ""
                empty = True

    if (turn % 2 == 1): # opponent turn
        for i in range(0,9):
            if copy[i] == "":
                copy[i] = "x"
                scores[i] = scores[i] + scoring(copy)
                best_choice(copy, scores, turn + 1)
                copy[i] = ""
                empty = True

    if not empty:
        return scores

best_choice(["x", "", "", ])

def draw_board():
    pieces = ["" for i in range(0,9)]
