from game_of_life import game_of_life
from start_screen import start_screen
from brians_brain import brians_brain


def main():
    simulation = start_screen()

    if simulation == "Game of Life":
        game_of_life()
    elif simulation == "Brian's Brain":
        brians_brain()


if __name__ == "__main__":
    main()
