from constants import Constants
from game_element import GameElement
from movable import Movable


class Pacman(GameElement, Movable):
    def __init__(self, size, pygame):
        self.pygame = pygame
        self.column = 1
        self.row = 1
        self.x_center = 400
        self.y_center = 300
        self.size = size
        self.speed_x = 0
        self.speed_y = 0
        self.radius = int(self.size / 2)
        self.column_intention = self.column
        self.row_intention = self.row
        self.gap = 0
        self.gap_speed = 1

    def calc_rules(self):
        self.column_intention = self.column + self.speed_x
        self.row_intention = self.row + self.speed_y
        self.x_center = int(self.column * self.size + self.radius)
        self.y_center = int(self.row * self.size + self.radius)

    def paint(self, screen):
        # draw pacman body
        self.pygame.draw.circle(screen, Constants.YELLOW, (self.x_center, self.y_center), self.radius, 0)

        self.gap += self.gap_speed
        if self.gap > self.radius:
            self.gap_speed = -1
        if self.gap <= 0:
            self.gap_speed = 1

        # draw pacman mouth
        mouth_edge = (self.x_center, self.y_center)
        upper_lip = (self.x_center + self.radius, self.y_center - self.gap)
        bottom_lip = (self.x_center + self.radius, self.y_center + self.gap)
        dots = [mouth_edge, upper_lip, bottom_lip]
        self.pygame.draw.polygon(screen, Constants.BLACK, dots, 0)

        # draw pacman eye
        eye_x = int(self.x_center + self.radius / 3)
        eye_y = int(self.y_center - self.radius * 0.7)
        eye_radius = int(self.radius / 10)
        self.pygame.draw.circle(screen, Constants.BLACK, (eye_x, eye_y), eye_radius, 0)

    def process_events(self, events):
        for e in events:
            if e.type == self.pygame.KEYDOWN:
                if e.key == self.pygame.K_RIGHT:
                    self.speed_x = Constants.SPEED
                elif e.key == self.pygame.K_LEFT:
                    self.speed_x = -Constants.SPEED
                elif e.key == self.pygame.K_UP:
                    self.speed_y = -Constants.SPEED
                elif e.key == self.pygame.K_DOWN:
                    self.speed_y = Constants.SPEED
            if e.type == self.pygame.KEYUP:
                if e.key == self.pygame.K_RIGHT:
                    self.speed_x = 0
                elif e.key == self.pygame.K_LEFT:
                    self.speed_x = 0
                elif e.key == self.pygame.K_UP:
                    self.speed_y = 0
                elif e.key == self.pygame.K_DOWN:
                    self.speed_y = 0

    def accept_movement(self):
        self.row = self.row_intention
        self.column = self.column_intention

    def deny_movement(self, directions):
        self.row_intention = self.row
        self.column_intention = self.column

    def corner(self, directions):
        pass
