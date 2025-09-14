import arcade
import time

from core import WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH
from game import GameLogic

class PyPong(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.game_logic = GameLogic()
        self.is_game_paused = False
        arcade.set_background_color(arcade.csscolor.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_line(WINDOW_WIDTH/2, WINDOW_HEIGHT-1, WINDOW_WIDTH/2, 0, arcade.csscolor.WHITE)
        self.game_logic.ball_sprite_list.draw()
        self.game_logic.player_sprite_list.draw()

        # Draw scores
        score_x_player1 = (WINDOW_WIDTH // 2) - 20
        score_x_player2 = (WINDOW_WIDTH // 2) + 20
        score_y = WINDOW_HEIGHT - 30
        arcade.draw_text(
            f"{self.game_logic.player1.score}",
            score_x_player1,
            score_y,
            arcade.csscolor.WHITE,
            24,
            anchor_x="center"
        )
        arcade.draw_text(
            f"{self.game_logic.player2.score}",
            score_x_player2,
            score_y,
            arcade.csscolor.WHITE,
            24,
            anchor_x="center"
        )

        if self.game_logic.is_game_freezed:
            self.draw_freeze()
        if self.is_game_paused:
            self.draw_pause_menu()

    def draw_freeze(self):
        count = int(time.time() - self.game_logic.freeze_start_time)
        arcade.draw_lrbt_rectangle_filled(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, (0, 0, 0, 150))
        arcade.draw_text(
            f"{3 - count}", WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
            arcade.color.WHITE, 128, anchor_x="center", anchor_y="center"
        )

    def draw_pause_menu(self):
        arcade.draw_lrbt_rectangle_filled(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, (0, 0, 0, 150))
        arcade.draw_text(
            "PAUSE\nPress P to unpause", WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
            arcade.color.WHITE, 64, width=600, align="center",
            anchor_x="center", anchor_y="center", multiline=True
        )

    def on_update(self, delta_time: float):
        if self.is_game_paused:
            return
        self.game_logic.update(delta_time)

    def on_key_press(self, symbol: int, modifiers: int):
        self.game_logic.handle_key_press(symbol, modifiers)
        if symbol == arcade.key.P:
            self.is_game_paused = not self.is_game_paused

    def on_key_release(self, symbol: int, modifiers: int):
        self.game_logic.handle_key_release(symbol, modifiers)
