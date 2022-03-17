import pygame

from config import *

class Alien(pygame.sprite.Sprite):
	# type means the shape of the alien,meanwhile position the layout of the arms
	def __init__(self, type, position, x, y):
		super().__init__()
		file_path = ALIEN_IMG['prefix'] + type + position + ALIEN_IMG['postfix']
		# lui aveva messo (file_path).convert_alpha ma a me cosí non andava
		self.image = pygame.image.load(file_path).convert_alpha()
		
		self.rect = self.image.get_rect(topleft = (x,y))

		if type == 'A':
			self.value = ALIEN_A_POINTS
		elif type == 'B':
			self.value = ALIEN_B_POINTS
		else:
			self.value = ALIEN_C_POINTS

	def update(self, direction):
			self.rect.x += direction

class Extra(pygame.sprite.Sprite):
	def __init__(self, side):
		super().__init__()
		self.image = pygame.image.load(EXTRA_IMG).convert_alpha()
		if side == 'right':
			x = WIDTH + EXTRA_X_OFFSET
			self.speed = -EXTRA_SPEED
		else:
			x = -EXTRA_X_OFFSET
			self.speed = EXTRA_SPEED

		self.rect = self.image.get_rect(topleft = (x, EXTRA_Y_START_POS))

	def update(self):
		self.rect.x += self.speed