import unittest
import Zrandomgame

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = Zrandomgame.run_guess(answer, guess)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest