import pygame
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw a circle representing the asteroid
        pygame.draw.circle(
            screen, # The surface to draw on
            ("white"),
            (int(self.position.x), int(self.position.y)), # center of circle position
            self.radius,
            2
        )
    def update(self, dt):
        self.position += self.velocity * dt
        
