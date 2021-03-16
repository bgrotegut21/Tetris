import pygame
import sys
from settings import Settings
from greyspace import GreyBlock   

class Main:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.backgroundcolor = self.settings.backgroundcolor
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
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
        right_blockspacce = screen_block_space//2
        screen_block_fill_space = right_blockspace - (5* block.rect.width)
        screen_blockheight_space = self.screen_rect.height//block.rect.width
        
    def _create_right_blocks(self,block_width, block_height):
        for height_number in range(block_height):
            for width_number in range(block_width):
                square = GreyBlock(self)
                square.rect.x = self.screen_rect.topright[0] - (width_number * square.rect.width)
                square.rect.y = self.screen_rect.topright[1] + (height_number * square.rect.height)
                self.grey_blocks.add(square)

    def _create_left_blocks(self,block_width, block_height):
        for height_number in range(block_height):
            for width_number in range(block_width):
                square = GreyBlock(self)
                square.rect.x = self.screen_rect.topleft[0] + (width_number * square.rect.width)
                square.rect.y = self.screen_rect.topright[1] + (height_number * square.rect.height)
                self.grey_blocks.add(square)
    
        
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