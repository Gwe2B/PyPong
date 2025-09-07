from typing import Mapping
import arcade

from core.constants import WINDOW_HEIGHT

class Player:
    PLAYER_WIDTH = 10
    PLAYER_HEIGHT = 100
    STEP_INCREMENT = 5

    def __init__(self, pos_x: int, pos_y: int, input_map: Mapping[str, int]):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.input_map = input_map

        self.key_press_state = {
            "up": False,
            "down": False,
        }

    def draw(self):
        arcade.draw_lbwh_rectangle_filled(self.pos_x, self.pos_y, self.PLAYER_WIDTH, self.PLAYER_HEIGHT, arcade.csscolor.WHITE)

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

    def on_update(self):
        if self.key_press_state["up"]:
            self.pos_y += self.STEP_INCREMENT
        
        if self.key_press_state["down"]:
            self.pos_y -= self.STEP_INCREMENT

        if self.pos_y < 0:
            self.pos_y = 0
        elif (self.pos_y + self.PLAYER_HEIGHT) >  WINDOW_HEIGHT:
            self.pos_y = WINDOW_HEIGHT - self.PLAYER_HEIGHT