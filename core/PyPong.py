import arcade

import random
from core.Ball import Ball
from core.Player import Player
from core.constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, PLAYER1_KEYS, PLAYER2_KEYS

class PyPong(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.ball_sprite_list = arcade.SpriteList()
        self.ball = Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, random.choice([-1, 1]), random.uniform(-0.5, 0.5))
        self.ball.on_side_wall_hit = self.on_ball_side_wall_hit
        self.ball_sprite_list.append(self.ball)

        self.player_sprite_list = arcade.SpriteList()
        self.player1 = Player(10, (WINDOW_HEIGHT - Player.PLAYER_HEIGHT)/2, PLAYER1_KEYS)
        self.player2 = Player(WINDOW_WIDTH - 10 - Player.PLAYER_WIDTH, (WINDOW_HEIGHT - Player.PLAYER_HEIGHT)/2, PLAYER2_KEYS)

        self.player_sprite_list.append(self.player1)
        self.player_sprite_list.append(self.player2)

        arcade.set_background_color(arcade.csscolor.BLACK)

    def on_ball_side_wall_hit(self, side: str):
        """Callback appelé quand la balle touche un mur latéral."""
        if side == "left":
            self.player2.increment_score()  # Joueur 2 marque
        elif side == "right":
            self.player1.increment_score()  # Joueur 1 marque
        
        # Réinitialise la balle au centre
        self.ball.velocity_y = random.uniform(-0.5, 0.5)
        self.ball.reset()

    def on_draw(self):
        self.clear()

        arcade.draw_line(WINDOW_WIDTH/2, WINDOW_HEIGHT-1, WINDOW_WIDTH/2, 0, arcade.csscolor.WHITE)
        self.ball_sprite_list.draw()
        self.player_sprite_list.draw()
        
        # Calcul des positions pour les scores (20px de chaque côté de la ligne centrale)
        score_x_player1 = (WINDOW_WIDTH // 2) - 20  # 20px à gauche de la ligne centrale
        score_x_player2 = (WINDOW_WIDTH // 2) + 20  # 20px à droite de la ligne centrale
        score_y = WINDOW_HEIGHT - 30  # 30px depuis le haut

        # Affichage des scores
        arcade.draw_text(
            f"{self.player1.score}",
            score_x_player1,
            score_y,
            arcade.csscolor.WHITE,
            24,
            anchor_x="center"  # Centre le texte horizontalement
        )
        arcade.draw_text(
            f"{self.player2.score}",
            score_x_player2,
            score_y,
            arcade.csscolor.WHITE,
            24,
            anchor_x="center"  # Centre le texte horizontalement
        )

    def on_update(self, delta_time):
        self.ball_sprite_list.update()
        self.player_sprite_list.update()

        ball_hit_list = arcade.check_for_collision_with_list(self.ball, self.player_sprite_list)
        if len(ball_hit_list) > 0:
            self.ball.bounce()

    def on_key_press(self, symbol, modifiers):
        self.player1.register_key_press(symbol)
        self.player2.register_key_press(symbol)

    def on_key_release(self, symbol, modifiers):
        self.player1.register_key_release(symbol)
        self.player2.register_key_release(symbol)