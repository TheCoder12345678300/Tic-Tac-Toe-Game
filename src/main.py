import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("TIC-TAC-TOE GAME")

# THIS IS TO DISPLAY THE PYGAME WINDOW ON THE SCREEN

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
           
    pygame.display.update()
