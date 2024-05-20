import pygame
import sys
import random
import time
from pygame import *
from pygame.sprite import Sprite
class weekend(Sprite):
    def __init__(self,a_game):
        super().__init__()
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()
        self.padlock = image.load("assets/buttons/padlock.png")
        self.rect_pad = self.padlock.get_rect()
        self.rect_pad.midbottom = self.screen_rect.midbottom
        self.week_1 = image.load("assets/buttons/week1.png")
        self.rect_1 = self.week_1.get_rect()
        self.rect_1.midtop = self.screen_rect.midtop
        self.week_2 = image.load("assets/buttons/week2.png")
        self.rect_2 = self.week_2.get_rect()
        self.rect_2.midbottom = self.screen_rect.midbottom
        self.week_3 = image.load("assets/buttons/week3.png")
        self.rect_3 = self.week_3.get_rect()
        self.rect_3.midbottom = self.screen_rect.midbottom
        self.week = 0
    def init(self):
        if self.week == 0:
            self.screen.blit(self.padlock,self.rect_pad)
        elif self.week == 1:
            self.screen.blit(self.week_1,self.rect_1)
        elif self.week == 2:
            self.screen.blit(self.week_2,self.rect_2)
        elif self.week == 3:
            self.screen.blit(self.week_3,self.rect_3)
        #print(self.rect_pad.x,self.rect_pad.y)
        #print(self.rect_1.x,self.rect_1.y)
        #print(self.rect_2.x,self.rect_2.y)
        #print(self.rect_3.x,self.rect_3.y)