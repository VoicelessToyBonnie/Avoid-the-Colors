import pygame
import time
import random

class particleTrail:
     def __init__(self, pos, size, life, direction):
        self.pos = pos
        self.size = size
        self.life = life
        self.particles = []
        self.direction = direction


     def update(self, dt):
        color = pygame.Color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        particle = Particle(self.pos, self.size, self.life, color)
        self.particles.append(particle)
        self._move_particles(dt)
        self.particles = [p for p in self.particles if not p.dead]

     def _move_particles(self, dt):
        for particle in self.particles:
            particle.update(dt)
            x, y = particle.pos
            if self.direction == 'vertical':
                particle.pos = (x, y + dt)
            elif self.direction == 'horizontal':
                particle.pos = (x + dt, y)
            elif self.direction == 'diagonal':
                particle.pos = (x + dt, y + dt)
            elif self.direction == 'random':
                particle.pos = (x + random.choice([-1, 1]) * dt, y + random.choice([-1, 1]) * dt)

     def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)

class Particle:
    def __init__(self, pos, size, life, color):
        self.pos = pos
        self.size = size
        self.color = color
        self.age = 0
        self.life = life
        self.dead = False

class Player:
     def __init__(self, pos, size=20):
        self.pos = pos
        self.size = size
        self.color = (255, 255, 255)

def main():
    pygame.init()

    screen_res = (1920, 1080)
    FPS = 60

    screen = pygame.display.set_mode(screen_res, pygame.FULLSCREEN)
    pygame.display.set_caption("Avoid the Colors")
    clock = pygame.time.Clock()

    pygame.quit()

if __name__ == "__main__":
    main()