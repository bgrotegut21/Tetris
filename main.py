
import pygame
import sys
import time
from settings import Settings
from greyspace import GreyBlock   
from  board import Board
from tetrimino import S_Tetrimnio
from scanner import Scanner


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode((1920,1080))
        self.screen_rect = self.screen.get_rect()
        self.grey_right_blocks = pygame.sprite.Group()
        self.grey_left_blocks = pygame.sprite.Group()
        self.grey_up_blocks = pygame.sprite.Group()
        self.grey_down_blocks = pygame.sprite.Group()
        self.board = pygame.sprite.Group()
        self.settings = Settings(self)
        self._create_greyblocks()
        self.s_tetrimnio = S_Tetrimnio(self)
        self.scanner = Scanner(self)
        self.backgroundcolor = self.settings.backgroundcolor
        self.last_time = pygame.time.get_ticks()
        
        self.current_tetrimino = []

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event.key)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event.key)

    def _check_keydown_events(self,event):
        if event == pygame.K_q:
            sys.exit()
        if event == pygame.K_RIGHT:
            print("key pressed")
            self.settings.right_movement = True
        if event == pygame.K_LEFT:
            print("left key pressed")
            self.settings.left_movement = True
        if event == pygame.K_DOWN:
            self.settings.down_movement = True
        if event == pygame.K_UP:
            self.settings.up_movement =  True
    def _check_keyup_events(self,event):
        if event == pygame.K_RIGHT:
            self.settings.right_movement = False
        if event == pygame.K_LEFT:
            self.settings.left_movement = False
        if event == pygame.K_DOWN:
            self.settings.down_movement = False

    def _create_greyblocks(self):
        block = GreyBlock(self)
        screen_block_space = self.screen_rect.width//block.rect.width
        right_blockspace = screen_block_space//2
        screen_block_fill_space = right_blockspace - 5
        screen_blockheight_space = (self.screen_rect.height//block.rect.width) 
        screen_fill_bottom_space = screen_blockheight_space//2
        screen_fill_bottom_cubes = screen_fill_bottom_space  - 10       
        screen_left_width = screen_block_fill_space
        screen_right_width = screen_block_fill_space
        
        if  not screen_block_fill_space % 2 == 0:
            screen_right_width = screen_block_fill_space + 1
            screen_left_width = screen_block_fill_space - 1
        
        print(screen_block_space)
    

        self._create_left_blocks(screen_left_width,screen_blockheight_space)
        self._create_right_blocks(screen_right_width,screen_blockheight_space)

        self._create_top_blocks(10,screen_fill_bottom_cubes)
        self._create_bottom_blocks(10,screen_fill_bottom_cubes)
        self._create_board(6,4)
    
    def _create_top_blocks(self,block_width, block_height):
        for height_number in range(block_height):
            for width_number in range(block_width):
                square = GreyBlock(self)
                screen_block_space = self.screen_rect.width//square.rect.width
                right_blockspace = screen_block_space//2

                screen_block_fill_space = right_blockspace -6
                starting_position = self.screen_rect.topleft[0]+ (screen_block_fill_space * square.rect.width)

                square.rect.x = starting_position + (width_number * square.rect.width)
                square.rect.y = self.screen_rect.topleft[1] + (height_number * square.rect.height)


                self.grey_up_blocks.add(square)
    
    def _create_bottom_blocks(self,block_width, block_height):
        for height_number in range(block_height):
            for width_number in range(block_width):
                square = GreyBlock(self)
                screen_block_space = self.screen_rect.width//square.rect.width
                right_blockspace = screen_block_space//2

                screen_block_fill_space = right_blockspace -6
                starting_position = self.screen_rect.topleft[0]+ (screen_block_fill_space * square.rect.width)

                square.rect.x = starting_position + (width_number * square.rect.width)
                square.rect.y = self.screen_rect.bottomleft[1] - (height_number * square.rect.height)


                self.grey_down_blocks.add(square)
        
        
    def _create_right_blocks(self,block_width, block_height):
        print(block_width)
        for height_number in range(block_height):
            for width_number in range(block_width + 1):
                square = GreyBlock(self)
                square.rect.x = self.screen_rect.topright[0] - (width_number * square.rect.width)
                square.rect.y = self.screen_rect.topright[1] + (height_number * square.rect.height)
                self.grey_right_blocks.add(square)

    def _create_left_blocks(self,block_width, block_height):
        print(block_width)
        for height_number in range(block_height):
            for width_number in range(block_width):
                square = GreyBlock(self)
                square.rect.x = self.screen_rect.topleft[0] + (width_number * square.rect.width)
                square.rect.y = self.screen_rect.topright[1] + (height_number * square.rect.height)
                self.grey_left_blocks.add(square)
    
    def _create_board(self, block_width, block_height):
        square = GreyBlock(self)
        screen_block_space = self.screen_rect.width//square.rect.width
        screen_blockheight_space = self.screen_rect.width // square.rect.height
        screen_fill_bottom_space = screen_blockheight_space//2
        screen_fill_bottom_cubes = screen_fill_bottom_space  - 33
        right_blockspace = screen_block_space//2
        board_xposition = right_blockspace + 11
        board_yposition = screen_fill_bottom_cubes + 6

        board_starting_xposition = self.screen_rect.topleft[0] + (board_xposition * square.rect.width)
        board_starting_yposition = self.screen_rect.topleft[1] + (board_yposition * square.rect.height)

        for height_number in range(block_height):
            for width_number in range(block_width):
                board = Board(self)
                board.rect.x = board_starting_xposition + (width_number * board.rect.width)
                board.rect.y = board_starting_yposition + (height_number * board.rect.height)
                self.board.add(board)
    
    def draw_board(self):
        for board in self.board:
            board.display_board()
    
    def tetrimino_collision(self):
        for block in self.s_tetrimnio.tetrimino:
            if block.rect.y >= self.settings.square_bottom_yposition+20:
                self.settings.stop_moving_tetrimino = True
                for new_block in self.s_tetrimnio.tetrimino:
                    self.scanner_collision(new_block.rect,new_block.image)
                break
    def block_collision(self):
        for s_block in self.s_tetrimnio.tetrimino:
            for position in self.scanner.scanner_blocks:
                for scanner_block in self.scanner.scanner_blocks[position]:
                    if scanner_block.can_collide_block:
                        if s_block.rect.y == scanner_block.rect.y - 20 and s_block.rect.x == scanner_block.rect.x:
                            self.settings.stop_moving_tetrimino = True

    def scanner_collision(self,block_rect, block_image):
        for position in self.scanner.scanner_blocks:
            for s_block in self.scanner.scanner_blocks[position]:
                if s_block.rect == block_rect and s_block.can_flip:
                    block = GreyBlock(self)
                    block.image = block_image
                    block.rect = s_block.rect
                    block.can_flip = False
                    s_block.can_flip = False
                    s_block.can_collide_block = True
                    self.scanner.scanner_blocks[position].add(block)

        print(f"Len of scanner blocks {len(self.scanner.scanner_blocks)}")
        self.settings.spawn_tetrimino = True

    def check_spawn_tetrimino(self):
        if self.settings.spawn_tetrimino:
            self.spawn_new_tetrimino()
            self.settings.spawn_tetrimino = False
        
    def check_scanner(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_time >= self.settings.empty_time:
            self.last_time = current_time
            for position in self.scanner.scanner_blocks:
                if len(self.scanner.scanner_blocks[position]) == 20:
                    self.scanner.clear_scanner_row(position)
                 

    def spawn_new_tetrimino(self):
        current_time = pygame.time.get_ticks()
        counter = 0
        for block in self.s_tetrimnio.tetrimino:
            center_position = self.settings.screen_block_face + 2
            statring_position = self.screen_rect.topleft[0] + (center_position * 20)
            block.rect.x = statring_position + (counter * 20)
            block.rect.y = self.settings.square_yposition
            counter += 1
        self.settings.stop_moving_tetrimino = False
        self.s_tetrimnio.can_collide = False
        self.s_tetrimnio.second_position = False



    def update_game(self):
        self.screen.fill((33,33,33)) 

        self.grey_right_blocks.draw(self.screen)
        self.grey_left_blocks.draw(self.screen)
        self.grey_up_blocks.draw(self.screen)
        self.grey_down_blocks.draw(self.screen)
        self.draw_board()
        self.tetrimino_collision()
        self.s_tetrimnio.movement()
        self.scanner.draw_scanner()
        self.tetrimino_collision()
        self.block_collision()
        self.check_scanner()
        self.s_tetrimnio.auto_movement()
        self.s_tetrimnio.blit_tetrimino()
        self.check_spawn_tetrimino()

        pygame.display.flip()

    
    def run_game(self):
        while True:
            self.check_events()
            self.update_game()


if __name__ == "__main__":
    main = Main()
    main.run_game()