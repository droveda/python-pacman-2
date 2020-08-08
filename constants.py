class Constants:
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    SPEED = 1
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    CYAN = (0, 255, 255)
    ORANGE = (255, 140, 0)
    PINK = (255, 15, 192)
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4
    STOPPED = 0
    FRAME_RATE = 8

    def __init__(self, pygame):
        self.pygame = pygame

    def get_event_song_ended(self):
        return self.pygame.USEREVENT + 1
