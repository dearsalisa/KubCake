import pygame
from pygame.locals import *
from gamelib import SimpleGame
from player import Player
from cake import Cake
from bomb import Bomb
from bonus import Bonus
from cakecollector import CakeCollector

class KubCakeGame(SimpleGame):

	BLACK = pygame.Color('black')

	def __init__(self):
		super(KubCakeGame, self).__init__('KubCake Game')
		self.player = Player(100,400)
		self.cakecollector = CakeCollector()
		self.start_image = pygame.image.load("start.png")
		self.bg = pygame.image.load("bg.jpg")
		self.bgscore_image = pygame.image.load("bgscore.png")
		self.start = True
		self.score = 0
		self.time = 31
		self.gameOver = False
		self.highScore = 0
		self.status = False

	def init(self):
		super(KubCakeGame, self).init()
		self.render_score()
		self.render_time()
		self.render_result(self.surface)

	def update(self):
		self.render_result(self.surface)
		if self.is_key_pressed(K_RETURN):
			self.score = 0
			self.time = 31
			self.player = Player(100,400)
			self.gameOver = False

		if self.time >= 0 :
			self.player.update()
			self.render_time()
		else :
			self.gameOver = True
			if self.score > self.highScore:
				self.highScore = self.score

		self.inputs()
		if self.gameOver:
			self.cakecollector.setGameOver(self.gameOver)

		self.cakecollector.update(self.player, self.gameOver)

		for x in self.cakecollector.cakeList:
			if x.ishit(self.player) and not self.gameOver:
				self.score += 10
			self.render_score()

		for y in self.cakecollector.bombList:
			if y.ishit(self.player) and not self.gameOver:
				self.score -= 50
			self.render_score()

		if self.cakecollector.bonus.ishit(self.player):
			if not self.gameOver:
				self.score += 100
			self.render_score()	

	def inputs(self):
		if self.is_key_pressed(K_LEFT):
			self.status = False
			self.player.move_left()
		elif self.is_key_pressed(K_RIGHT):
			self.status = True
			self.player.move_right()

	def render_result(self,surface):
		surface.blit(self.bgscore_image,pygame.Rect(200,200,400,205))
		self.yourscore_image = self.font.render("Your Score : %d" % self.score, 0, KubCakeGame.BLACK)
		self.highscore_image = self.font.render("High Score : %d" % self.highScore, 0, KubCakeGame.BLACK)

	def render_score(self):
		self.score_image = self.font.render("Score = %d" % self.score, 0, KubCakeGame.BLACK)

	def render_time(self):
		self.time -= self.clock.get_time()/1000.0
		self.time_image = self.font.render("Time = %d" % self.time, 0, KubCakeGame.BLACK)

	def render(self):
		if self.start :
			self.surface.blit(self.start_image, pygame.Rect(0,0, self.bg.get_rect().width, self.bg.get_rect().height))
			if self.is_key_pressed(K_RETURN):
				self.start = False
		else :
			self.surface.blit(self.bg, pygame.Rect(-1000,-700, self.bg.get_rect().width, self.bg.get_rect().height))

			self.player.render(self.surface,self.status)
			self.cakecollector.render(self.surface)
			self.surface.blit(self.score_image,(10,10))
			self.surface.blit(self.time_image,(10,40))
			if self.gameOver:
				self.surface.blit(self.bgscore_image,(100,100))
				self.surface.blit(self.yourscore_image,(200,180))
				self.surface.blit(self.highscore_image,(200,200))
		pygame.display.flip()
		
def main():
	game = KubCakeGame()
	game.run()

if __name__ == '__main__':
    main()
