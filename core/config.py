"""
This module provides a class to manage game settings.
"""
import pickle
from pathlib import Path
import arcade

from core.constants import DEFAULT_SETTINGS

class Settings:
    """
    A class to manage game settings.

    This class handles loading, saving, and providing access to game settings.
    Settings are stored in a binary file and can be accessed as attributes.
    """

    def __init__(self, config_file: str = "pypong.settings"):
        """
        Initialize the Settings class.
        """
        object.__setattr__(self, "_config_file", Path(config_file))
        # Set _config to defaults initially to ensure they always exist.
        object.__setattr__(self, "_config", self._get_default_settings())
        self.load()

    def load(self):
        """
        Load settings from the config file.

        If the file exists, it's loaded and its values overwrite the defaults.
        If not, the default settings are saved to a new file.
        """
        if self._config_file.exists():
            try:
                with open(self._config_file, "rb") as f:
                    loaded_config = pickle.load(f)
                    self._config.update(loaded_config) # Merge loaded config
                self.save() # Save to add any new default keys to the file
                return
            except (pickle.UnpicklingError, EOFError):
                # File is corrupted or empty, save defaults over it
                self.save()
        else:
            # File doesn't exist, save the defaults
            self.save()

    def _get_default_settings(self) -> dict:
        """Return a dictionary with the default settings."""
        return DEFAULT_SETTINGS

    def save(self):
        """Save the current settings to the config file."""
        with open(self._config_file, "wb") as f:
            pickle.dump(self._config, f)

    def __getattr__(self, name):
        """Get a setting from the config dictionary."""
        if name in self._config:
            return self._config[name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        """Set a setting in the config dictionary and save to file."""
        if name.startswith("_"):
            object.__setattr__(self, name, value)
        else:
            self._config[name] = value
            #self.save()

# Create a single instance of the Settings class to be used throughout the application
settings = Settings()