import pygame as pg

class ButtonBase(object):

    def __init__(self):
        self.mouse_down: bool = False

    def set_action(self, func, *args, **kwargs):
        self.button_action = (func, args, kwargs)
        return self

    def run_action(self):
        return self.button_action[0](*self.button_action[1], **self.button_action[2])

    def is_mouse_over(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if self.rect.x + self.rect.width > mouse_x > self.rect.x \
                and self.rect.y + self.rect.height > mouse_y > self.rect.y:
            return True
        return False

    def btn_update(self):
        if not self.mouse_down:
            if self.is_mouse_over():
                if pg.mouse.get_pressed()[0]:
                    self.mouse_down = True
        else:
            if not pg.mouse.get_pressed()[0]:
                if self.is_mouse_over():
                    self.mouse_down = False
                    self.run_action()
                else:
                    self.mouse_down = False

    def update(self):
        self.btn_update()