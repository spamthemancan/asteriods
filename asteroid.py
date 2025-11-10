from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import pygame
import random

class Asteroid (CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        # Update asteriod position based on velocity
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return()
        log_event("asteroid_split")
        new_angle = random.uniform(20,50)
        velocity_one = self.velocity.rotate(new_angle)
        velocity_two = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius / 2)
        asteroid_one.velocity = velocity_one * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius / 2)
        asteroid_two.velocity = velocity_two * 1.2

