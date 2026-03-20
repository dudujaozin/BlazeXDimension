import pygame
import random

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)
        self.camera = pygame.Rect(x, y, self.width, self.height)

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lifetime = random.randint(50, 100)

    def update(self):
        self.lifetime -= 1
        self.y -= 1  # Move up

    def is_alive(self):
        return self.lifetime > 0

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def emit(self, x, y):
        self.particles.append(Particle(x, y))

    def update(self):
        for particle in self.particles:
            particle.update()
        self.particles = [p for p in self.particles if p.is_alive()]

    def draw(self, surface):
        for particle in self.particles:
            pygame.draw.circle(surface, (255, 255, 255), (particle.x, particle.y), 2)

class HUD:
    def __init__(self, font):
        self.font = font

    def draw(self, surface, score):
        text = self.font.render(f'Score: {score}', True, (255, 255, 255))
        surface.blit(text, (10, 10))

class Sprite:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.camera = Camera(800, 600)
        self.hud = HUD(pygame.font.Font(None, 36))
        self.particle_system = ParticleSystem()
        self.entities = []
        self.score = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.particle_system.emit(400, 300)  # Emit particles at center
            self.particle_system.update()
            self.camera.update(self.entities[0])  # Assuming first entity is the player

            self.screen.fill((0, 0, 0))  # Clear screen
            for entity in self.entities:
                self.screen.blit(entity.image, self.camera.apply(entity))
            self.particle_system.draw(self.screen)
            self.hud.draw(self.screen, self.score)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run() 
