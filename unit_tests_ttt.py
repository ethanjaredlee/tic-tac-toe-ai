import unittest
from ticTacToe import winner, check_full, scoring, best_choice, best_choice_helper

class TicTacToeTests(unittest.TestCase):

    def test_winner(self):
        # no winner
        testBoard1 = ["x", "", "", "o", "o", "", "x", "x", "o"]
        self.assertEqual(winner(testBoard1), "no winner")

        # o wins
        testBoard2 = ["x", "", "", "o", "o", "o", "x", "x", "o"]
        self.assertEqual(winner(testBoard2), "o")

        testBoard3 = ["x", "", "o", "o", "o", " ", "x", "x", "x"]
        self.assertEqual(winner(testBoard3), "x")

    def test_scoring(self):

        testBoard1 = ["x", "x", "x", "", "", "", "", "", ""]
        self.assertEqual(scoring(testBoard1), -10)

    def test_best_choice(self):

        # one winning option left
        testBoard1 = ["x", "o", "x", "o", "o", "", "x", "x", "o"]
        self.assertEqual(best_choice(testBoard1), 5)
        ''' translates to:

        | x | x | o |
        | o | o | 5 | <-- this is the best choice: i = 5
        | x | o | x |

        '''

        # 2 options, one immediately wins
        testBoard2 = ["x", "", "x", "o", "o", "", "x", "x", "o"]
        self.assertEqual(best_choice(testBoard2), 5)
        ''' translates to:

        | x | x | o |
        | o | o | 5 | <-- this is the best choice: i = 5
        | x | 1 | x |

        '''

        # 3 options, one immediately wins
        testBoard3 = ["x", "", "", "o", "o", "", "x", "x", "o"]
        self.assertEqual(best_choice(testBoard3), 5)
        ''' translates to:

        | x | x | o |
        | o | o | 5 | <-- this is the best choice: i = 5
        | x | 1 | 2 |

        '''

        testBoard4 = ["x", "", "", "o", "o", "", "x", "x", ""]
        self.assertEqual(best_choice(testBoard4), 5)


if __name__ == '__main__':
    unittest.main()
