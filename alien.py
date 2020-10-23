import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
	'''
	A class that represents each alien
	'''
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen

		# Load the alien image and set its rect
		self.image = pygame.image.load('Images/alien.bmp')
		self.rect = self.image.get_rect()

		# Start new alien near the top left
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's position as float
		self.x = float(self.rect.x)