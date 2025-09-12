class Scoreboard():
    """Class defining the scoreboard"""

    def get_scores(self, number_of_scores : int) -> list[tuple[str, int, int]]:
        """Returns the best n scores"""
        ...
    
    def add_score(self, new_score : tuple[str, int, int]):
        """Adds a new score to the Scoreboard"""
        ...
    
    def reset_scoreboard(self):
        """Makes the scoreboard return to its original version"""
        ...