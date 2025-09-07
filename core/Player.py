from typing import Mapping
import arcade

from core.constants import WINDOW_HEIGHT

class Player(arcade.Sprite):
    PLAYER_WIDTH = 10
    PLAYER_HEIGHT = 100
    STEP_INCREMENT = 5

    def __init__(self, pos_x: int, pos_y: int, input_map: Mapping[str, int]):
        super().__init__()
        # Création d'une texture rectangulaire blanche
        self.texture = arcade.make_soft_square_texture(
            max(Player.PLAYER_WIDTH, Player.PLAYER_HEIGHT),
            arcade.csscolor.WHITE,
            outer_alpha=255
        )
        self.width = Player.PLAYER_WIDTH
        self.height = Player.PLAYER_HEIGHT
        self.center_x = pos_x + self.width // 2
        self.center_y = pos_y + self.height // 2
        self.input_map = input_map
        self.key_press_state = {
            "up": False,
            "down": False,
        }

    def register_key_press(self, key):
        if not key in self.input_map.values():
            pass

        if key == self.input_map.get("up"):
            self.key_press_state["up"] = True
        elif key == self.input_map.get("down"):
            self.key_press_state["down"] = True

    def register_key_release(self, key):
        if not key in self.input_map.values():
            pass

        if key == self.input_map.get("up"):
            self.key_press_state["up"] = False
        elif key == self.input_map.get("down"):
            self.key_press_state["down"] = False

    def update(self, delta_time: float = 1/60):
        if self.key_press_state["up"]:
            self.center_y += self.STEP_INCREMENT
        
        if self.key_press_state["down"]:
            self.center_y -= self.STEP_INCREMENT

        if self.center_y < (self.PLAYER_HEIGHT/2):
            self.center_y = self.PLAYER_HEIGHT/2
        elif (self.center_y + (self.PLAYER_HEIGHT/2)) >  WINDOW_HEIGHT:
            self.center_y = WINDOW_HEIGHT - (self.PLAYER_HEIGHT/2)