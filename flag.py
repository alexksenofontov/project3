import pygame


def flag_pole():
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 10, 400), 0)
    pygame.draw.rect(screen, (255, 255, 255), (95, 500, 22, 5), 0)


def blue_pole():
    pygame.draw.rect(screen, (0, 0, 255), (110, 200, 300, 100), 0)


def white_pole():
    pygame.draw.rect(screen, (255, 255, 255), (110, 100, 300, 100), 0)


pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
flag_pole()
blue_pole()
white_pole()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
