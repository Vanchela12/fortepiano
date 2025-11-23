from game.button import Button
from settings import *


class PianoInButton(Button):
    def __init__(self, pos, size, color, text='', text_color=(0, 0, 0), font_size=30, sound_file='assets/sounds/g6.mp3'):
        super().__init__(pos, size, color, text, text_color, font_size)
        self.sound = mixer.Sound(sound_file)

    def play_sound(self):
        self.sound.play()

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.play_sound()
