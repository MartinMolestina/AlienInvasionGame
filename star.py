import pygame
from pygame.sprite import Sprite 


class Star(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen

		# Load the star image and set its rect
		self.image = pygame.image.load('Images/stars.bmp')
		self.rect = self.image.get_rect()

		# Start new star near the top left
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

