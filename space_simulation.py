import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((1100, 800))
pygame.display.set_caption('space_simulation')


class Planet(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.radius = random.randint(3, 23)
    self.x = random.randint(100, 1000)
    self.y = random.randint(50, 850)
    self.velocity_x = 0.2
    self.velocity_y = 0.2

  def draw(self, screen):
    pygame.draw.circle(screen, (150, 150, 150), (self.x, self.y), self.radius)


all_planets = pygame.sprite.Group()
for i in range(2):
  planet = Planet()
  all_planets.add(planet)

min_distance = 1000

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  screen.fill((0, 0, 0))

  for planet in all_planets:
    planet.draw(screen)

    min_distance = 1000
    angle = 0

    for other in all_planets:
      if other != planet:

        d_x = other.x - planet.x
        d_y = other.y - planet.y

        distance = math.sqrt(d_x ** 2 + d_y ** 2)

        if distance < other.radius + planet.radius:
          if planet.radius > other.radius:
            planet.radius += other.radius
            other.kill()
          else:
            other.radius += planet.radius
            planet.kill()

        if distance < min_distance:
          min_distance = distance
          angle = math.atan2(d_y, d_x)

    planet.x += math.cos(angle) * planet.velocity_x
    planet.y += math.sin(angle) * planet.velocity_y

    if planet.x - planet.radius < 0 or planet.x + planet.radius > 1100:
      planet.velocity_x *= -1
    if planet.y - planet.radius < 0 or planet.y + planet.radius > 800:
      planet.velocity_y *= -1

  pygame.display.flip()
