import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        forward = self.velocity * dt
        self.position += forward

    def split(self):
        angle = random.uniform(20, 50)
        
        split_1_velocity = self.velocity.rotate(angle) * 1.2
        split_2_velocity = self.velocity.rotate(-angle) * 1.2
        x, y = (self.position.x, self.position.y)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_1 = Asteroid(x, y, new_radius)
        split_1.velocity = split_1_velocity
        split_2 = Asteroid(x, y, new_radius)
        split_2.velocity = split_2_velocity

        self.kill()

