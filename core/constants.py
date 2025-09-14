import arcade

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Pong"

DEFAULT_SETTINGS = {
    "master_volume": 1.0,
    "pause_key": arcade.key.P,
    "player1_keys": {
        "up": arcade.key.Z,
        "down": arcade.key.S,
    },
    "player2_keys": {
        "up": arcade.key.O,
        "down": arcade.key.L,
    },
}