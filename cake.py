import pygame
from pygame.locals import *
from random import randint
 
class Cake(object):        

    def __init__(self):
        num = randint(20,620)
        start = randint(-500,-50)
        self.posy = start
        self.posx = num
        tmp = randint(2,5)
        self.v = tmp
        self.rect1 = Rect(self.posx,self.posy,36,40)
 
    def update(self,player, gameOver):
        self.rect1 = Rect(self.posx,self.posy,36,40)
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
            start = randint(-500,-50)
            self.posx = num
            self.posy = start        
 
    def render(self,surface,bg):
        surface.blit(bg,pygame.Rect(self.posx,self.posy,bg.get_rect().width, bg.get_rect().height))

    def gety(self):
        return self.posy

    def getrect(self):
        return self.rect1

    #def getcheck(self):
    #    return self.check

    def ishit(self,player):
        #rect1 = Rect(self.posx,self.posy,bg.get_rect().width,bg.get_rect().height)
        #rect2 = Rect(player.getx(),player.gety(),player.getw(),player.geth())
        if self.rect1.colliderect(player.getrect()):
            return True
        else :
            return False