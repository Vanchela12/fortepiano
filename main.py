from settings import *
from game.pianinobutton import PianoInButton

notes = ['a', 'b', 'd', 'e', 'f', 'g']
pianos_buttons = [PianoInButton((150 + i * 110, 40), (100, 220), 'white', sound_file=f'assets/sounds/{nota}6.mp3') for i, nota in enumerate(notes)]

while True:
    for e in event.get():
        if e.type == QUIT:
            quit(); exit()
        if e.type == MOUSEBUTTONDOWN:
            mouse_pos = e.pos
            for button in pianos_buttons:
                button.is_clicked(mouse_pos)

    for button in pianos_buttons:
        button.reset()

    display.update()
    clock.tick(60)
