
import pygame
import sys
from settings import Settings
from greyspace import GreyBlock   
from  board import Board


class Main:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.backgroundcolor = self.settings.backgroundcolor
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode((1920,1080))
        self.screen_rect = self.screen.get_rect()
        self.grey_blocks = pygame.sprite.Group()
        self._create_greyblocks()
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

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


                self.grey_blocks.add(square)
    
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


                self.grey_blocks.add(square)
        
        
    def _create_right_blocks(self,block_width, block_height):
        print(block_width)
        for height_number in range(block_height):
            for width_number in range(block_width + 1):
                square = GreyBlock(self)
                square.rect.x = self.screen_rect.topright[0] - (width_number * square.rect.width)
                square.rect.y = self.screen_rect.topright[1] + (height_number * square.rect.height)
                self.grey_blocks.add(square)

    def _create_left_blocks(self,block_width, block_height):
        print(block_width)
        for height_number in range(block_height):
            for width_number in range(block_width):
                square = GreyBlock(self)
                square.rect.x = self.screen_rect.topleft[0] + (width_number * square.rect.width)
                square.rect.y = self.screen_rect.topright[1] + (height_number * square.rect.height)
                self.grey_blocks.add(square)
    
    def _create_board(self, block_width, block_height):
        square = GreyBlock(self)
        screen_block_space = self.screen_rect.width//square.rect.width
        screen_blockheight_space = self.screen_rect.width // square.rect.height
        screen_fill_bottom_space = screen_blockheight_space//2
        screen_fill_bottom_cubes = screen_fill_bottom_space  - 10
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
                self.grey_blocks.add(board)

    
        
    def update_game(self):
        self.screen.fill((33,33,33))
        self.grey_blocks.draw(self.screen)
        pygame.display.flip()

    
    def run_game(self):
        while True:
            self.check_events()
            self.update_game()


if __name__ == "__main__":
    main = Main()
    main.run_game()