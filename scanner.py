import pygame
from greyspace import GreyBlock

class Scanner:
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.scanner_blocks = []
        self.make_scanner_row()
        

    def make_scanner_row(self):
        block = GreyBlock(self,"images/purplesquare.bmp")
        x_position = self.settings.right_block_coord - 20
        y_position = self.settings.square_bottom_yposition + 20
        for number in range(10):
            block = GreyBlock(self,"images/purplesquare.bmp")
            block.rect.x = x_position + (number * 20)
            block.rect.y = y_position
            self.scanner_blocks.append(block)

    def draw_scanner(self):
        for block in self.scanner_blocks:
            self.screen.blit(block.image,block.rect)
    