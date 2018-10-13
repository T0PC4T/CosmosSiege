import sys
from interface.menus import *

EDITOR_WIDTH = TILE_SIZE*TILE_SIZE + TILE_SIZE*4
EDITOR_HEIGHT = TILE_SIZE*TILE_SIZE


class CharacterEditor:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((EDITOR_WIDTH, EDITOR_HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.Group()
        self.playing = True
        self.tiles = TILE_SIZE
        pg.mouse.set_cursor((8, 8), (4, 4), (24, 24, 24, 231, 231, 24, 24, 24), (0, 0, 0, 0, 0, 0, 0, 0))


        self.drawing = False
        self.drawing_colour = None

        self.colour_buttons = list()



        self.data = [list([None]*TILE_SIZE) for i in range(TILE_SIZE)]

        row = 0
        for col, colour in enumerate([WHITE, BLACK, LIGHTGREY, DARKGREY, BLUE, RED, GREEN, YELLOW]):
            if (col % 4) == 0 and col != 0:
                row +=1

            alt_col = col - (row*4)

            x = alt_col*TILE_SIZE + self.get_area_width()
            y = row*TILE_SIZE

            cb = ColourButton(self, x, y, colour)
            self.colour_buttons.append(cb)

    def run(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def get_tile_size(self):
        return TILE_SIZE
        # return EDITOR_WIDTH // self.tiles

    def get_area_width(self):
        return TILE_SIZE*TILE_SIZE

    def get_area_height(self):
        return TILE_SIZE*TILE_SIZE

    def draw_grid(self):
        for x in range(0, self.get_area_width(), TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, self.get_area_height()))

        for y in range(0, self.get_area_height(), TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (self.get_area_width(), y))


    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def set_drawing_colour(self, colour):
        self.drawing = True
        self.drawing_colour = colour

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def print_data(self):
        clean_data = list()
        for row in self.data:
            row_list = list()
            for cell in row:
                if not cell:
                    row_list.append(BLACK)
                else:
                    row_list.append(cell.get_colour())

            clean_data.append(row_list)

        print("data = [")
        for row in clean_data:
            print(str(row) + ",")
        print("]")

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.tiles += 4
                if event.key == pg.K_DOWN and self.tiles > 4:
                    self.tiles -= 4
                if event.key == pg.K_RETURN:
                    self.print_data()

        if self.drawing and pg.mouse.get_pressed()[0]:
            try:
                mousex, mousey = pg.mouse.get_pos()
                tile_x = mousex - (mousex % TILE_SIZE)
                tile_y = mousey - (mousey % TILE_SIZE)
                tile_index_x = tile_x // TILE_SIZE
                tile_index_y = tile_y // TILE_SIZE
                if tile_index_x < TILE_SIZE and tile_index_y < TILE_SIZE:
                    self.data[tile_index_y][tile_index_x] = ColourButton(self, tile_x, tile_y, self.drawing_colour)

            except Exception as e:
                pass


from interface.buttons import ButtonBase


class ColourButton(pg.sprite.Sprite, ButtonBase):
    def __init__(self, editor, x, y, colour):

        # Sprite base

        self.groups = editor.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        ButtonBase.__init__(self)
        self.editor = editor

        dim = editor.get_tile_size()
        self.image = pg.Surface((dim, dim))
        self.image.fill(colour)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # Other variables

        self.colour = colour

        self.button_action: tuple = (lambda colour: editor.set_drawing_colour(colour), [self.colour], {})

    def get_colour(self):
        return self.colour

    def update(self):
        self.btn_update()
        # self.rect.width = self.editor.get_tile_size()
        # self.rect.height = self.editor.get_tile_size()
        # self.rect.x = self.editor.get_tile_size()


g = CharacterEditor()
g.run()
