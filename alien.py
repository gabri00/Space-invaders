import pygame

class Alien(pygame.sprite.Sprite):
	# type means the shape of the alien,meanwhile position the layout of the arms
	def __init__(self, type, position, x, y):
		super().__init__()
		file_path = 'images/invader_' + type + position + '.png'
		# lui aveva messo (file_path).convert_alpha ma a me cosí non andava
		self.image = pygame.image.load(file_path)
		
		self.rect = self.image.get_rect(topleft = (x,y))