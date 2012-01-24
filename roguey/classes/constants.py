import os
MOVEMENT_SIZE = 16
RADIUS = 2
BLACK = (0,0,0)
WHITE = (255, 255, 255)
COLUMNS = 16
ROWS = 21
TREASURES = 10
WALLS = 30
MONSTERS = 3
TILE_SIZE = 48
DIRECTIONS = ['north', 'south', 'east', 'west']
ALL_TREASURES = {
                        "hat": "Quite cunning",
                        "sqord": "Knock-off sword. Probably from Ikea.",
                        "book": "What the hell are you going to do with this?",
			"rainbow": "Joy in a box."
                        }
LONG_STRING = "X" * 50

IMG_DIR = os.getcwd() + "/roguey/images/"
