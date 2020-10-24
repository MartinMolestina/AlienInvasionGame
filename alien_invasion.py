import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint



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
		self.aliens = pygame.sprite.Group()
		self.stars = pygame.sprite.Group()
		self._create_universe()
		self._create_fleet()


	def _create_universe(self):
		# Make stars
		for _ in range(self.settings.num_stars):
			star = Star(self)
			star.rect.x = randint(0, self.settings.screen_width)
			star.rect.y = randint(0, self.settings.screen_height)
			self.stars.add(star)


	def _update_stars(self):
		self.stars.update()
		# Delete stars that exit the screen
		for star in self.stars.copy():
			if star.rect.bottom > self.settings.screen_height:
				# Removes star from list
				self.stars.remove(star)

				# Adds a new star at top after a star has been deleted 
				new_star = Star(self)
				new_star.rect.y = 0 #randint(50, int(self.settings.screen_width)-50)
				new_star.rect.x = randint(50, int(self.settings.screen_width)-50)
				self.stars.add(new_star)

		


	def _create_fleet(self):
		# Make an alien
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size

		# Calcs how many aliens can fit in the width of the screen
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# Determine the number of rows of aliens that fit on the screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height)
									- ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# Creates fleet of aliens
		for row_num in range(number_rows):
			for alien_num in range(number_aliens_x):
				self._create_alien(alien_num, row_num)
		

	def _create_alien(self, alien_num, row_num):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_num
		alien.rect.x = alien.x 
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
		self.aliens.add(alien)


	def _update_bullets(self):
		self.bullets.update()
		# Delete bullets that exit the screen
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)



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

		self.stars.draw(self.screen)

		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.aliens.draw(self.screen)
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
			self._update_stars()
			self._update_bullets()
			self._update_screen()


def main():
	ai = AlienInvasion()
	ai.run_game()

if __name__ == '__main__':
	main()
