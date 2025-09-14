import arcade
import random
import time

from core import Ball, Player, WINDOW_WIDTH, WINDOW_HEIGHT, PLAYER1_KEYS, PLAYER2_KEYS

class GameLogic:
    def __init__(self):
        self.ball_sprite_list = arcade.SpriteList()
        self.ball = Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, random.choice([-1, 1]), random.uniform(-0.5, 0.5))
        self.ball.on_side_wall_hit = self.on_ball_side_wall_hit
        self.ball_sprite_list.append(self.ball)

        self.player_sprite_list = arcade.SpriteList()
        self.player1 = Player(10, (WINDOW_HEIGHT - Player.PLAYER_HEIGHT)/2, PLAYER1_KEYS)
        self.player2 = Player(WINDOW_WIDTH - 10 - Player.PLAYER_WIDTH, (WINDOW_HEIGHT - Player.PLAYER_HEIGHT)/2, PLAYER2_KEYS)
        self.player_sprite_list.append(self.player1)
        self.player_sprite_list.append(self.player2)

        self.is_game_freezed = False
        self.freeze_start_time = 0
        self.freeze_game()

    def on_ball_side_wall_hit(self, side: str):
        """Callback when the ball hits a side wall."""
        if side == "left":
            self.player2.increment_score()
        elif side == "right":
            self.player1.increment_score()

        self.ball.velocity_y = random.uniform(-0.5, 0.5)
        self.ball.reset()
        self.freeze_game()

    def freeze_game(self):
        self.freeze_start_time = time.time()
        self.is_game_freezed = True

    def update(self, delta_time: float):
        """Update game state."""
        self.player_sprite_list.update()
        if self.is_game_freezed:
            if time.time() - self.freeze_start_time >= 3:
                self.is_game_freezed = False
            return

        self.ball_sprite_list.update()
        ball_hit_list = arcade.check_for_collision_with_list(self.ball, self.player_sprite_list)
        if ball_hit_list:
            self.ball.bounce()

    def handle_key_press(self, symbol: int, modifiers: int):
        """Handle key press events."""
        self.player1.register_key_press(symbol)
        self.player2.register_key_press(symbol)

    def handle_key_release(self, symbol: int, modifiers: int):
        """Handle key release events."""
        self.player1.register_key_release(symbol)
        self.player2.register_key_release(symbol)
