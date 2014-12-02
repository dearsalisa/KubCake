import pygame
from pygame.locals import *
from random import randint
 
class Bonus(object):        

    def __init__(self):
        num = randint(20,620)
        self.posy = -500
        self.posx = num
        #self.check = False
        self.rect4 = Rect(self.posx,self.posy,55,54)
 
    def update(self,player, gameOver):
        self.rect4 = Rect(self.posx,self.posy,55,54)
        if self.posy < 3000:
            self.posy += 7
        else:
            self.resetPosToTop(gameOver)

        if self.ishit(player) == True:
            self.resetPosToTop(gameOver)


    def resetPosToTop(self, gameOver):
        if not gameOver:
            num = randint(20,620)
            self.posx = num
            self.posy = -500
 
 
    def render(self,surface,bg):
        surface.blit(bg,pygame.Rect(self.posx,self.posy,bg.get_rect().width, bg.get_rect().height))

    def gety(self):
        return self.posy

    def getrect(self):
        return self.rect4

    #def getcheck(self):
    #    return self.check

    def ishit(self,player):
        #rect1 = Rect(self.posx,self.posy,bg.get_rect().width,bg.get_rect().height)
        #rect2 = Rect(player.getx(),player.gety(),player.getw(),player.geth())
        if self.rect4.colliderect(player.getrect()):
            return True
        else :
            return False