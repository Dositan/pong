
__all__ = (
    'TITLE',
    'WIDTH',
    'HEIGHT',
    'FPS',
    'MAX_SCORES_PER_MATCH',
    'GREY',
    'BG_COLOR',
)

# Main Window
TITLE = 'Pongasyl!'
WIDTH = 1280
HEIGHT = 700
FPS = 60
MAX_SCORES_PER_MATCH = 10

# Colors.
LIGHT_THEME = False
GREY = (200, 200, 200)
BG_COLOR = (31, 31, 31)
if LIGHT_THEME:
    GREY, BG_COLOR = BG_COLOR, GREY
