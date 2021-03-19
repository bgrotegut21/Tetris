import pygame
from pygame.sprite import Sprite


class Tetromino(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
    
    def orange_block(self):
        self.orange_block = pygame.image.load("images/orangesquare.jpg")
        self.orange_rect = self.orange_block.get_rect()
        self.orange