import pygame
from pygame.locals import *
 

class SimpleGame(object):
 
    def __init__(self, title="Test", window_size=(640,480), fps=60):
        self.title = title
        self.window_size = window_size
        self.fps = fps 
        self.is_terminated = False

    def terminate(self):
        self.is_terminated = True

    def game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace", 20)

 
    def run(self):
        self.game_init()
        while not self.is_terminated:
            self.__handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()

    def is_key_pressed(self, key):
        keys_pressed = pygame.key.get_pressed()
        if key < 0 or key >= len(keys_pressed):
            return False
        return (keys_pressed[key])

    def on_key_up(self, key):
        pass
 
    def on_key_down(self, key):
        pass

    def init(self):
        pass
 
    def update(self):
        pass
 
    def render(self):
        pass