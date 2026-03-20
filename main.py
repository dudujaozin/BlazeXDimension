import pygame
import sys
from src.player import Blaze
from src.level import Level
from src.hud import HUD
from src.physics import Physics
from src.particles import ExplosionEffect
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    physics_engine = Physics()
    hud = HUD()
    level = Level()  # Initialize level with platforms and obstacles
    player = Blaze(position=(100, SCREEN_HEIGHT - 150), width=50, height=50)
    enemies = []
    particles = []
    fonts = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_a:
                    player.attack()

        keys = pygame.key.get_pressed()
        player.move(keys)

        physics_engine.apply_gravity(player)

        for enemy in enemies:
            enemy.update()
            if check_collision(player, enemy):
                handle_collision(player, enemy)

        # Update particles
        for particle in particles:
            particle.update()  

        screen.fill(level.background_color)
        # Draw platforms and obstacles
        for platform in level.platforms:
            pygame.draw.rect(screen, (128, 128, 128), platform)
        for obstacle in level.obstacles:
            pygame.draw.rect(screen, (139, 69, 19), obstacle)
        # Draw player, enemies, and particles
        pygame.draw.rect(screen, (255, 165, 0), player.get_rect())
        for enemy in enemies:
            pygame.draw.rect(screen, enemy.color, enemy.get_rect())
        for particle in particles:
            pygame.draw.circle(screen, (255, 165, 0), particle.position, particle.size)

        # Draw HUD
        hud.draw(screen, player)
        controls_info = fonts.render('Arrow keys to move, Space to jump, A to attack', True, (255, 255, 255))
        screen.blit(controls_info, (20, SCREEN_HEIGHT - 40))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()