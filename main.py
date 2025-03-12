import pygame
from constants import *
from asteroid import *
from asteroidfield import *
import resource_monitor
import player as player_module


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    pygame.mouse.set_visible(False)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable,drawable)
    AsteroidField.containers = (updatable,)
    player_module.Player.containers = (updatable, drawable)

    player = player_module.Player(x, y)
    asteroid_field= AsteroidField()
    clock = pygame.time.Clock()
    dt = 0


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Optionally, get resource usage data every frame or at set intervals
        cpu_usage = resource_monitor.get_cpu_usage(
            interval=0
        )  # Using interval=0 for a non-blocking call
        mem_usage, mem_total = resource_monitor.get_memory_usage()
        disk_usage = resource_monitor.get_disk_usage()

        # For demonstration, printhe resource usage to the console
        print(f"CPU: {cpu_usage}%  Memory: {mem_usage}%  Disk: {disk_usage}%")

        updatable.update(dt)
        screen.fill((0, 0, 0))
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        # limit framerate to 60 fps
        dt = clock.tick(60) / 1000.0
        # print(f"FPS: {clock.get_fps()}")


if __name__ == "__main__":
    main()
