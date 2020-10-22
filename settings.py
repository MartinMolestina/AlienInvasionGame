

class Settings:
	# A class to store all settings for the game
	
	def __init__(self):	
		# Screen size
		self.screen_width = 1200
		self.screen_height = 800

		# Backgorund color
		self.bg_color = (145, 115 ,155)

		# Ship moving speed
		self.ship_speed = 1.6

		# Bullet settings
		self.bullet_speed = 1.8
		self.bullet_width = 4
		self.bullet_height = 12
		self.bullet_color = (255,255,255)
		self.bullets_allowed = 4