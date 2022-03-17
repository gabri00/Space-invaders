import sys
import pygame

from config import *
from game import Game

if __name__ == '__main__':
	pygame.init()
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()

	ALIENLASER = pygame.USEREVENT + 1
	pygame.time.set_timer(ALIENLASER, ALIEN_LASER_RESET_TIME)

	game = Game(window)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == ALIENLASER:
				game.alien_shoot()

		window.fill(BG_COLOR)

		game.run()

		pygame.display.flip()
		clock.tick(60)