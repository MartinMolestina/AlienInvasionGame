import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet



class AlienInvasion:
	'''
	Overall class to manage game asset and behavior
	'''
	def __init__(self):
		'''
		Initalize the game and create game resources
		'''
		pygame.init()
		# Create instance od Settings
		self.settings = Settings()


		# Set screen size
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		# Set caption at top of window
		pygame.display.set_caption('Alien Invasion')

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()



	def _update_bullets(self):
		self.bullets.update()
		# Delete bullets that exit the screen
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		print(len(self.bullets))



	def _check_events(self):
		'''
		Respond to palyer inputs through mouse or keyboard
		'''
		for event in pygame.event.get():
			# Quit game
			if event.type == pygame.QUIT:
				sys.exit()

			# Move Ship (press key)
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			# Stop moving ship (release key)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)



	def _update_screen(self):
		'''
		Upadte images on screen and flip new screeb
		'''
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# Make the most recent screen visible
		pygame.display.flip()



	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True

		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True

		elif event.key == pygame.K_UP:
			self.ship.moving_up = True

		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True

		# Quit with q
		elif event.key == pygame.K_q:
			sys.exit()

		# Fire bullets
		elif event.key == pygame.K_SPACE:
			 self._fire_bullet()


	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False

		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

		elif event.key == pygame.K_UP:
			self.ship.moving_up = False

		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False


	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def run_game(self):
		'''
		Start the loop for the game
		'''
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()




def main():
	ai = AlienInvasion()
	ai.run_game()

if __name__ == '__main__':
	main()
