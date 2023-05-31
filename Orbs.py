import math

import pygame
from random import randint

vector = pygame.math.Vector2

class orbs(object):
    def __init__(self, x = 0, y = 0, r= randint(10,25), mass = 0):
        self.pos = vector(x, y)
        self.acc = vector()
        self.vel = vector()
        self.radius = r
        self.mass = mass
        self.colour = (randint(0, 255), randint(0,255), randint(0,255))

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

        self.acc = vector()fff


    def accelerate(self, External_Orb, Internal_Orb):
        self.acc += self.GetNormalizeVelocityApplier(External_Orb, Internal_Orb)
        return self.acc

    def GetGravitationalPull(self, External_Orb, Internal_Orb):
        return 6.6743 * math.pow(10, -11) * ((Internal_Orb.mass * External_Orb.mass)/math.pow
            (vector.distance_to(External_Orb.pos, Internal_Orb.pos), 2))

    def GetDistanceInVector(self, External_Orb, Internal_Orb ):
        return vector(External_Orb.pos.x - Internal_Orb.pos.x, External_Orb.pos.y - Internal_Orb.pos.y);

    def GetNormalizeVelocityApplier(self, External_Orb, Internal_Orb):
        return vector.normalize(self.GetDistanceInVector(External_Orb, Internal_Orb) *
                                self.GetGravitationalPull(External_Orb, Internal_Orb))

    def draw(self, window):
        pygame.draw.circle(window, self.colour, (round(self.pos.x), round(self.pos.y)), self.radius)