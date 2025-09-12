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
        original_lenght = len(self._scoreboard.get_scores(300))
        self._scoreboard.add_score(("Test", 100000, 1))
        self.assertEqual(original_lenght + 1, len(self._scoreboard.get_scores(300)))
        self._scoreboard.reset_scoreboard()
        self._scoreboard.add_score("Test")
        self.assertEqual(original_lenght, len(self._scoreboard.get_scores(300)))