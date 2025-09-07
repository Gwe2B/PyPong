import arcade
from core.constants import WINDOW_WIDTH, WINDOW_HEIGHT

class Ball(arcade.Sprite):
    def __init__(self, pos_x: int, pos_y: int, velocity_x: float, velocity_y: float, radius: int = 15, color = arcade.csscolor.WHITE):
        super().__init__()

        self.texture = arcade.make_circle_texture(radius * 2, color)

        self.center_x = pos_x
        self.center_y = pos_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.radius = radius

    def update(self, delta_time: float = 1/60):
        # Move the ball
        self.center_y += self.velocity_y
        self.center_x += self.velocity_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.center_x < self.radius:
            self.velocity_x *= -1

        if self.center_x > WINDOW_WIDTH - self.radius:
            self.velocity_x *= -1

        if self.center_y < self.radius:
            self.velocity_y *= -1

        if self.center_y > WINDOW_HEIGHT - self.radius:
            self.velocity_y *= -1
