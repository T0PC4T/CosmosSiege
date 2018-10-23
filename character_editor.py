import sys
from interface.menu import *
BLOCKS = [1, 1]

LOAD_DATA = None



if LOAD_DATA:
    BLOCKS = [len(LOAD_DATA[0])//TILE_SIZE, len(LOAD_DATA)//TILE_SIZE]

ED_TILE_SIZE = TILE_SIZE//2
ARENA_WIDTH = int((ED_TILE_SIZE*TILE_SIZE) * BLOCKS[0])
ARENA_HEIGHT = int((ED_TILE_SIZE*TILE_SIZE) * BLOCKS[1])
EDITOR_WIDTH = ARENA_WIDTH + ED_TILE_SIZE*4
EDITOR_HEIGHT = ARENA_HEIGHT


class CharacterEditor:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((EDITOR_WIDTH, EDITOR_HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.Group()
        self.playing = True
        self.tiles_width = int(TILE_SIZE*BLOCKS[0])
        self.tiles_height = int(TILE_SIZE*BLOCKS[1])
        if LOAD_DATA:
            self.data = list()

            for _y, row in enumerate(LOAD_DATA):
                new_row = list()
                for _x, cell in enumerate(row):
                    new_row.append(ColourCube(self, _x*ED_TILE_SIZE, _y*ED_TILE_SIZE, cell))

                self.data.append(new_row)

        else:
            self.data = [list([None] * self.tiles_width) for i in range(self.tiles_height)]
        self.drawing = False
        self.drawing_colour = [255, 255, 255]
        self.bg_colouring = False
        self.colour_buttons = list()
        self.amount = 0.5
        x = self.get_area_width()
        y = 0
        self.bg_colour_btn = ColourButton(self, x, y, ED_TILE_SIZE*2, BGCOLOUR)
        self.paint_colour_btn = ColourButton(self, x+ED_TILE_SIZE*2, y, ED_TILE_SIZE*2, self.drawing_colour)

        base_y = ED_TILE_SIZE*4
        lower_y = ED_TILE_SIZE*5

        self.ri_btn = ColourButton(self, x,                base_y, ED_TILE_SIZE, (255, 0, 0), [self.change_colour, [0, True]])
        self.rd_btn = ColourButton(self, x,                lower_y, ED_TILE_SIZE, (55, 0, 0), [self.change_colour, [0, False]])
        self.gi_btn = ColourButton(self, x+ED_TILE_SIZE,   base_y, ED_TILE_SIZE, (0, 255, 0), [self.change_colour, [1, True]])
        self.gd_btn = ColourButton(self, x+ED_TILE_SIZE,   lower_y, ED_TILE_SIZE, (0, 55, 0), [self.change_colour, [1, False]])
        self.bi_btn = ColourButton(self, x+ED_TILE_SIZE*2, base_y, ED_TILE_SIZE, (0, 0, 255), [self.change_colour, [2, True]])
        self.bd_btn = ColourButton(self, x+ED_TILE_SIZE*2, lower_y, ED_TILE_SIZE, (0, 0, 55), [self.change_colour, [2, False]])

        pg.mouse.set_cursor((8, 8), (4, 4), (24, 24, 24, 231, 231, 24, 24, 24), (0, 0, 0, 0, 0, 0, 0, 0))

    def change_colour(self, colour_id, increase=True):
        self.amount += 0.25
        if increase:
            self.drawing_colour[colour_id] += self.amount
        else:
            self.drawing_colour[colour_id] -= self.amount

        if self.drawing_colour[colour_id] > 255:
            self.drawing_colour[colour_id] = 255
        elif self.drawing_colour[colour_id] < 0:
            self.drawing_colour[colour_id] = 0

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def get_tile_size(self):
        return ED_TILE_SIZE
        # return EDITOR_WIDTH // self.tiles

    def get_area_width(self):
        return ARENA_WIDTH

    def get_area_height(self):
        return ARENA_HEIGHT

    def draw_grid(self):
        for x in range(0, self.get_area_width(), ED_TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, self.get_area_height()))

        for y in range(0, self.get_area_height(), ED_TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (self.get_area_width(), y))

        pg.draw.line(self.screen, WHITE, (self.get_area_width()//2, 0), (self.get_area_width()//2, self.get_area_height()))
        pg.draw.line(self.screen, WHITE, (0, self.get_area_height()//2), (self.get_area_width(), self.get_area_height()//2))

    def draw(self):
        pg.display.set_caption("{}".format([int(i) for i in self.drawing_colour]))
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        pg.display.flip()

    def set_drawing_colour(self, colour):
        if colour is BGCOLOUR:
            self.bg_colouring = True
        else:
            self.bg_colouring = False
            self.drawing_colour = colour

        self.drawing = True

    def update(self):
        # update portion of the game loop
        if not self.bg_colouring:
            self.paint_colour_btn.set_colour(self.drawing_colour)
        self.all_sprites.update()

    def print_data(self):
        clean_data = list()
        for row in self.data:
            row_list = list()
            for cell in row:
                if not cell or cell is BGCOLOUR:
                    row_list.append("BGCOLOUR")
                else:
                    row_list.append(cell.get_colour())

            clean_data.append(row_list)

        print("data = [")
        for row in clean_data:
            print(str(row).replace("'BGCOLOUR'", "BGCOLOUR") + ",")
        print("]")

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.print_data()

        if self.drawing and pg.mouse.get_pressed()[0]:
            mousex, mousey = pg.mouse.get_pos()
            tile_x = mousex - (mousex % ED_TILE_SIZE)
            tile_y = mousey - (mousey % ED_TILE_SIZE)
            tile_index_x = tile_x // ED_TILE_SIZE
            tile_index_y = tile_y // ED_TILE_SIZE
            if tile_index_x < len(self.data[0]) and tile_index_y < len(self.data):
                dc = BGCOLOUR if self.bg_colouring else self.drawing_colour
                self.data[tile_index_y][tile_index_x] = ColourCube(self, tile_x, tile_y, dc)

        if not pg.mouse.get_pressed()[0]:
            self.amount = 1.5



from interface.buttons import ButtonBase


class ColourButton(pg.sprite.Sprite, ButtonBase):
    def __init__(self, editor, x, y, dim, colour, func=None):

        # Sprite base

        self.groups = editor.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        ButtonBase.__init__(self, True)
        self.editor = editor

        self.image = pg.Surface((dim, dim))
        self.image.fill(colour)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # Other variables

        self.colour = colour
        if not func:
            self.button_action: tuple = (lambda colour: editor.set_drawing_colour(colour), [self.colour], {})
        else:
            self.set_action(func[0], *func[1])

    def get_colour(self):
        return (int(self.colour[0]), int(self.colour[1]), int(self.colour[2]))

    def set_colour(self, colour):
        self.colour = colour

    def update(self):
        self.image.fill(self.colour)
        self.btn_update()
        # self.rect.width = self.editor.get_tile_size()
        # self.rect.height = self.editor.get_tile_size()
        # self.rect.x = self.editor.get_tile_size()

class ColourCube(pg.sprite.Sprite):
    def __init__(self, editor, x, y, colour):
        # Sprite base

        self.groups = editor.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.editor = editor

        dim = editor.get_tile_size()
        self.image = pg.Surface((dim, dim))
        self.image.fill(colour)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # Other variables

        self.colour = [int(i) for i in colour]

    def get_colour(self):
        return self.colour

g = CharacterEditor()
g.run()
