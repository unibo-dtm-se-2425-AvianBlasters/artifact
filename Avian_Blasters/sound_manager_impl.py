import pygame

from Avian_Blasters.sound_manager import SoundManager

class SoundManagerImpl(SoundManager):

    """ SoundManagerImpl is an implementation of SoundManager interface """

    def __init__(self):
        pygame.mixer.init()

    def play_music(self, music_file_path: str, loop: int = -1, volume: float = 1.0):
        pygame.mixer.music.load(music_file_path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)

    def stop_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    def play_sound_effect(self, sound_file_path: str, volume: float = 1.0):
        sound = pygame.mixer.Sound(sound_file_path)
        sound.set_volume(volume)
        sound.play()