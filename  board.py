import pygame
from pygame.sprite import Sprite

class Board(Sprite):
    def __init__(self,self):
        self.settings = game.settings
        self.screen = game.screen
        self.rect = pygame.Rect(0,0,20,20)
        self.color = self.settings.backgroundcolor

    def display_board(self):
        pygame.draw.rect(self.screen,self.color,self.rect)