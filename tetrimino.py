import pygame
from pygame.sprite import Sprite
from greyspace import GreyBlock




class S_Tetrimnio:
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.straight_tetrimino = []
        self.grey_up_blocks = game.grey_up_blocks
        self.grey_down_blocks = game.grey_down_blocks
        self.grey_right_blocks = game.grey_right_blocks
        self.grey_left_blocks = game.grey_left_blocks
        self.last_time = pygame.time.get_ticks()
        self.second_position = False


    def add_tetrimnio(self):
        for num in range(4):
            orange_block = GreyBlock(self,"images/redsquare.bmp")
            center_position = self.settings.screen_block_face + 2
            starting_position = self.screen_rect.topleft[0] +  (center_position * orange_block.rect.width) 
            orange_block.rect.x = starting_position + (num * orange_block.rect.width)
            orange_block.rect.y = self.settings.square_yposition 
            orange_block.x_cord = orange_block.rect.x
            orange_block.y_cord = orange_block.rect.y
            self.straight_tetrimino.append(orange_block)
    
    def check_rotation(self):
        center_position = self.settings.screen_block_face +4
        rotate_position = self.screen_rect.topright[0] - (center_position * 20)
        if self.second_position:

            for block in self.straight_tetrimino:
                if block.rect.x > rotate_position:
                    self.settings.can_rotate = False
                else:
                    self.settings.can_rotate = True
            print(f"Can Rotate - {self.settings.can_rotate} ")
    
    def movement(self):
        self.check_rotation()
        last_index = self.straight_tetrimino[-1]
        first_index = self.straight_tetrimino[0]
        if self.settings.right_movement:
            if not self.second_position:
                if last_index.rect.x <= self.settings.left_block_coord - last_index.rect.width * 3:
                    for block in self.straight_tetrimino:
                        block.rect.x += self.settings.tetrimino_speed   
            else:
                for block in self.straight_tetrimino:
                    if block.rect.x <= self.settings.left_block_coord - last_index.rect.width *3:
                        block.rect.x += self.settings.tetrimino_speed

        if self.settings.left_movement:
            if not self.second_position:
                if first_index.rect.x >= self.settings.right_block_coord:
                    for block in self.straight_tetrimino:
                        block.rect.x += -self.settings.tetrimino_speed
            else:
                for block in self.straight_tetrimino:
                    if block.rect.x >= self.settings.right_block_coord:
                        block.rect.x += -self.settings.tetrimino_speed

        if self.settings.down_movement:
            if not self.second_position:
                if first_index.rect.y <= self.settings.square_bottom_yposition:
                    for block in self.straight_tetrimino:
                        block.rect.y += self.settings.tetrimino_speed 
            else:
                for block in self.straight_tetrimino:
                    if last_index.rect.y <= self.settings.square_bottom_yposition:
                        for block in self.straight_tetrimino:
                            block.rect.y += self.settings.tetrimino_speed                

        if self.settings.up_movement:
            counter = 0
            if not self.second_position:
                self.second_position = True
                starting_yposition = self.straight_tetrimino[0].rect.y
                starting_xposition = self.straight_tetrimino[0].rect.x
                for block in self.straight_tetrimino:
                        block.rect.y = starting_yposition + (block.rect.width * counter)
                        block.rect.x = starting_xposition
                        counter += 1
            elif self.settings.can_rotate:
                self.second_position = False
                starting_yposition = self.straight_tetrimino[-1].rect.y
                starting_xposition = self.straight_tetrimino[1].rect.x 
                for block in self.straight_tetrimino:
                    block.rect.y = starting_yposition
                    block.rect.x = starting_xposition + (block.rect.width * counter)
                    counter += 1
            self.settings.up_movement = False

        
        
    def blit_tetrimino(self):
        for block in self.straight_tetrimino:
            self.screen.blit(block.image, block.rect)