import pygame
import time
import random


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