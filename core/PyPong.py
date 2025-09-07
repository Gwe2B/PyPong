import arcade

from core.Ball import Ball
from core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE

class PyPong(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.csscolor.BLACK)

    def on_draw(self):
        self.clear()

        arcade.draw_line(600, 599, 600, 0, arcade.csscolor.WHITE)

    def on_update(self, delta_time):
        pass

    def on_key_press(self, symbol, modifiers):
        pass