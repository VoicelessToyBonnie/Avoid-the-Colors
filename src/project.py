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