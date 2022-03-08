from re import X
import pygame
import sys

from player import Player
import obstacle
from alien import Alien

class Game:
	def __init__(self):
		# Player setup
		player_sprite = Player((WIDTH / 2, HEIGHT), WIDTH, 5)
		self.player = pygame.sprite.GroupSingle(player_sprite) # GroupSingle is a class that contains only one sprite.
															   # When one more is added the last will be deleted
		# Obstacle setup
		self.shape = obstacle.shape
		self.block_size = 6
		self.blocks = pygame.sprite.Group()
		self.obstacle_amount = 4
		self.obstacle_x_positions = [num * (WIDTH / self.obstacle_amount) for num in range(self.obstacle_amount)]
		self.create_obstacle_grid(*self.obstacle_x_positions, x_start = WIDTH / 15, y_start = 480)

		# Alien setup 
		self.aliens = pygame.sprite.Group()
		self.aliens_setup(rows = 6, cols = 8) # number of alien that we will have

	def create_obstacle(self, x_start, y_start, offset_x):
		for i, row in enumerate(self.shape):
			for j, col in enumerate(row):
				if col == 'x':
					x = x_start + j * self.block_size + offset_x
					y = y_start + i * self.block_size
					block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
					self.blocks.add(block)

	def create_obstacle_grid(self, *offset, x_start, y_start):
		for x in offset:
			self.create_obstacle(x_start, y_start, x)

	def aliens_setup(self,rows,cols, x_distance = 60, y_distance = 48, x_offset = 70, y_offset = 100):
		for i, row in enumerate(range(rows)):
			for j, col in enumerate(range(cols)):
				x = j * x_distance + x_offset
				y = i * y_distance + y_offset
				if i == 0: 			alien_sprite = Alien('A', '1', x, y)
				elif 1 <= i <= 2: 	alien_sprite = Alien('B', '1', x, y)
				else: 				alien_sprite = Alien('C', '1', x, y)
			
				self.aliens.add(alien_sprite)
		
	def run(self):
		self.player.update()
		self.player.sprite.lasers.draw(window)
		self.player.draw(window)
		self.blocks.draw(window)
		self.aliens.draw(window)



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