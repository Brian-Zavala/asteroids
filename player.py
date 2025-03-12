import pygame
from constants import *
from circleshape import CircleShape, Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        # in the player class

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt, shots_group):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(shots_group)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, shots_group):

        # Create velocity vector (starts pointing down)
        shot_velocity = pygame.Vector2(0, 1)

        # Rotate to match player direction
        shot_velocity = shot_velocity.rotate((self.rotation))

        # Scale up by PLAYER_SHOOT_SPEED
        shot_velocity = shot_velocity * PLAYER_SHOOT_SPEED

        # Create new shot at player position
        new_shot = Shot(self.position.x, self.position.y, shot_velocity)

        # Add to shots group (you'll beed to pass this group to the method or access it some other way)
        shots_group.add(new_shot)
