import pygame
from pygame.sprite import Sprite
from greyspace import GreyBlock




class S_Tetrimnio:
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.straight_tetrimnio = pygame.sprite.Group()
        self.down_movement = False
        self.right_movment = False
        self.left_movement = False

    def add_tetrimnio(self):
        for num in range(4):
            orange_block = GreyBlock(self,"images/orangesquare.jpg")
            center_position = self.settings.screen_block_face + 2
            starting_position = self.screen_rect.topleft[0] + (center_position * orange_block.rect.width)
            orange_block.rect.x = starting_position + (num * orange_block.rect.width)
            orange_block.rect.y = self.settings.square_yposition 
            self.straight_tetrimnio.add(orange_block)
    
    def update(self):
        if right_movment:
            for block in self.straight_tetrimnio:
                x_cord = block.rect.x
                x_cord += self.settings.tetrimino_speed
                block.rect.x += x_cord
        if left_movement:
            for block in self.straight_tetrimnio:
                x_cord = block.rect.x
                x_cord += self.settings.tetrimino_speed
                block.rect.x += -x_cord
        if down_movement:
            for block in self.straight_tetrimnio:
                y_cord = block.rect.y
                y_cord += self.settings.tetrimino_speed
                block.rect.y = y_cord
    
    def draw_tetrimino(self):
        self.straight_tetrimnio.update()
        self.straight_tetrimnio.draw(self.screen)