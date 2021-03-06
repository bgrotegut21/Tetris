import pygame
from pygame.sprite import Sprite

class GreyBlock(Sprite):
    def __init__(self,game, image = "images/greysquare.bmp"):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x_cord = self.rect.x
        self.y_cord  = self.rect.y
        