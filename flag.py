import pygame


pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
