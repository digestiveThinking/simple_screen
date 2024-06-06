import curses
from .entities import Position, Color, Dimensions


# Definición de constantes de colores
# Colores en formato RGB base 1000

ALICE_BLUE = Color(240, 248, 255)
ANTIQUE_WHITE = Color(250, 235, 215)
AQUA = Color(0, 255, 255)
AQUAMARINE = Color(127, 255, 212)
AZURE = Color(240, 255, 255)
BEIGE = Color(245, 245, 220)
BISQUE = Color(255, 228, 196)
BLACK = Color(0, 0, 0)
BLANCHED_ALMOND = Color(255, 235, 205)
BLUE = Color(0, 0, 255)
BLUE_VIOLET = Color(138, 43, 226)
BROWN = Color(165, 42, 42)
BURLYWOOD = Color(222, 184, 135)
CADET_BLUE = Color(95, 158, 160)
CHARTREUSE = Color(127, 255, 0)
CHOCOLATE = Color(210, 105, 30)
CORAL = Color(255, 127, 80)
CORNFLOWER_BLUE = Color(100, 149, 237)
CORNSILK = Color(255, 248, 220)
CRIMSON = Color(220, 20, 60)
CYAN = Color(0, 255, 255)
DARK_BLUE = Color(0, 0, 139)
DARK_CYAN = Color(0, 139, 139)
DARK_GOLDENROD = Color(184, 134, 11)
DARK_GRAY = Color(169, 169, 169)
DARK_GREEN = Color(0, 100, 0)
DARK_KHAKI = Color(189, 183, 107)
DARK_MAGENTA = Color(139, 0, 139)
DARK_OLIVE_GREEN = Color(85, 107, 47)
DARK_ORANGE = Color(255, 140, 0)
DARK_ORCHID = Color(153, 50, 204)
DARK_RED = Color(139, 0, 0)
DARK_SALMON = Color(233, 150, 122)
DARK_SEA_GREEN = Color(143, 188, 143)
DARK_SLATE_BLUE = Color(72, 61, 139)
DARK_SLATE_GRAY = Color(47, 79, 79)
DARK_TURQUOISE = Color(0, 206, 209)
DARK_VIOLET = Color(148, 0, 211)
DEEP_PINK = Color(255, 20, 147)
DEEP_SKY_BLUE = Color(0, 191, 255)
DIM_GRAY = Color(105, 105, 105)
DODGER_BLUE = Color(30, 144, 255)
FIREBRICK = Color(178, 34, 34)
FLORAL_WHITE = Color(255, 250, 240)
FOREST_GREEN = Color(34, 139, 34)
FUCHSIA = Color(255, 0, 255)
GAINSBORO = Color(220, 220, 220)
GHOST_WHITE = Color(248, 248, 255)
GOLD = Color(255, 215, 0)
GOLDENROD = Color(218, 165, 32)
GRAY = Color(128, 128, 128)
GREEN = Color(0, 128, 0)
GREEN_YELLOW = Color(173, 255, 47)
HONEYDEW = Color(240, 255, 240)
HOT_PINK = Color(255, 105, 180)
INDIAN_RED = Color(205, 92, 92)
INDIGO = Color(75, 0, 130)
IVORY = Color(255, 255, 240)
KHAKI = Color(240, 230, 140)
LAVENDER = Color(230, 230, 250)
LAVENDER_BLUSH = Color(255, 240, 245)
LAWN_GREEN = Color(124, 252, 0)
LEMON_CHIFFON = Color(255, 250, 205)
LIGHT_BLUE = Color(173, 216, 230)
LIGHT_CORAL = Color(240, 128, 128)
LIGHT_CYAN = Color(224, 255, 255)
LIGHT_GOLDENROD_YELLOW = Color(250, 250, 210)
LIGHT_GRAY = Color(211, 211, 211)
LIGHT_GREEN = Color(144, 238, 144)
LIGHT_PINK = Color(255, 182, 193)
LIGHT_SALMON = Color(255, 160, 122)
LIGHT_SEA_GREEN = Color(32, 178, 170)
LIGHT_SKY_BLUE = Color(135, 206, 250)
LIGHT_SLATE_GRAY = Color(119, 136, 153)
LIGHT_STEEL_BLUE = Color(176, 196, 222)
LIGHT_YELLOW = Color(255, 255, 224)
LIME = Color(0, 255, 0)
LIME_GREEN = Color(50, 205, 50)
LINEN = Color(250, 240, 230)
MAGENTA = Color(255, 0, 255)
MAROON = Color(128, 0, 0)
MEDIUM_AQUAMARINE = Color(102, 205, 170)
MEDIUM_BLUE = Color(0, 0, 205)
MEDIUM_ORCHID = Color(186, 85, 211)
MEDIUM_PURPLE = Color(147, 112, 219)
MEDIUM_SEA_GREEN = Color(60, 179, 113)
MEDIUM_SLATE_BLUE = Color(123, 104, 238)
MEDIUM_SPRING_GREEN = Color(0, 250, 154)
MEDIUM_TURQUOISE = Color(72, 209, 204)
MEDIUM_VIOLET_RED = Color(199, 21, 133)
MIDNIGHT_BLUE = Color(25, 25, 112)
MINT_CREAM = Color(245, 255, 250)
MISTY_ROSE = Color(255, 228, 225)
MOCCASIN = Color(255, 228, 181)
NAVAJO_WHITE = Color(255, 222, 173)
NAVY = Color(0, 0, 128)
OLD_LACE = Color(253, 245, 230)
OLIVE = Color(128, 128, 0)
OLIVE_DRAB = Color(107, 142, 35)
ORANGE = Color(255, 165, 0)
ORANGE_RED = Color(255, 69, 0)
ORCHID = Color(218, 112, 214)
PALE_GOLDENROD = Color(238, 232, 170)
PALE_GREEN = Color(152, 251, 152)
PALE_TURQUOISE = Color(175, 238, 238)
PALE_VIOLET_RED = Color(219, 112, 147)
PAPAYA_WHIP = Color(255, 239, 213)
PEACH_PUFF = Color(255, 218, 185)
PERU = Color(205, 133, 63)
PINK = Color(255, 192, 203)
PLUM = Color(221, 160, 221)
POWDER_BLUE = Color(176, 224, 230)
PURPLE = Color(128, 0, 128)
REBECCA_PURPLE = Color(102, 51, 153)
RED = Color(255, 0, 0)
ROSY_BROWN = Color(188, 143, 143)
ROYAL_BLUE = Color(65, 105, 225)
SADDLE_BROWN = Color(139, 69, 19)
SALMON = Color(250, 128, 114)
SANDY_BROWN = Color(244, 164, 96)
SEA_GREEN = Color(46, 139, 87)
SEASHELL = Color(255, 245, 238)
SIENNA = Color(160, 82, 45)
SILVER = Color(192, 192, 192)
SKY_BLUE = Color(135, 206, 235)
SLATE_BLUE = Color(106, 90, 205)
SLATE_GRAY = Color(112, 128, 144)
SNOW = Color(255, 250, 250)
SPRING_GREEN = Color(0, 255, 127)
STEEL_BLUE = Color(70, 130, 180)
TAN = Color(210, 180, 140)
TEAL = Color(0, 128, 128)
THISTLE = Color(216, 191, 216)
TOMATO = Color(255, 99, 71)
TURQUOISE = Color(64, 224, 208)
VIOLET = Color(238, 130, 238)
WHEAT = Color(245, 222, 179)
WHITE = Color(255, 255, 255)
WHITE_SMOKE = Color(245, 245, 245)
YELLOW = Color(255, 255, 0)
YELLOW_GREEN = Color(154, 205, 50)

# Lista de colores en la que la posición del número es el valor hexadecimal


def app(func):
    def wrapper(stdsrc, *args, **kwargs):
        try:
            func(stdsrc, *args, **kwargs)
        finally:
            _end(stdsrc)

    return wrapper


def _end(scr):
    curses.nocbreak()
    scr.keypad(False)
    curses.echo()
    curses.endwin()


def _init_curses():
    pantalla = curses.initscr()

    curses.cbreak()
    curses.start_color()
    pantalla.keypad(True)

    return pantalla


STDSRC = None
POS = Position(0, 0)
FOREGROUND = Color(250, 250, 250)
BACKGROUND = Color(0, 0, 0)
DIMENSIONS = None
MAX_PAIRS = -1
MAX_COLORS = -1
ACTIVE_PAIR = 1


def pause(ms):
    curses.napms(ms)


def init():
    global STDSRC, POS, DIMENSIONS, MAX_PAIRS, MAX_COLORS
    STDSRC = _init_curses()
    DIMENSIONS = Dimensions(*STDSRC.getmaxyx())
    MAX_PAIRS = curses.COLOR_PAIRS
    MAX_COLORS = curses.COLORS
    pair(FOREGROUND, BACKGROUND)


def finish():
    _end(STDSRC)
    

def cls(refresh=False):
    STDSRC.clear()
    locate(0, 0)
    if refresh:
        STDSRC.refresh()


def locate(x, y):
    global POS
    STDSRC.move(y, x)
    _retrievePos()
    

def Print(cadena, refresh=False):
    STDSRC.addstr(str(cadena), curses.color_pair(ACTIVE_PAIR))
    _retrievePos()
    locate(0, POS.y + 1)
    _retrievePos()
    if refresh:
        STDSRC.refresh()


def Input(mensaje=""):
    curses.curs_set(1)
    STDSRC.addstr(mensaje, curses.color_pair(ACTIVE_PAIR))
    curses.echo()
    user_input = STDSRC.getstr(curses.color_pair(ACTIVE_PAIR)).decode('utf-8')
    curses.noecho()
    _retrievePos()
    return user_input


def _create_color(ix: int, color: Color):
    curses.init_color(ix, *color.value)


def _retrievePos():
    global POS
    POS = Position(*STDSRC.getyx())


def pair(fg, bg, refresh=False):
    global FOREGROUND, BACKGROUND
    _create_color(12, fg)
    _create_color(13, bg)
    curses.init_pair(ACTIVE_PAIR, 12, 13)
    FOREGROUND = fg
    BACKGROUND = bg
    STDSRC.bkgd(' ', curses.color_pair(ACTIVE_PAIR))
    if refresh:
        STDSRC.refresh()


def pen(fg, refresh=False):
    pair(fg, BACKGROUND, refresh)


def paper(bg, refresh=False):
    pair(FOREGROUND, bg, refresh)
