import pygame
import sys

from player import Player

class Game:
	def __init__(self):
		player_sprite = Player((WIDTH / 2, HEIGHT), WIDTH, 5)
		self.player = pygame.sprite.GroupSingle(player_sprite)

	def run(self):
		self.player.update()
		self.player.draw(window)



if __name__ == '__main__':
	pygame.init()
	WIDTH, HEIGHT = 600, 600
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()
	game = Game()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		window.fill((30, 30, 30))

		game.run()

		pygame.display.flip()
		clock.tick(60)