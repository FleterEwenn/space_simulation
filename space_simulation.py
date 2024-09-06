import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1100, 900))
pygame.display.set_caption('space_simulation')

class Planet(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.all_planets = pygame.sprite.Group()

    pygame.draw.circle(screen, (150, 150, 150), (0, 0), random.randint(10, 60))
    
planet = Planet()
planet.x = random.randint(100, 1000)
planet.y = random.randint(50, 850)
  
Planet().all_planets.add(planet) 

run = True

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      
  Planet().all_planets.update()
  
  screen.fill((0, 0, 0))

  Planet().all_planets.draw(screen)
  
  #pygame.draw.circle(screen, (150, 150, 150), pos_1, rayon_1)
  #pygame.draw.circle(screen, (150, 150, 150), pos_2, rayon_2)

  pygame.display.flip()
