import pygame
from pygame.locals import *
from random import randint
from cake import Cake
from bomb import Bomb
from bonus import Bonus
from player import Player
 
class CakeCollector(object):
    
    cakeList = []
    bombList = []

    def __init__(self):
        self.bg = pygame.image.load("cake.png")
        self.bg2 = pygame.image.load("bomb.png")
        self.bg3 = pygame.image.load("cake2.png")
        self.cakeList = [(Cake()),(Cake()),(Cake()),(Cake()),(Cake()),(Cake()),(Cake()),(Cake()),(Cake()),(Cake())]
        self.bombList = [(Bomb()),(Bomb()),(Bomb())]
        self.bonus = Bonus()
        self.player = Player(100,400)
        self.gameOver = False
 
    def update(self,player, gameOver):
        for i in self.cakeList:
            i.update(player, gameOver)
        for j in self.bombList:
            j.update(player, gameOver)
        self.bonus.update(player, gameOver)

 
    def render(self,surface):
        for i in self.cakeList:
            i.render(surface,self.bg)
        for j in self.bombList:
            j.render(surface,self.bg2)
        self.bonus.render(surface,self.bg3)

    def setGameOver(self, gameOver):
        self.gameOver = gameOver
    