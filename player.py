import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):

	def __init__(self,x,y):
		super().__init__(x,y,PLAYER_RADIUS)		
		self.rotation = 0
		self.shootTimer = 0			
		
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
		
	def draw(self, screen):
		pygame.draw.polygon(screen,"white",self.triangle(),2)
					
	def rotade(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self, dt):
		if self.shootTimer <= 0:
			x1 = self.position.x
			y1 = self.position.y
		
			missle = Shot(x1, y1, SHOT_RADIUS)
			missle.velocity = pygame.Vector2(0, 1).rotate(self.rotation)		
		
			self.shootTimer = PLAYER_SHOOT_COOLDOWN
	def update(self, dt):
		keys = pygame.key.get_pressed()
		self.shootTimer -= dt
		if keys[pygame.K_LEFT]:
			self.rotade(dt * -1)

		if keys[pygame.K_RIGHT]:
			self.rotade(dt)
		
		if keys[pygame.K_UP]:
			self.move(dt)

		if keys[pygame.K_DOWN]:
			self.move(dt * -1)

		if keys[pygame.K_SPACE]:
			self.shoot(dt)
					
