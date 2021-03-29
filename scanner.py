import pygame
from greyspace import GreyBlock

class Scanner:
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.scanner_blocks = []

    def make_scanner_row(self):
        block = GreyBlock(self,"images/purplesquare.bmp")
        self.xposition = self.screen_rect.topleft[0] + (self.settings.left_block_coord * 20)
        self.y_position = self.settings.square_bottom_yposition
        for 