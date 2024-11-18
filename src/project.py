import pygame
import random
import time

class ParticleTrail:
    def __init__(self, pos, size, life, direction, screen_res):
        self.pos = pos
        self.size = size
        self.life = life
        self.screen_res = screen_res
        self.particles = []
        self.direction = direction
        self.spawn_timer = 0

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer >= 0.1:
            direction_vector = self._get_direction_vector()
            speed = abs(direction_vector[0]) or abs(direction_vector[1]) 
            max_distance = max(self.screen_res)
            life = max_distance / speed
            color = pygame.Color(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            particle = Particle(self.pos, self.size, life, color, direction_vector)
            self.particles.append(particle)
            self.spawn_timer = 0

        for particle in self.particles:
            particle.update(dt, self.screen_res)
        self.particles = [p for p in self.particles if not p.dead]

    def _get_direction_vector(self):
        speed = 200
        if self.direction == 'vertical':
            return (0, random.choice([-speed, speed]))
        elif self.direction == 'horizontal':
            return (random.choice([-speed, speed]), 0)
        elif self.direction == 'diagonal':
            return (random.choice([-speed, speed]), random.choice([-speed, speed]))
        return (0, 0)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)


class Particle:
    def __init__(self, pos, size, life, color, direction):
        self.pos = pos
        self.size = size
        self.color = color
        self.age = 0
        self.life = life
        self.dead = False
        self.direction = direction

    def update(self, dt, screen_res):
        self.age += dt
        if self.age > self.life:
            self.dead = True

        dx, dy = self.direction
        self.pos = (self.pos[0] + dx * dt, self.pos[1] + dy * dt)

        if self.pos[0] < 0 or self.pos[0] > screen_res[0] or self.pos[1] < 0 or self.pos[1] > screen_res[1]:
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


def display_game_over(screen, survival_time, high_score):
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    survival_text = font.render(f"Survival Time: {survival_time:.2f}s", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {high_score:.2f}s", True, (255, 255, 255))
    restart_text = pygame.font.Font(None, 48).render("Press SPACE to play again", True, (200, 200, 200))
    
    screen.fill((0, 0, 0))
    screen.blit(game_over_text, (1920 // 2 - game_over_text.get_width() // 2, 1080 // 2 - 100))
    screen.blit(survival_text, (1920 // 2 - survival_text.get_width() // 2, 1080 // 2))
    screen.blit(high_score_text, (1920 // 2 - high_score_text.get_width() // 2, 1080 // 2 + 100))
    screen.blit(restart_text, (1920 // 2 - restart_text.get_width() // 2, 1080 // 2 + 200))
    pygame.display.flip()

    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting_for_restart = False 


def main():
    pygame.init()

    screen_res = (1920, 1080)
    FPS = 60

    screen = pygame.display.set_mode(screen_res, pygame.FULLSCREEN)
    pygame.display.set_caption("Avoid the Colors")
    clock = pygame.time.Clock()

    player = Player(pos=(screen_res[0] // 2, screen_res[1] // 2))
    trails = []
    survival_time = 0
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
            survival_time += dt

            if random.random() < 0.05:
                direction = random.choice(['vertical', 'horizontal', 'diagonal'])
                if direction == 'vertical':
                    start_pos = (random.randint(0, screen_res[0]), random.choice([0, screen_res[1]]))
                elif direction == 'horizontal':
                    start_pos = (random.choice([0, screen_res[0]]), random.randint(0, screen_res[1]))
                else: 
                    start_pos = random.choice([(0, 0), (screen_res[0], 0), (0, screen_res[1]), (screen_res[0], screen_res[1])])

                new_trail = ParticleTrail(pos=start_pos, size=15, life=1, direction=direction, screen_res=screen_res)
                trails.append(new_trail)

            for trail in trails:
                trail.update(dt)

            if check_collision(player, trails):
                game_active = False
                high_score = max(high_score, survival_time)

        screen.fill((0, 0, 0))
        if game_active:
            player.draw(screen)
            for trail in trails:
                trail.draw(screen)
        else:
            display_game_over(screen, survival_time, high_score)
            survival_time = 0
            game_active = True
            trails.clear()  

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()