import pygame
import math
import sys

def main_systems():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SOLAR STRATEGY")
    screen = pygame.display.set_mode((1000,700 ))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0,0,0))
        clock.tick(60)

main_systems()