import arcade
from core.constants import WINDOW_WIDTH, WINDOW_HEIGHT

class Ball(arcade.Sprite):
    def __init__(self, pos_x: int, pos_y: int, velocity_x: float, velocity_y: float, delta_vx: float = 0.2, radius: int = 15, color = arcade.csscolor.WHITE):
        """Ball constructor

        Args:
            pos_x (int): Initial X position of the ball
            pos_y (int): Initial Y position of the ball
            velocity_x (float): Initial velocity on the X axis
            velocity_y (float): Initial velocity on the Y axis
            delta_vx (float, optional): Increment in speed at each call to the bounce method. Defaults to 0.2.
            radius (int, optional): Radius of the ball. Defaults to 15.
            color (_type_, optional): Color of the ball. Defaults to arcade.csscolor.WHITE.
        """

        super().__init__()

        self.texture = arcade.make_circle_texture(radius * 2, color)

        self.initial_x = pos_x
        self.initial_y = pos_y
        self.inital_x_velocity = abs(velocity_x)

        self.center_x = pos_x
        self.center_y = pos_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.delta_vx = delta_vx
        self.radius = radius

        self.on_side_wall_hit = None

    def update(self, delta_time: float = 1/60):
        # Move the ball
        self.center_y += self.velocity_y
        self.center_x += self.velocity_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.center_x < self.radius:
            if self.on_side_wall_hit:
                self.on_side_wall_hit("left")
            self.velocity_x *= -1

        if self.center_x > WINDOW_WIDTH - self.radius:
            if self.on_side_wall_hit:
                self.on_side_wall_hit("right")
            self.velocity_x *= -1

        if self.center_y < self.radius:
            self.velocity_y *= -1

        if self.center_y > WINDOW_HEIGHT - self.radius:
            self.velocity_y *= -1
    
    def bounce(self):
        self.velocity_x *= -1
        if self.velocity_x > 0:
            self.velocity_x += self.delta_vx
        else:
            self.velocity_x -= self.delta_vx

    def reset(self):
        velocity_x = self.inital_x_velocity
        if (self.velocity_x < 0):
            velocity_x *= -1

        self.center_x = self.initial_x
        self.center_y = self.initial_y
        self.velocity_x = velocity_x
