import sys
from interface.menu import *
from assets import *
from interface.buttons import ButtonBase
from random import randint


class PreGame:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.playing = True

        self.text_font = pg.font.Font(FONT_DIR, 30)
        self.server_ip_address = ""
        self.port = ""

        self.assets = list()
        self.load_assets()

    def load_assets(self):
        self.background_image = pg.Surface((WIDTH, HEIGHT))
        self.background_image.fill(DARK_GREY)

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

        return self.server_ip_address, self.port
    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        pass
    def draw(self):
        self.screen.blit(self.background_image, (0, 0))

        text_surface = self.text_font.render("Join a server", False, FONT_COLOUR)
        self.screen.blit(text_surface, (TILE_SIZE * 15, TEXT_PADDING * 15))

        ipaddr_surface = self.text_font.render(self.server_ip_address, False, FONT_COLOUR)
        self.screen.blit(ipaddr_surface, (TILE_SIZE * 15, TEXT_PADDING * 20))

        pg.display.flip()

    def events(self):
        # catch all events here


        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                print(event.key)
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_0:
                    self.server_ip_address += "0"
                if event.key == pg.K_1:
                    self.server_ip_address += "1"
                if event.key == pg.K_2:
                    self.server_ip_address += "2"
                if event.key == pg.K_3:
                    self.server_ip_address += "3"
                if event.key == pg.K_4:
                    self.server_ip_address += "4"
                if event.key == pg.K_5:
                    self.server_ip_address += "5"
                if event.key == pg.K_6:
                    self.server_ip_address += "6"
                if event.key == pg.K_7:
                    self.server_ip_address += "7"
                if event.key == pg.K_8:
                    self.server_ip_address += "8"
                if event.key == pg.K_9:
                    self.server_ip_address += "9"
                if event.key == pg.K_PERIOD:
                    self.server_ip_address += "."
                if event.key == pg.K_COLON or event.key == pg.K_SEMICOLON:
                    self.server_ip_address += ":"
                if event.key == pg.K_BACKSPACE:
                    if len(self.server_ip_address) > 0:
                        self.server_ip_address = self.server_ip_address[:-1]
                if event.key == pg.K_RETURN:
                    self.playing = False
