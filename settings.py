

class Settings:
	# A class to store all settings for the game
	
	def __init__(self):	
		# Screen size
		self.screen_width = 1200
		self.screen_height = 800

		# Backgorund color
		self.bg_color = (45, 25 ,65)

		# Ship moving speed
		self.ship_speed = 1.6

		# Bullet settings
		self.bullet_speed = 1.8
		self.bullet_width = 6
		self.bullet_height = 18
		self.bullet_color = (190,225,255)
		self.bullets_allowed = 4

		# Stars settings
		self.star_speed = 1
		self.num_stars = 3