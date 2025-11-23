from settings import *

class Button:
    def __init__(self, pos, size, color, text='', text_color=(0, 0, 0), font_size=30):
        self.rect = Rect(*pos, *size)
        self.color = color
        self.text = text
        self.text_color = text_color
        if text:
            self.font = font.Font('Arial', font_size)

    def reset(self):
        draw.rect(window, self.color, self.rect)
        if self.text:
            text_surf = self.font.render(self.text, True, self.text_color)
            text_rect = text_surf.get_rect(center=self.rect.center)
            window.blit(text_surf, text_rect)
            