
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot
import pygame

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shotCoolDown = 0

    def update(self, dt):
        # Update player position based on velocity
        self.position += self.velocity * dt

        # Update shot cooldown
        if self.shotCoolDown > 0:
            self.shotCoolDown -= dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shotCoolDown > 0:
            return
        self.shotCoolDown = PLAYER_SHOOT_COOLDOWN_SECONDS
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_velocity = forward * PLAYER_SHOOT_SPEED
        shot_position = self.position + forward * (self.radius + SHOT_RADIUS)
        Shot(shot_position, shot_velocity)