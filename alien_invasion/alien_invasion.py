'''
pygame: write a game
'''
import sys
import pygame

def run_game():
    # init a pygame app
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))

    pygame.display.set_caption("Alien Invasion(Test)")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
run_game()


