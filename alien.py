import pygame

class Alien(pygame.sprite.Sprite):
	# type means the shape of the alien,meanwhile position the layout of the arms
	def __init__(self, type, position, x, y):
		super().__init__()
		file_path = 'images/invader_' + type + position + '.png'
		# lui aveva messo (file_path).convert_alpha ma a me cosí non andava
		self.image = pygame.image.load(file_path)
		
		self.rect = self.image.get_rect(topleft = (x,y))

		if type == 'A':
			self.value = 100
		elif type == 'B':
			self.value = 200
		else:
			self.value = 300


def update(self,direction):
		self.rect.x += direction

class Extra(pygame.sprite.Sprite):
	def __init__(self,side,WIDTH):
		super().__init__()
		self.image = pygame.image.load('images/extra.png').convert_alpha()
		if side == 'right':
			x = WIDTH + 50
			self.speed = -3
		else:
			x = -50
			self.speed = 3

		self.rect = self.image.get_rect(topleft = (x,10))

	def update(self):
		self.rect.x += self.speed