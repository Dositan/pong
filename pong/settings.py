
__all__ = (
    'TITLE',
    'WIDTH',
    'HEIGHT',
    'FPS',
    'GREY',
    'BG_COLOR',
)

# Main Window
TITLE = 'Pong!'
WIDTH = 1280
HEIGHT = 700
FPS = 60

# Colors.
LIGHT_THEME = False
GREY = (200, 200, 200)
BG_COLOR = (31, 31, 31)
if LIGHT_THEME:
    GREY, BG_COLOR = BG_COLOR, GREY
