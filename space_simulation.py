import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1100, 900))
pygame.display.set_caption('space_simulation')

run = True

rayon_1 = random.randint(10, 30)
rayon_2 = random.randint(35, 60)

pos_1 = (random.randint(100, 500), random.randint(50, 850))
pos_2 = (random.randint(600, 1000), random.randint(50, 850))

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  screen.fill((0, 0, 0))

  pygame.draw.circle(screen, (150, 150, 150), pos_1, rayon_1)
  pygame.draw.circle(screen, (150, 150, 150), pos_2, rayon_2)

  pygame.display.flip()

pygame.quit()
