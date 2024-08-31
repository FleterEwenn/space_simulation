import pygame

pygame.init()

screen = pygame.display.set_mode((850, 850))
pygame.display.set_caption('space_simulation')

run = True

While run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT():
      run = False
