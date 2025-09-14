
import arcade
from arcade.gui import UIManager, UIFlatButton, UISlider, UIBoxLayout, UILabel
from core import WINDOW_WIDTH, WINDOW_HEIGHT, BUTTON_STYLE, SLIDER_STYLE, settings

class SettingsView(arcade.View):
    """
    A view to display the game settings.
    
    Attributes:
        manager (UIManager): The UI manager for this view.
        v_box (arcade.gui.UIBoxLayout): The vertical box layout to hold the UI elements.
        volume_slider (UISlider): The slider to control the game volume.
        back_button (UIFlatButton): The button to go back to the previous view.
    """

    def __init__(self, previous_view: arcade.View):
        """
        Initializes the SettingsView.
        
        Args:
            previous_view (arcade.View): The view to return to when the back button is clicked.
        """
        super().__init__()
        self.previous_view = previous_view
        self.manager = UIManager()

        # Create a vertical box layout to hold the UI elements
        self.v_box = UIBoxLayout(x=WINDOW_WIDTH / 2 - 100, y=WINDOW_HEIGHT - 250, vertical=True, space_between=20)

        # Create the volume slider
        self.volume_slider = UISlider(
            value=settings.master_volume * 100,
            min_value=0,
            max_value=100,
            width=200,
            height=50,
            style=SLIDER_STYLE,
        )

        self.volume_slider.on_change = self.on_volume_change

        # Create a horizontal box layout to hold the volume icon and slider
        h_box = UIBoxLayout(vertical=False)
        
        # Add a text label for the volume icon
        volume_icon = UILabel(text="🔊", font_size=24)
        h_box.add(volume_icon)
        h_box.add(self.volume_slider)
        
        self.v_box.add(h_box)

        # Create the back button
        self.back_button = UIFlatButton(text="Back", width=200, height=50, style=BUTTON_STYLE)
        self.v_box.add(self.back_button)

        # Assign the on_click event for the back button
        self.back_button.on_click = self.on_click_back

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(self.v_box)

    def on_volume_change(self, event):
        """
        This function is called when the volume slider is changed.
        It updates the master volume setting.
        """
        settings.master_volume = self.volume_slider.value / 100

    def on_click_back(self, event):
        """
        This function is called when the back button is clicked.
        It returns to the previous view.
        """
        settings.save()
        self.window.show_view(self.previous_view)

    def on_show_view(self):
        """
        This method is called when the view is shown.
        """
        arcade.set_background_color(arcade.color.BLACK)
        self.manager.enable()

    def on_hide_view(self):
        """
        This method is called when the view is hidden.
        """
        self.manager.disable()

    def on_draw(self):
        """
        Draws the settings view.
        """
        self.clear()
        
        # Draw the title
        arcade.draw_text(
            "Settings",
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT - 100,
            arcade.color.WHITE,
            font_size=40,
            anchor_x="center"
        )
        
        self.manager.draw()
