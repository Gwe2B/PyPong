
import arcade
from arcade.gui import UIManager, UIFlatButton

from core import WINDOW_WIDTH, WINDOW_HEIGHT


class PauseView(arcade.View):
    """
    A view to display when the game is paused.

    This view darkens the screen and displays a "PAUSED" message.
    It waits for the user to press the 'P' key to resume the game.

    Attributes:
        game_view (arcade.View): The view to return to when the game is unpaused.
    """

    def __init__(self, game_view: arcade.View):
        """
        Initializes the PauseView.

        Args:
            game_view (arcade.View): The view to return to when the game is unpaused.
        """
        super().__init__()
        self.game_view = game_view
        self.ui_manager = UIManager()

        resume_button = UIFlatButton(
            text="RESUME",
            width=200,
            height=50,
        )

        resume_button.with_background(color=arcade.color.BLACK)
        resume_button.with_border(width=2, color=arcade.color.WHITE)
        resume_button.center_x = WINDOW_WIDTH / 2
        resume_button.center_y = WINDOW_HEIGHT / 2 - 100
        self.ui_manager.add(resume_button)

        resume_button.on_click = self.on_resume_button_click

    def on_resume_button_click(self, event):
        """
        Resumes the game when the resume button is clicked.
        """
        self.window.show_view(self.game_view)

    def on_show_view(self):
        """
        Called when this view is shown.

        This method sets the background color to a semi-transparent black to
        darken the game screen.
        """
        arcade.set_background_color(arcade.color.BLACK)
        self.ui_manager.enable()

    def on_hide_view(self):
        """
        Called when this view is hidden.

        This method disables the UI manager.
        """
        self.ui_manager.disable()

    def on_draw(self):
        """
        Draws the pause screen.

        This method first draws the game view (to keep it visible in the
        background), then draws a semi-transparent overlay, and finally
        displays the "PAUSED" text.
        """
        self.clear()

        # Draw the game view as a background.
        # This gives the effect of a semi-transparent overlay.
        self.game_view.on_draw()

        # Draw a semi-transparent black rectangle to darken the screen
        arcade.draw_lrbt_rectangle_filled(
            0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, (0, 0, 0, 150)
        )

        # Display the "PAUSED" text
        arcade.draw_text(
            "PAUSED",
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT / 2,
            arcade.color.WHITE,
            font_size=64,
            anchor_x="center",
        )
        self.ui_manager.draw()
