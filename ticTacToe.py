'''

Quick notation:
    * 0 + n*2 stands for ai turn
    * 1 + n*2 stands for opponent turn

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
    copy = array[:]
    finalScores = [0] * 9

    for i in range(0,9):
        if copy[i] == "":
            copy[i] = "o"
            finalScores[i] = best_choice_helper(copy, 0, 1)
            print 'FINAL SCORE ' + str(finalScores[i]) + ' index: ' + str(i)
            copy[i] = ""

    for i in range(0,9):
        if array[i] != "":
            finalScores[i] = -1

    print finalScores
    return finalScores.index(max(finalScores))

def best_choice_helper(array, score, turn):
    # recurses and finds the score of each more in best_choice

    if check_full(array):
        #print 'score (full): ' + str(scoring(array) + score)
        #print 'I RETURNED THE RIGHT THING (full board)'
        return int(scoring(array) + score)

    if scoring(array) != 0:
        #print 'score (winner) ' + str(scoring(array) + score)
        #print 'I RETURNED THE RIGHT THING (early win)'
        return int(scoring(array) + score)

    copy = array[:]
    #print 'copy: ' + str(copy)
    savedTurn = turn

    # check whose turn it is
    if (savedTurn % 2 == 0): # ai turn

        for i in range(0,9):
            if copy[i] == "":
                #print 'ai turn: ' + str(i)
                copy[i] = "o"
                score = max([score, best_choice_helper(copy, score, turn + 1)])
                copy[i] = ""

    if (savedTurn % 2 == 1): # opponent turn
        for i in range(0,9):
            if copy[i] == "":
                #print 'opp turn: ' + str(i)
                copy[i] = "x"
                score = min([score, best_choice_helper(copy, score, turn + 1)])
                copy[i] = ""

    #print 'returned score: ' + str(scoring(array) + score)
    return scoring(array) + score



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

        if check_full(pieces) and scoring(pieces) == -10:
            print "player wins!"
            draw_board(pieces)
            break

        if check_full(pieces) and scoring(pieces) == 0:
            print "tie game!"
            draw_board(pieces)
            break

        draw_board(pieces)

        print 'hello ' + str(pieces)
        aiMove = best_choice(pieces)
        print 'why ' + str(aiMove)
        pieces[aiMove] = "o"

        if check_full(pieces) and scoring(pieces) == 10:
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
