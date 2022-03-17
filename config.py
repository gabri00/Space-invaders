# window
WIDTH = 600
HEIGHT = 650
BG_COLOR = (30, 30, 30)

# images
SHIP_IMG = 'images/ship.png'
EXTRA_IMG = 'images/extra.png'
ALIEN_IMG = {
	'prefix': 'images/invader_',
	'postfix': '.png'
}

# font
FONT = 'fonts/unifont.ttf'
FONT_SIZE = 20

# obstacles
BLOCK_SIZE = 6
BLOCK_AMOUNT = 4
BLOCK_COLOR = (241, 79, 80)

# aliens
ALIENS_GRID = {
	'rows': 6,
	'cols': 8
}
ALIENS_SPEED = 1
ALIEN_LASER_RESET_TIME = 800 # ms
ALIENS_SPEED = {
	'x': 1,
	'y': 1
}

# laser
LASER_DIMENS = (4, 20)
PLAYER_LASER_COOLDOWN = 500
PLAYER_LASER_COLOR = 'green'
PLAYER_LASER_SPEED = -8
ALIEN_LASER_SPEED = 6

# extra alien
EXTRA_SPAWN_TIME = {
	'min': 400,
	'max': 800
}
EXTRA_SPEED = 3
EXTRA_X_OFFSET = 50
EXTRA_Y_START_POS = 65

# health
MAX_LIVES = 3

# score
SCORE_POS = (10, 20)
SCORE_COLOR = 'white'
EXTRA_SCORE = 800
ALIEN_A_POINTS = 300
ALIEN_B_POINTS = 200
ALIEN_C_POINTS = 100