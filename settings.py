# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (20, 20, 20)
GREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (66, 134, 244)
BROWN = (147, 96, 59)
DARK_BLUE = (58, 112, 150)
DARK_GREEN = (38, 77, 0)
# game settings

FPS: int = 65
TITLE = "Tower Wars"
BGCOLOUR = (0, 0, 0)
FONT_DIR = 'assets/fonts/slkscr.ttf'
FONT_COLOUR = (51, 255, 0)

# Display settings
TILE_SIZE = 34
TEXT_PADDING = TILE_SIZE//4

WIDTH = int(TILE_SIZE * 44)
HEIGHT = int(TILE_SIZE * 26)

# MENU SETTINGS
MENU_COLOUR = DARK_GREY
MENU_WIDTH = int(TILE_SIZE * 6)
MENU_X = WIDTH - MENU_WIDTH
MENU_Y = 0


# MENU TITLE
TITLE_STRIP_HEIGHT = TILE_SIZE + TEXT_PADDING
TITLE_STRIP_WIDTH = MENU_WIDTH
TITLE_STRIP_X = MENU_X
TITLE_STRIP_Y = 0

# MENU IMAGE
UNIT_IMG_WIDTH = MENU_WIDTH
UNIT_IMG_HEIGHT = MENU_WIDTH
UNIT_IMG_X = MENU_X
UNIT_IMG_Y = TITLE_STRIP_HEIGHT

# MENU INFO
MENU_INFO_HEIGHT = TILE_SIZE * 4
MENU_INFO_WIDTH = MENU_WIDTH
MENU_INFO_Y = UNIT_IMG_Y + UNIT_IMG_HEIGHT + TEXT_PADDING
MENU_INFO_X = MENU_X
MENU_INFO_TITLE = 26
MENU_INFO_TEXT_SIZE = 20

# MENU DATA RECORDS
UNIT_BTN_NUM = 4
DATA_RECORD_WIDTH = MENU_WIDTH
DATA_RECORD_HEIGHT = TILE_SIZE * 2

DATA_LIST_WIDTH = MENU_WIDTH
DATA_LIST_HEIGHT = DATA_RECORD_HEIGHT * UNIT_BTN_NUM
DATA_LIST_X = MENU_X
DATA_LIST_Y = MENU_INFO_Y + MENU_INFO_HEIGHT

PAGE_BTN_WIDTH = TILE_SIZE
PAGE_BTN_HEIGHT = TILE_SIZE
PAGE_PREV_X = MENU_X
PAGE_NEXT_X = WIDTH - PAGE_BTN_WIDTH
PAGE_Y = DATA_LIST_Y + DATA_LIST_HEIGHT


# MENU READY BTN
MENU_READY_COLOUR = (51, 255, 0)
MENU_READY_HEIGHT = TILE_SIZE * 2
MENU_READY_WIDTH = DATA_LIST_WIDTH
MENU_READY_X = MENU_X
MENU_READY_Y = HEIGHT - MENU_READY_HEIGHT


# ARENA
ARENA_WIDTH = WIDTH - MENU_WIDTH
ARENA_HEIGHT = HEIGHT

ARENA_TILE_WIDTH = int(ARENA_WIDTH / TILE_SIZE)
ARENA_TILE_HEIGHT = int(ARENA_HEIGHT / TILE_SIZE)