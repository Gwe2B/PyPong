"""
This module contains the KeyInput class, a UI component for changing key bindings.
"""

import arcade
from arcade.gui import UIBoxLayout, UIFlatButton, UILabel, UIKeyPressEvent, UIEvent

from core import settings
from core.constants import BUTTON_STYLE

class KeyInput(UIBoxLayout):
    """
    A UI component for displaying and changing a key binding.
    
    It consists of a label and a button. The button shows the current key,
    and when clicked, it waits for a new key press to update the binding.
    """

    def __init__(self, label: str, key_code: int):
        """
        Initializes the KeyInput component.
        
        Args:
            label (str): The label to display next to the key binding button.
            setting_key (str): The key in the settings dictionary to bind to.
        """
        super().__init__(vertical=False, space_between=10)
        
        self.key_code = key_code
        self.is_waiting_for_key = False

        # Create the label
        self.label = UILabel(text=label, width=100)
        self.add(self.label)

        # Create the button that shows the current key
        key_name = self.reverse_key_lookup(key_code)
        self.key_button = UIFlatButton(text=key_name, width=150, style=BUTTON_STYLE)
        self.key_button.on_click = self._on_key_button_click
        self.add(self.key_button)

    def on_key_change(self, symbol: int, modifiers: int):
        """
        A callback function that is called when the key binding is changed.
        
        Args:
            symbol (int): The new key code.
            modifiers (int): The modifiers that were held down.
        """
        pass

    def reverse_key_lookup(self, key_code: int) -> str | None:
        """
        Returns the string representation of a key code.
        
        Args:
            key_code (int): The key code to look up.
        
        Returns:
            str: The string representation of the key code.
        """
        # Get the key name from Arcade's key module
        for name, value in vars(arcade.key).items():
            if not name.startswith("__") and value == key_code:
                return name
        
        return None
    
    def _on_key_button_click(self, event):
        """
        Called when the key binding button is clicked.
        
        It sets the component to wait for a new key press.
        """
        self.is_waiting_for_key = True
        self.key_button.text = "Press a key..."

    def on_event(self, event: UIEvent):
        if isinstance(event, UIKeyPressEvent):
            self.on_key_press(event.symbol, event.modifiers)
            self.on_key_change(event.symbol, event.modifiers)
        else:
            super().on_event(event)

    def on_key_press(self, key: int, modifiers: int):
        """
        Called when a key is pressed.
        
        If the component is waiting for a key, it updates the binding.
        
        Args:
            key (int): The key that was pressed.
            modifiers (int): The modifiers that were held down.
        """
        if self.is_waiting_for_key:
            self.key_code = key
            self.key_button.text = self.reverse_key_lookup(key)
            self.is_waiting_for_key = False

class PlayerKeyBindings(UIBoxLayout):
    """
    A UI component for managing the key bindings of a single player.
    """

    def __init__(self, label: str, player_input_map):
        """
        Initializes the PlayerKeyBindings component.
        
        Args:
            player_number (int): The player number (1 or 2).
            player_input_map (dict): The dictionary mapping action names to key codes for the player.
        """
        super().__init__(vertical=True, space_between=10, align="right")

        self.keys = player_input_map

        # Title
        title = UILabel(text=label, font_size=18)
        self.add(title)

        # Key inputs
        self.up_input = KeyInput(label="Up", key_code=self.keys["up"])
        self.up_input.on_key_change = self.register_key_change("up")
        self.add(self.up_input)
        
        self.down_input = KeyInput(label="Down", key_code=self.keys["down"])
        self.add(self.down_input)

    def register_key_change(self, binding_name: str):
        return lambda symbol, modifiers: self.on_binding_change(binding_name, symbol)
    
    def on_binding_change(self, binding_name: str, new_key: int):
        """ A callback function that is called when a key binding is changed.
        Args:
            binding_name (str): The name of the binding that was changed.
            new_key (int): The new key code.
        """
        pass
