import arcade
from core.constants import WINDOW_WIDTH, WINDOW_HEIGHT

class Ball:
    def __init__(self, pos_x: int, pos_y: int, velocity_x: float, velocity_y: float, radius: int = 15, color = arcade.csscolor.WHITE):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radius, self.color)

    def on_update(self):
        # Move the ball
        self.pos_y += self.velocity_y
        self.pos_x += self.velocity_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.pos_x < self.radius:
            self.velocity_x *= -1

        if self.pos_x > WINDOW_WIDTH - self.radius:
            self.velocity_x *= -1

        if self.pos_y < self.radius:
            self.velocity_y *= -1

        if self.pos_y > WINDOW_HEIGHT - self.radius:
            self.velocity_y *= -1
