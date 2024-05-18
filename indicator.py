import pygame
from pygame import *
class BS7:
    def __init__(self,a_game):
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()
        self.image = image.load("assets/add/arrow2.png")
        self.image_scale = transform.scale(self.image,(105,105))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False
    def motion(self):
        if self.move_up:
            self.rect.y -= 1
        if self.move_down:
            self.rect.y += 1
        if self.move_right:
            self.rect.x += 1
        if self.move_left:
            self.rect.x -= 1
    def init(self):
        self.screen.blit(self.image,self.rect)