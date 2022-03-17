import sys
import pygame
from random import choice, randint

from config import *
from player import Player
from alien import Alien, Extra
from laser import Laser
import obstacle

class Game:
	def __init__(self, window):
		self.window = window

		# Player setup
		player_sprite = Player((WIDTH / 2, HEIGHT), WIDTH, 5)
		self.player = pygame.sprite.GroupSingle(player_sprite) # GroupSingle -> contains only one sprite, when a new one is added the last will be deleted
		
		# health and score setup
		self.lives = MAX_LIVES
		self.life_surf = pygame.image.load(SHIP_IMG).convert_alpha()
		self.life_x_start_pos = WIDTH - (self.life_surf.get_size()[0] * 2 + 20)
		self.score = 0
		self.font = pygame.font.Font(FONT, FONT_SIZE)

		# Obstacle setup
		self.shape = obstacle.shape
		self.block_size = BLOCK_SIZE
		self.blocks = pygame.sprite.Group()
		self.obstacle_amount = BLOCK_AMOUNT
		self.obstacle_x_positions = [num * (WIDTH / self.obstacle_amount) for num in range(self.obstacle_amount)]
		self.create_obstacle_grid(*self.obstacle_x_positions, x_start = WIDTH / 15, y_start = 520)

		# Alien setup 
		self.aliens = pygame.sprite.Group()
		self.aliens_setup(rows = ALIENS_GRID['rows'], cols = ALIENS_GRID['cols']) # number of alien that we will have
		self.aliens.speed = ALIENS_SPEED
		self.alien_direction = ALIENS_SPEED['x']
		self.alien_lasers = pygame.sprite.Group()

		#Extra setup
		self.extra = pygame.sprite.GroupSingle()
		self.extra_spown_time = randint(EXTRA_SPAWN_TIME['min'], EXTRA_SPAWN_TIME['max'])

	def create_obstacle(self, x_start, y_start, offset_x):
		for i, row in enumerate(self.shape):
			for j, col in enumerate(row):
				if col == 'x':
					x = x_start + j * self.block_size + offset_x
					y = y_start + i * self.block_size
					block = obstacle.Block(self.block_size, BLOCK_COLOR, x, y)
					self.blocks.add(block)

	def create_obstacle_grid(self, *offset, x_start, y_start):
		for x in offset:
			self.create_obstacle(x_start, y_start, x)

	def aliens_setup(self, rows, cols, x_distance = 60, y_distance = 48, x_offset = 70, y_offset = 130):
		for i, row in enumerate(range(rows)):
			for j, col in enumerate(range(cols)):
				x = j * x_distance + x_offset
				y = i * y_distance + y_offset
				if i == 0:
					alien_sprite = Alien('A', '1', x, y)
				elif 1 <= i <= 2:
					alien_sprite = Alien('B', '1', x, y)
				else:
					alien_sprite = Alien('C', '1', x, y)
			
				self.aliens.add(alien_sprite)
		
	def alien_position_checker(self):
		all_aliens = self.aliens.sprites()
		for alien in all_aliens:
			if alien.rect.right >= WIDTH:
				self.alien_direction = -ALIENS_SPEED['x']
				self.alien_move_down()
			elif alien.rect.left <= 0:
				self.alien_direction = ALIENS_SPEED['x']
				self.alien_move_down()

	def alien_move_down(self):
		if self.aliens:
			for alien in self.aliens.sprites():
				alien.rect.y += ALIENS_SPEED['y']

	def alien_shoot(self):
		if self.aliens.sprites():
			random_alien = choice(self.aliens.sprites())
			laser_sprite = Laser(random_alien.rect.center, ALIEN_LASER_SPEED, HEIGHT, 'white')
			self.alien_lasers.add(laser_sprite)

	def extra_alien_timer(self):
		self.extra_spown_time -=1
		if self.extra_spown_time <= 0:
			self.extra.add(Extra(choice(['right', 'left'])))
			self.extra_spown_time = randint(EXTRA_SPAWN_TIME['min'], EXTRA_SPAWN_TIME['max'])

	def check_collisions(self):
		#player lasers
		if self.player.sprite.lasers:
			for laser in self.player.sprite.lasers:
				# obstacle collisions
				if pygame.sprite.spritecollide(laser, self.blocks, True):
					laser.kill()

				# alien collisions
				aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
				if aliens_hit:
					for alien in aliens_hit:
						self.score += alien.value
					laser.kill()

				# extra collisions
				if pygame.sprite.spritecollide(laser, self.extra, True):
					self.score += EXTRA_SCORE
					laser.kill()

		# alien lasers
		if self.alien_lasers:
			for laser in self.alien_lasers:
				# obstacle collisions
				if pygame.sprite.spritecollide(laser, self.blocks, True):
					laser.kill()

				if pygame.sprite.spritecollide(laser, self.player, False):
					laser.kill()
					self.lives -= 1
					if self.lives <= 0:
						pygame.quit()
						sys.exit()

		# aliens
		if self.aliens:
			for alien in self.aliens:
				pygame.sprite.spritecollide(alien, self.blocks, True)

				if pygame.sprite.spritecollide(alien, self.blocks, False):
					pygame.quit()
					sys.exit()

	def display_lives(self):
		for life in range(self.lives - 1):
			x = self.life_x_start_pos + (life * (self.life_surf.get_size()[0] + 10))
			self.window.blit(self.life_surf, (x, 10))

	def display_score(self):
		score_surf = self.font.render(f'score: {self.score}', False, SCORE_COLOR)
		score_rect = score_surf.get_rect(topleft = SCORE_POS)
		self.window.blit(score_surf, score_rect)

	def run(self):
		self.player.update()
		self.alien_lasers.update()
		self.extra.update()
		self.aliens.update(self.alien_direction)

		self.alien_position_checker()
		self.extra_alien_timer()
		self.check_collisions()

		self.player.sprite.lasers.draw(self.window)
		self.player.draw(self.window)
		self.blocks.draw(self.window)
		self.aliens.draw(self.window)
		self.alien_lasers.draw(self.window)
		self.extra.draw(self.window)

		self.display_lives()
		self.display_score()