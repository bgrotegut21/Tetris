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
        self.can_collide = False
        self.can_rotate = True
        self.can_move = True
        self.add_tetrimnio()
        self.last_index = self.straight_tetrimino[-1]
        self.first_index = self.straight_tetrimino[0]
        self.last_time = pygame.time.get_ticks()


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
        right_position = self.settings.screen_block_face + 4
        left_position = self.settings.screen_block_face 
        right_rotation = self.screen_rect.topright[0] - (right_position * 20)
        left_rotation = self.screen_rect.topleft[0] + (left_position * 20)
        
        for block in self.straight_tetrimino:
            if block.rect.x > right_rotation:
                self.can_rotate = False
            elif block.rect.x < left_rotation:
                self.can_rotate = False
            else:
                self.can_rotate = True

    def _move_right_blocks(self):
        for block in self.straight_tetrimino:
            block.rect.x += self.settings.tetrimino_speed   

    def _move_left_blocks(self):
        for block in self.straight_tetrimino:
            block.rect.x += -self.settings.tetrimino_speed

    def right_movement(self):
        if self.settings.right_movement:
            if not self.second_position:
                if not self.can_collide:
                    if self.last_index.rect.x <= self.settings.left_block_coord - self.last_index.rect.width * 3:
                        self._move_right_blocks()
                else:
                    if self.last_index.rect.x <= self.settings.left_block_coord - self.last_index.rect.width * 6:
                        self._move_right_blocks()
            else:
                for block in self.straight_tetrimino:
                    if block.rect.x <= self.settings.left_block_coord - self.last_index.rect.width *3:
                        block.rect.x += self.settings.tetrimino_speed

    def left_movement(self):
        if self.settings.left_movement:
            if not self.second_position:
                if not self.can_collide:
                    if self.first_index.rect.x >= self.settings.right_block_coord:
                        self._move_left_blocks()
                else:
                    if self.first_index.rect.x >= self.settings.right_block_coord + 20:
                        self._move_left_blocks()
            else:
                for block in self.straight_tetrimino:
                    if block.rect.x >= self.settings.right_block_coord:
                        block.rect.x += -self.settings.tetrimino_speed
    
    def down_movement(self):
        if self.settings.down_movement:
            if not self.second_position:
                if self.first_index.rect.y <= self.settings.square_bottom_yposition:
                    for block in self.straight_tetrimino:
                        block.rect.y += self.settings.tetrimino_speed 
            else:
                for block in self.straight_tetrimino:
                    if self.last_index.rect.y <= self.settings.square_bottom_yposition:
                        for block in self.straight_tetrimino:
                            block.rect.y += self.settings.tetrimino_speed    

    def up_rotation(self):
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
            elif self.can_rotate:
                self.second_position = False
                starting_xposition = self.straight_tetrimino[0].rect.x
                starting_yposition = self.straight_tetrimino[0].rect.y
                for block in self.straight_tetrimino[:-1]:
                    block.rect.x = starting_xposition + (block.rect.width * counter)
                    block.rect.y = starting_yposition
                    counter += 1
                self.straight_tetrimino[-1].rect.x = self.straight_tetrimino[0].rect.x - 20
                self.straight_tetrimino[-1].rect.y = starting_yposition
                self.can_collide = True

            self.settings.up_movement = False


    def movement(self):
        current_time = pygame.time.get_ticks()
        self.check_rotation()
        print(f"last time - {self.last_time}")
        print(f"Current time - {current_time}")
        if current_time - self.last_time  >= self.settings.cool_down:
            self.last_time = current_time
            self.right_movement()
            self.left_movement()
            self.down_movement()
        self.up_rotation()

    def blit_tetrimino(self):
        for block in self.straight_tetrimino:
            self.screen.blit(block.image, block.rect)