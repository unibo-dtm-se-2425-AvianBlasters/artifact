from Avian_Blasters.menu.scoreboard import Scoreboard
import os

class ScoreboardImpl(Scoreboard):
    """The main implementation of scoreboard"""

    def __init__(self):
        current_dir = os.path.dirname(__file__)
        self._file_path = os.path.join(current_dir, '..', '..', 'assets', 'scoreboard.txt')

    def get_scores(self, number_of_scores : int) -> list[tuple[str, int, str]]:
        self.__check_if_scoreboard_exists()
        
        with open(self._file_path, 'r') as file:
            lines = file.readlines()
        
        file.close()
        
        scoreboard : list[tuple[str, int, int]] = []

        if not isinstance(number_of_scores, int):
            raise ValueError("A number of scores must be set!")
        
        for line in lines[1 : number_of_scores + 1]:
            name, points, difficulty = line.replace('\n', '').split(',')
            scoreboard.append([name, int(points), difficulty])

        return scoreboard
    
    def add_score(self, new_score : tuple[str, int, int]):
        if not (isinstance(new_score[0], str) and isinstance(new_score[1], int) and (isinstance(new_score[2], int))):
            raise Exception("Score won't be stored, as the new score is not set up correctly!")
        
        self.__check_if_scoreboard_exists()
        
        scoreboard : list[tuple[str, int, int]] = []
        scoreboard = self.get_scores(300)

        scoreboard.append(new_score)
        scoreboard.sort(key = lambda x:x[1], reverse = True)

        with open(self._file_path, 'w') as file:
            file.write("Name:,Score:,Difficulty:\n")
            for score in scoreboard:
                name, points, difficulty = score
                if isinstance(score[2], int):
                    difficulty = self.__difficulty(score[2])
                file.writelines(name + "," + str(points) + "," + difficulty + "\n")
        
        file.close()
    
    def __difficulty(self, difficulty : int) -> str:
        str = "EASY"
        if difficulty == 2:
            str = "MEDIUM"
        elif difficulty == 1:
            str = "HARD"
        return str

    def reset_scoreboard(self):
        with open(self._file_path, 'w+') as file:
            file.write("Name:,Score:,Difficulty:\n"+
                        "Luke,20000,HARD\n" +
                        "Atom,19000,HARD\n" +
                        "Joe,18000,HARD\n" +
                        "Alucard,17000,MEDIUM\n" +
                        "Leon,16000,HARD\n" +
                        "Samus,15000,HARD\n" +
                        "Vincent,14000,EASY\n" +
                        "Eric,13000,MEDIUM\n" +
                        "Trevor,12000,MEDIUM\n" +
                        "Adam,11000,HARD\n" +
                        "Mathias,10000,MEDIUM\n" +
                        "Pluto,9000,EASY\n" +
                        "William,8000,MEDIUM\n" +
                        "Walter,7000,EASY\n" +
                        "Jack,6000,MEDIUM\n" +
                        "Sonia,5000,EASY\n" +
                        "Saul,4000,EASY\n" +
                        "Averell,3000,EASY\n")
    
    def __check_if_scoreboard_exists(self):
        try:
            file = open(self._file_path, 'r')
            file.close()
        except FileNotFoundError:
            self.reset_scoreboard()