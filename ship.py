import pygame

class Ship:
	'''
	A class to manage the ship
	'''
	def __init__(self, ai_game):
		'''
		Init the ship and position
		'''
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load ship image and get its rect
		self.image = pygame.image.load('Images/space_ship.bmp')
		self.rect = self.image.get_rect()

		# Start ship at bottom center of screen
		self.rect.midbottom = self.screen_rect.midbottom
		# Store decimal value for ships x position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		'''
		Updates the ship's position based on the movemenet flag
		'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed
		# Update rect from self.x
		self.rect.x = self.x 
		self.rect.y = self.y


	def blitme(self):
		'''
		Draw ship at current location
		'''
		self.screen.blit(self.image, self.rect)