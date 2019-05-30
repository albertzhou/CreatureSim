import pygame, sys
import pygame.locals

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
        pygame.display.flip()
