import pygame

pygame.init()

screen = pygame.display.set_mode((1100, 900))
pygame.display.set_caption('space_simulation')

run = True

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

pygame.quit()
