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
    self.ref_solarsys = (False, [0, 0])
    self.x = random.randint(100, 1000)
    self.y = random.randint(50, 850)
    self.velocity = 0
    self.G = 16
    self.color = (150, 150, 150)

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

  def solarsys_move(self):
    for star in all_stars:
      if star.solarsys_id == self.ref_solarsys[1][0]:
        self.y = star.y
        self.x = star.x
    star.y += 20 * self.ref_solarsys[1][1]
    for i in range(20*self.ref_solarsys[1][1]):
      self.x += 1
      self.y += 1

class Star(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.radius = random.randint(5, 15)
    self.velocity = 1
    self.solarsys_id = 0
    self.x = random.randint(100, 1000)
    self.y = random.randint(50, 850)
    self.Bcolor = int(self.radius*200/15)
    self.color = (320-self.Bcolor, 125, self.Bcolor)
    self.life = int(10**5-(self.radius*10**5)/15) # la durée de vie maximale d'une étoile est 10**5

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

  def death(self):
    if self.radius > 13 :
      self.color = (255, 255, 255)
    elif self. radius >= 8 :
      self.color = (255, 50, 50)
      for i in range(50):
        self.radius += 0.1
        for planet in all_planets:
          if star.y-star.radius == planet.y-planet.radius:
            if star.x-star.radius == planet.x-planet.radius:
              planet.kill()
      self.radius = 4
      self.color = (255, 255, 255)
    else:
      self.radius = 4
      self.color = (255, 255, 255)

all_stars = pygame.sprite.Group()
for i in range(5):
  star = Star()
  star.solarsys_id = i + 1
  all_stars.add(star)

all_planets = pygame.sprite.Group()

for i in range(10):
  planet = Planet()
  all_planets.add(planet)

chance_starborn = [1] + 100*[0]

run = True
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  screen.fill((0, 0, 0))

  if random.choice(chance_starborn) == 1:
    chance_starborn.remove(0)
    star = Star()
    all_stars.add(star)

  for star in all_stars:
    star.draw(screen)

    #star.x += 0.1 * star.velocity
    #star.y += 0.1  * star.velocity

    if star.life <= 0:
      chance_starborn.append(0)
      star.death()

    star.life -= 1
    print(star.life)

    if star.x - star.radius < 0 or star.x + star.radius > 1100:
      star.velocity *= -1
    if star.y - star.radius < 0 or star.y + star.radius > 800:
      star.velocity *= -1

  for planet in all_planets:
    planet.draw(screen)

    planet.solarsys_move()

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
'''
        if distance < min_distance:
          min_distance = distance
          angle = math.atan2(d_y, d_x)

    planet.x += math.cos(angle) * planet.velocity
    planet.y += math.sin(angle) * planet.velocity

    if planet.x - planet.radius < 0 or planet.x + planet.radius > 1100:
      planet.velocity *= -1
    if planet.y - planet.radius < 0 or planet.y + planet.radius > 800:
      planet.velocity *= -1
'''
  pygame.display.flip()
