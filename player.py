import pygame
from pygame.locals import *
 
class Player(object):
 
    def __init__(self,posx,posy):
        self.bg = pygame.image.load("player.png")
        self.posx = posx
        self.posy = posy
        self.rect2 = Rect(self.posx,self.posy,121,73)
 
    def update(self):
        self.rect2 = Rect(self.posx,self.posy,121,73)

 
    def render(self,surface):
        surface.blit(self.bg, pygame.Rect(self.posx,self.posy,self.bg.get_rect().width, self.bg.get_rect().height))
    
    def getrect(self):
        return self.rect2


    def move_left(self):
        self.posx -= 5

    def move_right(self):
        self.posx += 5

    def getx(self):
        return self.posx

    def gety(self):
        return self.posy

    def getw(self):
        return self.bg.get_rect().width

    def geth(self):
        return self.bg.get_rect().height
