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
        self.grey_up_blocks = game.grey_up_blocks
        self.grey_down_blocks = game.grey_down_blocks
        self.grey_right_blocks = game.grey_right_blocks
        self.grey_left_blocks = game.grey_left_blocks
        self.last_time = pygame.time.get_ticks()


    def add_tetrimnio(self):
        for num in range(4):
            orange_block = GreyBlock(self,"images/redsquare.bmp")
            center_position = self.settings.screen_block_face + 2
            starting_position = self.screen_rect.topleft[0] + (center_position * orange_block.rect.width) 
            orange_block.rect.x = starting_position + (num * orange_block.rect.width)
            orange_block.rect.y = self.settings.square_yposition 
            orange_block.x_cord = orange_block.rect.x
            orange_block.y_cord = orange_block.rect.y
            self.straight_tetrimnio.add(orange_block)
    
    def movement(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= self.settings.cool_down:
            self.last_time = current_time
            if self.settings.right_movement:
                collision = pygame.sprite.groupcollide(self.straight_tetrimnio,self.grey_right_blocks,False,False,)
                if not collision:         
                    for block in self.straight_tetrimnio:
                        block.x_cord += self.settings.tetrimino_speed
                        block.rect.x = block.x_cord

            if self.settings.left_movement:
                collision = pygame.sprite.groupcollide(self.straight_tetrimnio,self.grey_left_blocks,False,False)
                if not collision:
                    for block in self.straight_tetrimnio:
                        block.x_cord += -self.settings.tetrimino_speed
                        block.rect.x = block.x_cord
            
            if self.settings.up_movement:
                collision = pygame.sprite.groupcollide(self.straight_tetrimnio,self.grey_up_blocks,False,False)
                if not collision:
                    for block in self.straight_tetrimnio:
                        block.y_cord += -self.settings.tetrimino_speed
                        block.rect.y = block.y_cord

            if self.settings.down_movement:
                collision = pygame.sprite.groupcollide(self.straight_tetrimnio,self.grey_down_blocks,False,False)
                if not collision:
                    for block in self.straight_tetrimnio:
                        block.y_cord += self.settings.tetrimino_speed
                        block.rect.y = block.y_cord
        


    def draw_tetrimino(self):
        self.straight_tetrimnio.update()
        self.straight_tetrimnio.draw(self.screen)
