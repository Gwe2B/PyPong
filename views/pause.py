
import arcade
from arcade.gui import UIManager, UIBoxLayout, UIFlatButton

from core import WINDOW_WIDTH, WINDOW_HEIGHT, BUTTON_STYLE
from views.settings import SettingsView


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

        # Create a vertical box layout to hold the buttons
        self.v_box = UIBoxLayout(
            x=WINDOW_WIDTH / 2 - 100,
            y=WINDOW_HEIGHT / 2 - 130,
            vertical=True,
            space_between=20
        )

        # Create the resume button
        resume_button = UIFlatButton(
            text="RESUME",
            width=200,
            height=50,
            style=BUTTON_STYLE
        )
        self.v_box.add(resume_button)

        # Create the settings button
        settings_button = UIFlatButton(
            text="SETTINGS",
            width=200,
            height=50,
            style=BUTTON_STYLE
        )
        self.v_box.add(settings_button)

        # Assign the on_click events
        resume_button.on_click = self.on_resume_button_click
        settings_button.on_click = self.on_settings_button_click

        # Create a widget to hold the v_box widget, that will center the buttons
        self.ui_manager.add(self.v_box)

    def on_resume_button_click(self, event):
        """
        Resumes the game when the resume button is clicked.
        """
        self.window.show_view(self.game_view)

    def on_settings_button_click(self, event):
        """
        Opens the settings view when the settings button is clicked.
        """
        self.window.show_view(SettingsView(self))

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
