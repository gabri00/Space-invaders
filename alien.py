import pygame

class Alien(pygame.sprite.Sprite):
	def __init__(self, color):
		super().__init__()
		self.image