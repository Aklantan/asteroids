import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)



    def draw(self, screen):
        pygame.draw.circle(screen,"white", (self.position),self.radius,width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        ran_angle = random.uniform(20,50)
        child_velocity_one, child_velocity_two = self.velocity * ran_angle, self.velocity * - ran_angle
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child_one, child_two = Asteroid(self.position.x,self.position.y,new_radius),Asteroid(self.position.x,self.position.y,new_radius)
        child_one.velocity = child_velocity_one * 1.2
        child_two.velocity = child_velocity_two * 1.2

