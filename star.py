import pygame
from pygame.sprite import Sprite 
from random import randint


class Star(Sprite):

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the star image and set its rect
		size = randint(1,3)
		if size == 1:
			self.image = pygame.image.load('Images/stars_smll.bmp')
		elif size == 2:
			self.image = pygame.image.load('Images/stars_med.bmp')
		elif size == 3:
			self.image = pygame.image.load('Images/stars_large.bmp')

		self.rect = self.image.get_rect()

		# Start new star near the top left
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#self.y = float(self.rect.y)



	def update(self):
		'''
		Move the star through the screen
		'''
		self.rect.y += self.settings.star_speed*randint(0,3)
		

