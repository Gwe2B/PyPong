import arcade

from core.Ball import Ball
from core.Player import Player
from core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, PLAYER1_KEYS, PLAYER2_KEYS

class PyPong(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.ball = Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 1, 0.5)
        self.player1 = Player(10, (WINDOW_HEIGHT - Player.PLAYER_HEIGHT)/2, PLAYER1_KEYS)
        self.player2 = Player(WINDOW_WIDTH - 10 - Player.PLAYER_WIDTH, (WINDOW_HEIGHT - Player.PLAYER_HEIGHT)/2, PLAYER2_KEYS)

        arcade.set_background_color(arcade.csscolor.BLACK)

    def on_draw(self):
        self.clear()

        arcade.draw_line(WINDOW_WIDTH/2, WINDOW_HEIGHT-1, WINDOW_WIDTH/2, 0, arcade.csscolor.WHITE)
        self.ball.draw()
        self.player1.draw()
        self.player2.draw()

    def on_update(self, delta_time):
        self.ball.on_update()
        self.player1.on_update()
        self.player2.on_update()

    def on_key_press(self, symbol, modifiers):
        self.player1.register_key_press(symbol)
        self.player2.register_key_press(symbol)

    def on_key_release(self, symbol, modifiers):
        self.player1.register_key_release(symbol)
        self.player2.register_key_release(symbol)