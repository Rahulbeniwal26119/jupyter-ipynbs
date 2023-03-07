#%%
import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

player_quits = False

pygame.draw.rect(screen, (255, 255, 34), pygame.Rect(10, 10, 70, 60))
pygame.display.flip()


while not player_quits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_quits = True

# %%
