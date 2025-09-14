import arcade
from arcade.gui import UIManager, UIFlatButton, UISlider, UIBoxLayout, UILabel
from core import WINDOW_WIDTH, WINDOW_HEIGHT, BUTTON_STYLE, SLIDER_STYLE, settings
from views.key_input import PlayerKeyBindings, KeyInput

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
        self._active_key_input: KeyInput | None = None

        # Create a vertical box layout to hold the UI elements
        self.v_box = UIBoxLayout(x=WINDOW_WIDTH / 2 - 250, y=WINDOW_HEIGHT - 470, vertical=True, space_between=20)

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
        volume_box = UIBoxLayout(vertical=False, space_between=10)
        
        # Add a text label for the volume icon
        volume_icon = UILabel(text="🔊", font_size=24)
        volume_box.add(volume_icon)
        volume_box.add(self.volume_slider)
        
        self.v_box.add(volume_box)

        # Create the key bindings section
        pause_key_input = KeyInput(label="Pause", key_code=settings.pause_key, on_click_callback=self._set_active_key_input)
        pause_key_input.on_key_change = lambda symbol, modifiers: self.on_binding_key_change("pause_key", symbol)
        self.v_box.add(pause_key_input)

        key_bindings_box = UIBoxLayout(vertical=False, space_between=50)
        # Create player 1 key bindings
        self.player1_bindings = PlayerKeyBindings("Player 1", settings.player1_keys, on_key_input_click_callback=self._set_active_key_input)
        self.player1_bindings.on_binding_change = lambda name, key: self.on_binding_change("player1_keys", name, key)
        key_bindings_box.add(self.player1_bindings)

        # Create player 2 key bindings
        self.player2_bindings = PlayerKeyBindings("Player 2", settings.player2_keys, on_key_input_click_callback=self._set_active_key_input)
        self.player2_bindings.on_binding_change = lambda name, key: self.on_binding_change("player2_keys", name, key)
        key_bindings_box.add(self.player2_bindings)
        
        self.v_box.add(key_bindings_box)

        # Create the back button
        self.back_button = UIFlatButton(text="Back", width=200, height=50, style=BUTTON_STYLE)
        self.v_box.add(self.back_button)

        # Assign the on_click event for the back button
        self.back_button.on_click = self.on_click_back

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(self.v_box)

    def _set_active_key_input(self, key_input: KeyInput):
        if self._active_key_input:
            self._active_key_input.is_waiting_for_key = False
            self._active_key_input.key_button.text = self._active_key_input.reverse_key_lookup(self._active_key_input.key_code)
        self._active_key_input = key_input

    def on_key_press(self, key: int, modifiers: int):
        if self._active_key_input:
            self._active_key_input.set_key(key)
            self._active_key_input = None

    def on_volume_change(self, event):
        """
        This function is called when the volume slider is changed.
        It updates the master volume setting.
        """
        settings.master_volume = self.volume_slider.value / 100
    
    def on_binding_key_change(self, setting_attr: str, new_key: int):
        """
        A callback function that is called when a key binding is changed.
        Args:
            setting_attr (str): The attribute name in the settings module (e.g., "pause_key").
            new_key (int): The new key code.
        """
        settings.__setattr__(setting_attr, new_key)

    def on_binding_change(self, setting_attr, binding_name: str, new_key: int):
        """
        A callback function that is called when a key binding is changed.
        Args:
            setting_attr (str): The attribute name in the settings module (e.g., "player1_keys").
            binding_name (str): The name of the binding that was changed.
            new_key (int): The new key code.
        """
        key_map = getattr(settings, setting_attr)
        key_map[binding_name] = new_key
        setattr(settings, setting_attr, key_map)

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