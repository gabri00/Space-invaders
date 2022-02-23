import pygame
import sys

if __name__ == '__main__':
	pygame.init()
	WIDTH, HEIGHT = 600, 600
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		window.fill((30, 30, 30))

		clock.tick(60)