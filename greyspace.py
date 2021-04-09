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
        self.show_block = True
        self.can_collide_block = False
        self.create_rect = True
        self.pseudo_rect = False
        self.can_flip = True
        self.created_pseudo_rect = False
        self.position1 = 0
        self.can_add_coord = True