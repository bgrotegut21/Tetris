
import pygame
import sys
import time

from pygame.draw import rect
from settings import Settings
from greyspace import GreyBlock   
from  board import Board
from tetrimino import S_Tetrimnio
from scanner import Scanner
from pseudo_rect import PseudoRect


class Main:
    def __init__(self):
        pygame.init()
        pygame.display. set_caption("Tetris")
        self.screen = pygame.display.set_mode((1920, 900))
        self.screen_rect = self.screen.get_rect()
        self.grey_right_blocks = pygame.sprite.Group()
        self.grey_left_blocks = pygame.sprite.Group()
        self.grey_up_blocks = pygame.sprite.Group()
        self.grey_down_blocks = pygame.sprite.Group()
        self.board = pygame.sprite.Group()
        self.settings = Settings(self)
        self._create_greyblocks()
        self.scanner = Scanner(self)
        self.s_tetrimino = S_Tetrimnio(self)
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
        self._create_bottom_blocks(10,screen_fill_bottom_cubes +8) # +8 when working on 15 inch black hp laptop
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

    def add_blocks(self):
        for new_block in self.s_tetrimino.tetrimino:
            self.scanner_collision(new_block.rect, new_block.image)
    
    def tetrimino_collision(self):
        for block in self.s_tetrimino.tetrimino:
            if block.rect.y >= self.settings.square_bottom_yposition-20:
                self.settings.stop_moving_tetrimino = True
                self.add_blocks()

                break
    def block_collision(self):
        for position in self.scanner.scanner_blocks:
            for block in self.scanner.scanner_blocks[position]:
                if not block.pseudo_rect:
                    if block.can_collide_block:
                        for s_block in self.s_tetrimino.tetrimino:
                            if s_block.rect.y == block.rect.y -20:
                                if s_block.rect.x == block.rect.x:
                                    self.add_blocks()


                                
    def scanner_collision(self,block_rect, block_image):
        for position in self.scanner.scanner_blocks:
            for s_block in self.scanner.scanner_blocks[position]:
                if not s_block.pseudo_rect:
                    if s_block.rect == block_rect and s_block.can_flip:
                        block = GreyBlock(self)
                        block.image = block_image
                        block.rect.x = s_block.rect.x
                        block.rect.y = s_block.rect.y
                        block.can_flip = False
                        s_block.can_flip = False
                        s_block.can_collide_block = True
                        s_block.right_collision = True
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

    def current_position(self,scanner_block):
        for block in self.s_tetrimino.tetrimino:
            collision = block.rect.colliderect(scanner_block.rect)
            if collision:
                block.position = block.rect


    def spawn_new_tetrimino(self):
        current_time = pygame.time.get_ticks()
        counter = 0
        for block in self.s_tetrimino.tetrimino:
            center_position = self.settings.screen_block_face + 1
            statring_position = self.screen_rect.topleft[0] + (center_position * 20) 
            block.rect.x = statring_position + (counter * 20)
            block.rect.y = self.settings.square_yposition 
            counter += 1
        self.settings.stop_moving_tetrimino = False
        self.s_tetrimino.second_position = False
        self.s_tetrimino.can_collide = False

    def create_pseudo_rect(self):
        rect_position = True
        rect_width = 0
        rect_height = 20
        rect_xcoord = 0
        rect_ycoord = 0
        create_block = False
        for position in self.scanner.scanner_blocks:
            for blocks in self.scanner.scanner_blocks[position]:
                if not blocks.pseudo_rect:
                    if blocks.can_collide_block:

                        if blocks.created_pseudo_rect == False:
                            print("something")
                            if rect_position:
                                rect_xcoord = blocks.rect.x
                                rect_ycoord = blocks.rect.y
                                rect_position = False
                            rect_width += 20
                            blocks.created_pseudo_rect = True
                            print(f"len of scanner blocks {position} - {self.scanner.scanner_blocks[position]}")
                    else:
                        rect_position = True
                        create_block = True
            if create_block:
                create_block = False
                self.check_pseudo_rect(rect_width,rect_height,rect_xcoord,rect_ycoord)
                rect_width = 0
                rect_xcoord = 0
                rect_ycoord = 0

    def check_pseudo_rect(self,width,height,xcoord,ycoord):
        for position in self.scanner.scanner_blocks:
            for blocks in self.scanner.scanner_blocks[position]:
                if blocks.pseudo_rect:
                    if width != blocks.rect.width:
                        self.make_pseudo_rect(width,height,xcoord,ycoord,position)
                else:
                    self.make_pseudo_rect(width,height,xcoord,ycoord,position)

    def make_pseudo_rect(self,width,height,xcoord,ycoord,position):
        print("It is working")
        pseudo_rect = PseudoRect(self,width,height)
        pseudo_rect.rect.x = xcoord
        pseudo_rect.rect.x = ycoord
        self.scanner.scanner_blocks[position].add(pseudo_rect)
            
        
    def draw_pseudo_rect(self):
        for position in self.scanner.scanner_blocks:
            for block in self.scanner.scanner_blocks[position]:
                if block.pseudo_rect:
                    block.draw_pseudo_rect()

    def update_game(self):
        self.screen.fill((33,33,33)) 

        self.grey_right_blocks.draw(self.screen)
        self.grey_left_blocks.draw(self.screen)
        self.grey_up_blocks.draw(self.screen)
        self.grey_down_blocks.draw(self.screen)
        self.draw_board()
        self.tetrimino_collision()
        self.s_tetrimino.movement()
        self.scanner.draw_scanner()
        self.tetrimino_collision()
        self.block_collision()
        self.check_scanner()
        self.create_pseudo_rect()
        self.s_tetrimino.collision_detection()
        self.s_tetrimino.auto_movement()
        self.s_tetrimino.find_position()
        self.s_tetrimino.blit_tetrimino()
        self.check_spawn_tetrimino()
        self.draw_pseudo_rect()

        pygame.display.flip()

    
    def run_game(self):
        while True:
            self.check_events()
            self.update_game()


if __name__ == "__main__":
    main = Main()
    main.run_game()