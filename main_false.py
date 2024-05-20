import pygame
import sys
import random
import time
from pygame import *
from indicator import BS7
from weeks import weekend
class vivential_project:
    def __init__(self):
        pygame.init()
        self.size = (1920,1080)
        self.screen = pygame.display.set_mode(self.size,pygame.FULLSCREEN)
        pygame.display.set_caption("Vivential Project in pygame :D")
        self.color = (0,0,0)
        self.indicator = BS7(self)
        self.weeks = weekend(self)
    def arrow(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP or event.key == K_w:
                        self.indicator.move_up = True
                    if event.key == K_DOWN or event.key == K_s:
                        self.indicator.move_down = True
                    if event.key == K_RIGHT or event.key == K_d:
                        self.indicator.move_right = True
                    if event.key == K_LEFT or event.key == K_a:
                        self.indicator.move_left = True
                elif event.type == KEYUP:
                    if event.key == K_UP or event.key == K_w:
                        self.indicator.move_up = False
                    if event.key == K_DOWN or event.key == K_s:
                        self.indicator.move_down = False
                    if event.key == K_RIGHT or event.key == K_d:
                        self.indicator.move_right = False
                    if event.key == K_LEFT or event.key == K_a:
                        self.indicator.move_left = False
            self.indicator.motion()
            self.screen.fill(self.color)
            self.weeks.init()
            self.indicator.init()
            display.flip()
if __name__ == "__main__":
    a = vivential_project()
    a.arrow()