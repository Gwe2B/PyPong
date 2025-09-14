import arcade

from views import GameView
from core import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()