from circleshape import *
from constants import *

class Shot(CircleShape):	
	def __init__(self, x, y, RADIUS):
		super().__init__(x, y, RADIUS)

	def draw(self, screen):
		pygame.draw.circle(screen, "red", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * PLAYER_SHOOT_SPEED * dt


