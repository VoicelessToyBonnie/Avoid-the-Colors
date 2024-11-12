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


    def update(self, dt, screen_width, screen_height):
        color = pygame.Color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        particle = Particle(self.pos, self.size, self.life, color, self.direction, screen_width, screen_height)
        self.particles.append(particle)
        self._move_particles(dt)
        self.particles = [p for p in self.particles if not p.dead]

    def _move_particles(self, dt):
         for particle in self.particles:
            particle.update(dt)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)

class Particle:
    def __init__(self, pos, size, life, color, direction, screen_width, screen_height):
        self.pos = list(pos)
        self.size = size
        self.color = color
        self.age = 0
        self.life = life
        self.direction = direction
        self.dead = False
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True

        if self.direction == 'vertical':
            self.pos[1] += 100 * dt  
            if self.pos[1] > self.screen_height:
                self.dead = True
        elif self.direction == 'horizontal':
            self.pos[0] += 100 * dt
            if self.pos[0] > self.screen_width:
                self.dead = True
        elif self.direction == 'diagonal':
            self.pos[0] += 70 * dt
            self.pos[1] += 70 * dt
            if self.pos[0] > self.screen_width or self.pos[1] > self.screen_height:
                self.dead = True
        elif self.direction == 'random':
            self.pos[0] += random.choice([-100, 100]) * dt
            self.pos[1] += random.choice([-100, 100]) * dt
            if self.pos[0] < 0 or self.pos[0] > self.screen_width or self.pos[1] < 0 or self.pos[1] > self.screen_height:
                self.dead = True

    def draw(self, surface):
        if not self.dead:
            pygame.draw.circle(surface, self.color, (int(self.pos[0]), int(self.pos[1])), self.size // 2)       

class Player:
    def __init__(self, pos, size=20):
        self.pos = pos
        self.size = size
        self.color = (255, 255, 255)

    def update(self, mouse_pos):
        self.pos = mouse_pos

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.pos[0]), int(self.pos[1])), self.size // 2)

def check_collision(player, trails):
    for trail in trails:
        for particle in trail.particles:
            if not particle.dead and (abs(player.pos[0] - particle.pos[0]) < player.size and
                                      abs(player.pos[1] - particle.pos[1]) < player.size):
                return True
    return False

def game_over(screen, survival_time, high_score):
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("Game Over!", True, (255, 255, 255)) 
    survival_text = font.render(f"Survival Time: {survival_time:.2f}s", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {high_score:.2f}s", True, (255, 255, 255))
    
    screen.blit(game_over_text, (1920 // 2 - game_over_text.get_width() // 2, 1080 // 2 - 100))
    screen.blit(survival_text, (1920 // 2 - survival_text.get_width() // 2, 1080 // 2))
    screen.blit(high_score_text, (1920 // 2 - high_score_text.get_width() // 2, 1080 // 2 + 100))
    pygame.display.flip()
    pygame.time.delay(2000)

def main():
    pygame.init()

    screen_res = (1920, 1080)
    FPS = 60

    screen = pygame.display.set_mode(screen_res, pygame.FULLSCREEN)
    pygame.display.set_caption("Avoid the Colors")
    clock = pygame.time.Clock()

    player = Player(pos=(screen_res[0]//2, screen_res[1]//2))
    trails = []
    time_survived = 0
    high_score = 0
    running, game_active = True, True

    while running:
        dt = clock.tick(FPS) / 1000.0 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                
        if game_active:
            player.update(pygame.mouse.get_pos())
            time_survived += dt

        if random.random() < 0.05:
            direction = random.choice(['vertical', 'horizontal', 'diagonal', 'random'])
            new_trail = particleTrail((random.randint(0, screen_res[0]), random.randint(0, screen_res[1])),
                                  size=15, life=1, direction=direction)
            trails.append(new_trail)

        for trail in trails:
            trail.update(dt, screen_res[0], screen_res[1])
        
        screen.fill((0, 0, 0))
        if game_active:
            player.draw(screen)
            for trail in trails:
                trail.draw(screen)
        else:
            game_over(screen, time_survived, high_score)
            time_survived = 0
            game_active = True
            trails.clear()
        
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()