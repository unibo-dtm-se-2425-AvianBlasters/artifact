import unittest
from Avian_Blasters.menu.scoreboard_impl import ScoreboardImpl

class TestScoreboard(unittest.TestCase):

    def setUp(self):
        self._scoreboard = ScoreboardImpl()
        self._scoreboard.reset_scoreboard()

    def test_get_scores(self):
        scores = self._scoreboard.get_scores(15)
        i = 0
        self.assertIsNotNone(scores[i])
        while i < len(scores):
            self.assertIsNotNone(scores[i])
            i += 1
    
    def test_wrong_request(self):
         with self.assertRaises(ValueError):
            self._scoreboard.get_scores("Ciao")
    
    def test_add(self):
        # Test addition of scores and handling of wrong requests
        original_lenght = len(self._scoreboard.get_scores(300))
        self._scoreboard.add_score(("Test", 100000, 1))
        self.assertEqual(original_lenght + 1, len(self._scoreboard.get_scores(300)))
        self._scoreboard.reset_scoreboard()
        with self.assertRaises(Exception):
            self._scoreboard.add_score("Test")
        with self.assertRaises(Exception):
            self._scoreboard.add_score(("Test", "Test", "Test"))
        with self.assertRaises(Exception):
            self._scoreboard.add_score((1, 2, "Test"))
        self.assertEqual(original_lenght, len(self._scoreboard.get_scores(300)))