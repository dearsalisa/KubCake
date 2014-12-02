import pygame
from pygame.locals import *
from random import randint
 
class Bomb(object):        

    def __init__(self):
        num = randint(20,620)
        start = randint(-1000,-50)
        self.posy = start
        self.posx = num
        #self.check = False
        tmp = randint(4,7)
        self.v = tmp
        self.rect3 = Rect(self.posx,self.posy,30,30)
 
    def update(self,player, gameOver):
        self.rect3 = Rect(self.posx,self.posy,30,30)
        if self.posy < 500:
            self.posy += self.v
            #self.check = False
        else:
            self.resetPosToTop(gameOver)

        if self.ishit(player) == True:
            self.resetPosToTop(gameOver)

    def resetPosToTop(self, gameOver):
        if not gameOver:
            num = randint(20,620)
            start = randint(-1000,-50)
            self.posx = num
            self.posy = start   
 
    def render(self,surface,bg):
        surface.blit(bg,pygame.Rect(self.posx,self.posy,bg.get_rect().width, bg.get_rect().height))

    def gety(self):
        return self.posy

    def getrect(self):
        return self.rect3

    #def getcheck(self):
    #    return self.check

    def ishit(self,player):
        #rect1 = Rect(self.posx,self.posy,bg.get_rect().width,bg.get_rect().height)
        #rect2 = Rect(player.getx(),player.gety(),player.getw(),player.geth())
        if self.rect3.colliderect(player.getrect()):
            return True
        else :
            return False