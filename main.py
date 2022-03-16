import sys
import pygame

from game import Game
from player import Player
import obstacle
from alien import Alien, Extra
from random import choice, randint
from laser import Laser

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
		self.alien_direction = 1
		self.alien_lasers = pygame.sprite.Group()

		#Extra setup
		self.extra = pygame.sprite.GroupSingle()
		self.extra_spown_time = randint(40,80)

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

	def aliens_setup(self,rows,cols, x_distance = 60, y_distance = 48, x_offset = 70, y_offset = 20):
		for i, row in enumerate(range(rows)):
			for j, col in enumerate(range(cols)):
				x = j * x_distance + x_offset
				y = i * y_distance + y_offset
				if i == 0: 			alien_sprite = Alien('A', '1', x, y)
				elif 1 <= i <= 2: 	alien_sprite = Alien('B', '1', x, y)
				else: 				alien_sprite = Alien('C', '1', x, y)
			
				self.aliens.add(alien_sprite)
		
	def alien_position_checker(self):
		all_aliens = self.aliens.sprites()
		for alien in all_aliens:
			if alien.rect.right >= WIDTH:
				self.alien_direction = -1
				self.alien_move__down(1)
			elif alien.rect.left <= 0:
				self.alien_direction = 1
				self.alien_move__down(1)

	def alien_move__down(self,distance):
		if self.aliens:
			for alien in self.aliens.sprites():
				alien.rect.y += distance
	
	def alien_shoot(self):
		if self.aliens.sprites():
			random_alien = choice(self.aliens.sprites())
			laser_sprite = Laser(random_alien.rect.center, 6, HEIGHT)
			self.alien_lasers.add(laser_sprite)

	def extra_alien_timer(self):
		self.extra_spown_time -=1
		if self.extra_spown_time <= 0:
			self.extra.add(Extra(choice(['right', 'left']),WIDTH))
			self.extra_spown_time = randint(400,800)

	def run(self):
		self.player.update()
		self.aliens.update(self.alien_direction)
		self.alien_position_checker()
		self.alien_lasers.update()
		self.extra_alien_timer()
		self.extra.update()

		self.player.sprite.lasers.draw(window)
		self.player.draw(window)

		self.blocks.draw(window)
		self.aliens.draw(window)
		self.alien_lasers.draw(window)
		self.extra.draw(window)



if __name__ == '__main__':
	pygame.init()
	WIDTH, HEIGHT = 600, 600
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()
	game = Game()

	ALIENLASER = pygame.USEREVENT + 1
	pygame.time.set_timer(ALIENLASER,800) # the time every shoot from aliens is 800 millisecond

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == ALIENLASER:
				game.alien_shoot()

		window.fill((30, 30, 30))

		game.run()

		pygame.display.flip()
		clock.tick(60)