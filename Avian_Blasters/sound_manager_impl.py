import pygame

from Avian_Blasters.sound_manager import SoundManager

class SoundManagerImpl(SoundManager):

    """ SoundManagerImpl is an implementation of SoundManager interface """

    def __init__(self):
        pygame.mixer.init()

    def play_music(self, music_file_path: str, loop: int = -1, volume: float = 0.5):
        pygame.mixer.music.load(music_file_path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)

    def stop_music(self):
        pygame.mixer.music.stop()