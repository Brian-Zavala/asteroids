import pygame
from constants import *


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other_shape):
        # calculate distance between containers
        distance = self.position.distance_to(other_shape.position)

        # Check if distance is less than or equal to sum of radii
        return distance <= (self.radius + other_shape.radius)


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        # Draw a circle representing the asteroid
        pygame.draw.circle(
            screen,  # The surface to draw on
            "white",
            (int(self.position.x), int(self.position.y)),  # center of circle position
            SHOT_RADIUS,
            2,
        )

    def update(self, dt):
        self.position += self.velocity * dt
