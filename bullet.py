import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''
	A class that manages the bullets firesd from the ship
	'''

	def __init__(self, ai_game):
		'''
		Create a bullet object at the ship's position
		'''
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		# Create a bullet rect at (0,0) and correct the position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		# Store the bullet's position as float
		self.y = float(self.rect.y)


	def update(self):
		'''
		Move the bullet through the screen
		'''
		# Update decimal position of the bullet
		self.y -= self.settings.bullet_speed
		# Update the rect position
		self.rect.y = self.y


	def draw_bullet(self):
		'''
		Draw's the bullet in the screen
		'''
		pygame.draw.rect(self.screen, self.color, self.rect)