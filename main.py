import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	pygame.init()
	PyGame = pygame.get_init()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	AsteroidField.containers = (updatable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, drawable, updatable)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	PyClock = pygame.time.Clock()
	dt = 0
	
	player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
	updatable.add(player1)
	drawable.add(player1)
	
	asteroid_f = AsteroidField()
		
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		
		FillColor = pygame.Color(0,0,0)
		screen.fill(FillColor)
		for thing in updatable:
			thing.update(dt)
		
		for asteroid in asteroids:
			if asteroid.collision_check(player1) == True:
				exit("Game over!")
			
		for thing in drawable:
			thing.draw(screen)
		
		pygame.display.flip()
					
		mt = PyClock.tick(60)
		dt = mt/1000		
		
		
if __name__ == "__main__":

	main()
	
