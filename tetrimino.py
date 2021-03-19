import pygame
from pygame.sprite import Sprite
from greyspace import GreyBlock




class S_Tetrimnio:
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.straight_tetrimnio = pygame.sprite.Group()


    def add_tetrimnio(self):
        for num in range(4):
            orange_block = GreyBlock(self,"images/redsquare.bmp")
            center_position = self.settings.screen_block_face + 2
            starting_position = self.screen_rect.topleft[0] + (center_position * orange_block.rect.width) 
            orange_block.rect.x = starting_position + (num * orange_block.rect.width)
            orange_block.rect.y = self.settings.square_yposition 
            self.straight_tetrimnio.add(orange_block)
    
    def movement(self):
        if self.settings.right_movement:
            for block in self.straight_tetrimnio:
                block.rect.x += 10
        if self.settings.left_movement:
            for block in self.straight_tetrimnio:
                x_cord = block.rect.x
                x_cord += self.settings.tetrimino_speed
                block.rect.x = -x_cord
        if self.settings.down_movement:
            for block in self.straight_tetrimnio:
                y_cord = block.rect.y
                y_cord += self.settings.tetrimino_speed
                block.rect.y = y_cord
    
    def draw_tetrimino(self):
        self.straight_tetrimnio.update()
        self.straight_tetrimnio.draw(self.screen)
