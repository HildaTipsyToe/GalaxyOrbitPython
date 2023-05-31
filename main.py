# This is a sample Python script.
import pygame
from random import randint
from Orbs import orbs

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class MainProgram():
    def __init__(self):
        pygame.init()

        self.running = True
        self.width = 1800
        self.height = 1000

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Jimmy")

        self.fps = 60
        self.clock = pygame.time.Clock()

        self.Orbs = []
        self.antal_Orbs = randint(1, 10)
        self.add_orb(self.antal_Orbs)


    def add_orb(self, n=1):
        for i in range(n):
            r = randint(10,25)
            self.Orbs.append(orbs(randint(0 + r, self.width - r), randint(0 + r, self.height - r), r, randint(1,10)))


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.window.fill((255, 255, 255))
            for Internal_Orbs in self.Orbs:
                for External_Orbs in self.Orbs:
                    if(External_Orbs != Internal_Orbs):
                        Internal_Orbs.accelerate(External_Orbs, Internal_Orbs)
                    else:
                        break
                Internal_Orbs.update()
                Internal_Orbs.draw(self.window)
            pygame.display.update()
            self.clock.tick(self.fps)
        pygame.quit()
MainProgram().run()


