import sys
from interface.menu import *
from assets import *
from interface.buttons import ButtonBase
from random import randint
import socket

CONNECT_TO_SERVER = 1
CONNECT_BETWEEN_UNREADY = 1.5
UNREADY = 2
UNREADY_BETWEEN_READY = 2.5
READY = 3
ALL_READY = 4

class PreGame:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.code = CONNECT_TO_SERVER

        self.text_font = pg.font.Font(FONT_DIR, 30)
        self.server_ip_address = ""

        self.assets = list()
        self.load_assets()
        self.s = None

    def load_assets(self):
        self.background_image = pg.Surface((WIDTH, HEIGHT))
        self.background_image.fill(DARK_GREY)

    def run(self):
        while self.code != ALL_READY:
            self.clock.tick(FPS)
            self.events()
            self.communicate()
            self.update()
            self.draw()

        return self.s

    def communicate(self):
        if self.code == CONNECT_BETWEEN_UNREADY:
            try:
                ipaddr, port = self.server_ip_address.split(":")
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((ipaddr, int(port)))
                self.s.sendall(b'echo')
                data = self.s.recv(1024)
                if not data or data != b'echo':
                    print(data)
                    raise Exception("data was")

                self.code = UNREADY
            except Exception as e:
                print(e)
                self.code = CONNECT_TO_SERVER

        elif self.code > CONNECT_BETWEEN_UNREADY:
            print("GETTING DATA")
            data = self.s.recv(1024)
            print("FINISHED GETTING DATA")
            if self.code == UNREADY_BETWEEN_READY:
                self.s.sendall(b'ready')
                self.code = READY

            if self.code == READY:
                data = self.s.recv(1024)
                if b"all ready" in data:
                    self.code = ALL_READY

    def players_are_ready(self):
        self.code = ALL_READY

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        pass

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        if self.code == CONNECT_TO_SERVER:
            text_surface = self.text_font.render("Join a server", False, FONT_COLOUR)
            self.screen.blit(text_surface, (TILE_SIZE * 15, TEXT_PADDING * 15))
        elif self.code == UNREADY:
            text_surface = self.text_font.render("[NOT READY] Press Enter", False, FONT_COLOUR)
            self.screen.blit(text_surface, (TILE_SIZE * 15, TEXT_PADDING * 15))
        elif self.code == READY:
            text_surface = self.text_font.render("[READY] Waiting for players", False, FONT_COLOUR)
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
                    if self.code == CONNECT_TO_SERVER:
                        self.code = CONNECT_BETWEEN_UNREADY
                    elif self.code == UNREADY:
                        self.code = UNREADY_BETWEEN_READY
