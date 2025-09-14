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

BUTTON_STYLE = button_style = {
    'normal': {
        'font_color': arcade.color.WHITE,
        'bg': arcade.color.BLACK,
        'border': arcade.color.WHITE,
        'border_width': 2,
    },
    'hover': {
        'font_color': arcade.color.BLACK,
        'bg': arcade.color.WHITE,
        'border': arcade.color.WHITE,
        'border_width': 2,
    },
    'press': {
        'font_color': arcade.color.GRAY,
        'bg': arcade.color.DARK_GRAY,
        'border': arcade.color.WHITE,
        'border_width': 2,
    }
}

SLIDER_STYLE = {
    'normal': {
        'bg': arcade.color.WHITE,
        'border': arcade.color.DARK_GRAY,
        'border_width': 2,
        'filled_track': arcade.color.DARK_GRAY,
        'filled_step': arcade.color.PURPLE,
        'unfilled_track': arcade.color.LIGHT_GRAY,
        'unfilled_step': arcade.color.ORANGE,
    },
    'hover': {
        'bg': arcade.color.DARK_GRAY,
        'border': arcade.color.LIGHT_GRAY,
        'border_width': 2,
        'filled_track': arcade.color.DARK_GRAY,
        'filled_step': arcade.color.PURPLE,
        'unfilled_track': arcade.color.LIGHT_GRAY,
        'unfilled_step': arcade.color.ORANGE,
    },
    'press': {
        'bg': arcade.color.DARK_GRAY,
        'border': arcade.color.LIGHT_GRAY,
        'border_width': 2,
        'filled_track': arcade.color.DARK_GRAY,
        'filled_step': arcade.color.PURPLE,
        'unfilled_track': arcade.color.LIGHT_GRAY,
        'unfilled_step': arcade.color.ORANGE,
    },
}
