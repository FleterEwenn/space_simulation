import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1100, 800))
pygame.display.set_caption('space_simulation')

class Planet(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.radius = random.randint(3, 23)
    self.x = random.randint(100, 1000)
    self.y = random.randint(50, 850)
    self.velocity_x = random.choice([-1, 1]) * ((random.random() * 2)/self.radius)
    self.velocity_y = random.choice([-1, 1]) * ((random.random() * 2)/self.radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (150, 150, 150), (self.x, self.y), self.radius)

all_planets = pygame.sprite.Group()
for i in range(10):
  planet = Planet()
  all_planets.add(planet) 

run = True

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  screen.fill((0, 0, 0))

  for planet in all_planets:
    planet.draw(screen)

    planet.x += planet.velocity_x
    planet.y += planet.velocity_y
      
    if planet.x - planet.radius < 0 or planet.x + planet.radius > 1100:
      planet.velocity_x *= -1
    if planet.y - planet.radius < 0 or planet.y + planet.radius > 800:
      planet.velocity_y *= -1

  pygame.display.flip()
