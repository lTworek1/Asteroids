import pygame

from constants import *
from player import *

def main():
	pygame.init()
	PyGame = pygame.get_init()
	print(f"pygem initialization: {PyGame}")
	
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	PyClock = pygame.time.Clock()
	dt = 0
	
	player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		
		FillColor = pygame.Color(0,0,0)
		screen.fill(FillColor)
		player1.update(dt)
		player1.draw(screen)
		pygame.display.flip()
					
		mt = PyClock.tick(60)
		dt = mt/1000		
		
		
if __name__ == "__main__":

	main()

