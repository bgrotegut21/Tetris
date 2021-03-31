class Settings:
    def __init__(self, game):
        self.backgroundcolor = (33,33,33)
    
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        sqaure_size = 20
        self.square_xamount = self.screen_rect.width//sqaure_size
        self.square_yamount = self.screen_rect.height//sqaure_size
        self.square_ycord = (self.square_yamount//2) -10
        print(self.square_ycord)
        self.square_yposition = self.screen_rect.topleft[0] + (self.square_ycord * sqaure_size)
        self.square_bottom_yposition = self.screen_rect.bottomleft[1] - (18 * sqaure_size)
        self.right_position = self.square_xamount//2
        self.screen_block_face = self.right_position - 5
        self.right_block_coord = self.screen_rect.topleft[0] + (self.screen_block_face * sqaure_size)
        self.left_block_coord = self.screen_rect.topright[0] - (self.screen_block_face * sqaure_size)
        self.tetrimino_speed = 20
        self.down_movement = False
        self.right_movement = False
        self.left_movement = False
        self.up_movement = False
        self.stop_moving_tetrimino = False

        self.cool_down = 50