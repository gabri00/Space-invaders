import pygame

from config import *

class Laser(pygame.sprite.Sprite):
	def __init__(self, pos, speed, screen_height, color):
		super().__init__()
		self.image = pygame.Surface(LASER_DIMENS)
		self.image.fill(color)
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed
		self.height_y_constraint = screen_height

	def destroy(self):
		if self.rect.y <= -10 or self.rect.y >= self.height_y_constraint + 50:
			self.kill()

	def update(self):
		self.rect.y += self.speed
		self.destroy()
