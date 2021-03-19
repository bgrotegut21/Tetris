class Settings:
    def __init__(self):
        self.backgroundcolor = (33,33,33)
    
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        sqaure_size = 20
        self.square_xamount = self.screen_rect.width//sqaure_size
        self.square_yamount = self.screen_rect.height//sqaure_size
        self.square_ycord = (self.square_yamount//2) -9
        print(self.square_ycord)
        self.square_yposition = self.screen_rect.topleft[0] + (self.square_ycord * sqaure_size)
        self.right_position = self.square_xamount//2
        self.screen_block_face = self.right_position - 5
        self.tetrimino_speed = 20

        self.settings = game.settings


        