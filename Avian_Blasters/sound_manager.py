class SoundManager:

    """ SoundManager is a class that manages sound effects and music for the game"""

    def play_music(self, music_file_path: str, loop: int, volume: float) -> None:
       ...

    def stop_music(self) -> None:
        ...