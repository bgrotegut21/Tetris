import pygame
from pygame.sprite import Sprite

class PseudoRect(Sprite):
    def __init__(self,game, rect_width, rect_height):
        super().__init__()
        self.screen = game.screen
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.pseudo_rect = True
        self.color = (233,233,233)
        self.rect = pygame.Rect(0,0,self.rect_width, self.rect_height)
    def draw_pseudo_rect(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        