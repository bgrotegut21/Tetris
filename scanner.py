import pygame
from greyspace import GreyBlock

class Scanner:
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.scanner_blocks = {0:pygame.sprite.Group()}
        self.make_scanner_row()
        self.last_time = pygame.time.get_ticks()
        self.xcollisions = game.xcollisions
        

    def make_scanner_row(self):
        blocks = GreyBlock(self,"images/scanner.bmp")
        x_position = self.settings.right_block_coord - 20
        y_position = self.settings.square_bottom_yposition - 20

        for number_y in range(21):
            self.scanner_blocks[number_y] = pygame.sprite.Group()
            for number_x in range(10):
                block = GreyBlock(self,"images/purplesquare.bmp")
                block.rect.x = x_position + (number_x * 20)
                block.rect.y = y_position - (number_y * 20)
                self.scanner_blocks[number_y].add(block)
    
    def make_one_row(self,position):
        x_position = self.settings.right_block_coord - 20
        y_position = self.settings.square_bottom_yposition - 20
        for number in range(10):
            block = GreyBlock(self,"images/purplesquare.bmp")
            block.rect.x = x_position + (number * 20)
            block.rect.y = y_position - (position * 20 )
            self.scanner_blocks[position].add(block)

    def delete_one_row(self,position):
        self.scanner_blocks[position].empty()
        self.xcollisions[position] = [[]]

    
    def clear_scanner_row(self,position):
        self.delete_one_row(position)
        self.make_one_row(position)

    

    def draw_scanner(self):
        for num in self.scanner_blocks:
            for block in self.scanner_blocks[num]:
                if block.pseudo_rect == False:
                    self.screen.blit(block.image, block.rect)