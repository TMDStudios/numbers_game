import unittest
import numbers_game

class TestNumbersGame(unittest.TestCase):

    def test_answer(self):
        # Make sure that the answer is a number between 0 and 10
        self.assertTrue(0 <= numbers_game.answer <= 10)

    def test_counter(self):
        # Make sure the count is between 0 and 3
        self.assertTrue(0 <= numbers_game.count <= 3)

    def test_guess_value(self):
        # Make sure user only enters numbers
        self.assertRaises(ValueError, numbers_game.guess)