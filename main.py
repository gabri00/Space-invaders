import pygame
import sys

from player import Player
import obstacle

class Game:
	def __init__(self):
		player_sprite = Player((WIDTH / 2, HEIGHT), WIDTH, 5)
		self.player = pygame.sprite.GroupSingle(player_sprite) # GroupSingle is a class that contains only one sprite.
															   # When one more is added the last will be deleted
		self.shape = obstacle.shape
		self.block_size = 6
		self.blocks = pygame.sprite.Group()
		self.obstacle_amount = 4
		self.obstacle_x_positions = [num * (WIDTH / self.obstacle_amount) for num in range(self.obstacle_amount)]
		self.create_blocks_grid(*self.obstacle_x_positions, x_start = WIDTH / 15, y_start = 480)

	def create_block(self, x_start, y_start, offset_x):
		for i, row in enumerate(self.shape):
			for j, col in enumerate(row):
				if col == 'x':
					x = x_start + j * self.block_size + offset_x
					y = y_start + i * self.block_size
					block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
					self.blocks.add(block)

	def create_blocks_grid(self, *offset, x_start, y_start):
		for x in offset:
			self.create_block(x_start, y_start, x)

	def run(self):
		self.player.update()
		self.player.sprite.lasers.draw(window)
		self.player.draw(window)
		self.blocks.draw(window)



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