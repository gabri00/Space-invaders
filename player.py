import pygame

from config import *
from laser import Laser

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, constraint, speed):
		super().__init__()
		self.image = pygame.image.load(SHIP_IMG).convert_alpha()
		self.rect = self.image.get_rect(midbottom = pos)
		self.speed = speed
		self.max_x_constraint = constraint
		self.ready = True
		self.laser_time = 0
		self.laser_cooldown = PLAYER_LASER_COOLDOWN
		self.lasers = pygame.sprite.Group()

	def move(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			if self.rect.right < self.max_x_constraint:
				self.rect.x += self.speed
		elif keys[pygame.K_LEFT]:
			if self.rect.left > 0:
				self.rect.x -= self.speed

		if keys[pygame.K_SPACE] and self.ready:
			self.shoot()
			self.ready = False
			self.laser_time = pygame.time.get_ticks()

	def recharge(self):
		if not self.ready:
			current_time = pygame.time.get_ticks()
			if current_time - self.laser_time >= self.laser_cooldown:
				self.ready = True



	def shoot(self):
		self.lasers.add(Laser(self.rect.center, PLAYER_LASER_SPEED, self.rect.bottom, PLAYER_LASER_COLOR))

	def update(self):
		self.move()
		self.recharge()
		self.lasers.update()