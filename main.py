import pygame
from constants import *
import resource_monitor

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()
    dt = 0
    while True:
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Optionally, get resource usage data every frame or at set intervals
        cpu_usage = resource_monitor.get_cpu_usage(interval=0)  # Using interval=0 for a non-blocking call
        mem_usage, mem_total = resource_monitor.get_memory_usage()
        disk_usage = resource_monitor.get_disk_usage()

        # For demonstration, print the resource usage to the console
        print(f"CPU: {cpu_usage}%  Memory: {mem_usage}%  Disk: {disk_usage}%")

        screen.fill((0, 0, 0))
        pygame.display.flip()

        # limit framerate to 60 fps
        dt = clock.tick(60) / 1000.0
        # print(f"FPS: {clock.get_fps()}")

if __name__ == "__main__":
    main()