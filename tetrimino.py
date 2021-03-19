import pygame
from pygame.sprite import Sprite


class Tetromino(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        sqaure_size = 20
        self.square_xamount = self.screen_rect//sqaure_size
        self.right_position = self.square_xamount//2
        self.screen_block_face = self.right_position - 5
        self.settings = game.settings
        self.straight_tetrimnio = pygame.sprite.Group()
    
    def s_tetrimnio(self):
        for num in range(4):
            orange_image = pygame.image.load("images/orangesquare.jpg")
            orange_rect = orange_image.get_rect()
            center_position = self.right_position + 3
            

