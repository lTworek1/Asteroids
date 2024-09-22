import pygame


from constants import *

def main():
	pygame.init()
	PyGame = pygame.get_init()
	print(f"pygem initialization: {PyGame}")
	
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		FillColor = pygame.Color(0,0,0)
		screen.fill(FillColor)
		pygame.display.flip()



if __name__ == "__main__":

	main()

