import arcade

from core.Ball import Ball
from core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE

class PyPong(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.ball = Ball(600, 300, 1, 0.5)

        arcade.set_background_color(arcade.csscolor.BLACK)

    def on_draw(self):
        self.clear()

        arcade.draw_line(600, 599, 600, 0, arcade.csscolor.WHITE)
        self.ball.draw()

    def on_update(self, delta_time):
        self.ball.on_update()

    def on_key_press(self, symbol, modifiers):
        pass