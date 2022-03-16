import sys
import pygame
from re import X

from config import *
from game import Game
from player import Player
import obstacle
from alien import Alien, Extra
from random import choice, randint
from laser import Laser

if __name__ == '__main__':
	pygame.init()
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()

	alien_laser = pygame.USEREVENT + 1
	pygame.time.set_timer(alien_laser, ALIEN_LASER_RESET_TIME)

	game = Game(alien_laser)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == alien_laser:
				game.alien_shoot()

		window.fill(BG_COLOR)

		game.run()

		pygame.display.flip()
		clock.tick(60)