import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((1100, 800))
pygame.display.set_caption('space_simulation')


class Planet(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.radius = random.randint(1, 3)
    self.x = random.randint(100, 1000)
    self.y = random.randint(50, 850)
    self.velocity = 0
    self.G = 16
    self.color = (150, 150, 150)

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Star(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.radius = random.randint(5, 10)
    self.x = random.randint(100, 1000)
    self.y = random.randint(50, 850)
    self.color = (150, (255//self.radius)*3, 0)
    self.life = (1000//self.radius)*5

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

all_stars = pygame.sprite.Group()
for i in range(10):
  star = Star()
  all_stars.add(star)

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

  for star in all_stars:
    star.draw(screen)

    star.life -= 1
    print(star.life)

  for planet in all_planets:
    planet.draw(screen)

    min_distance = 1000

    for other in all_planets:
      if other != planet:

        d_x = other.x - planet.x
        d_y = other.y - planet.y

        distance = math.sqrt(d_x ** 2 + d_y ** 2)

        planet.velocity = ((planet.radius*other.radius)/min_distance**2)*planet.G

        if distance < other.radius + planet.radius:
          if planet.radius > other.radius:
            planet.radius += other.radius // 2
            other.kill()
          else:
            other.radius += planet.radius // 2
            planet.kill()

        if distance < min_distance:
          min_distance = distance
          angle = math.atan2(d_y, d_x)

    planet.x += math.cos(angle) * planet.velocity
    planet.y += math.sin(angle) * planet.velocity

    if planet.x - planet.radius < 0 or planet.x + planet.radius > 1100:
      planet.velocity *= -1
    if planet.y - planet.radius < 0 or planet.y + planet.radius > 800:
      planet.velocity *= -1

  pygame.display.flip()
