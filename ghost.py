import random

from constants import Constants
from game_element import GameElement
from movable import Movable


class Ghost(GameElement, Movable):
    def __init__(self, color, size, pygame):
        self.column = 12.0
        self.row = 12.0
        self.color = color
        self.size = size
        self.pygame = pygame
        self.speed = Constants.SPEED
        self.direction = Constants.DOWN
        self.row_intention = self.row
        self.column_intention = self.column

    def paint(self, screen):
        slice = self.size // 8
        px = int(self.column * self.size)
        py = int(self.row * self.size)
        outline = [
            (px, py + self.size),
            (px + slice, py + slice * 2),
            (px + slice * 2, py + slice // 2),
            (px + slice * 3, py),
            (px + slice * 5, py),
            (px + slice * 6, py + slice // 2),
            (px + slice * 7, py + slice * 2),
            (px + self.size, py + self.size)
        ]
        self.pygame.draw.polygon(screen, self.color, outline, 0)

        external_eye_radius = slice
        internal_eye_radius = slice // 2

        x_left_eye = int(px + slice * 2.5)
        y_left_eye = int(py + slice * 2.5)

        x_right_eye = int(px + slice * 5.5)
        y_right_eye = int(py + slice * 2.5)

        self.pygame.draw.circle(screen, Constants.WHITE, (x_left_eye, y_left_eye), external_eye_radius, 0)
        self.pygame.draw.circle(screen, Constants.BLACK, (x_left_eye, y_left_eye), internal_eye_radius, 0)
        self.pygame.draw.circle(screen, Constants.WHITE, (x_right_eye, y_right_eye), external_eye_radius, 0)
        self.pygame.draw.circle(screen, Constants.BLACK, (x_right_eye, y_right_eye), internal_eye_radius, 0)

    def calc_rules(self):
        if self.direction == Constants.UP:
            self.row_intention -= self.speed
        elif self.direction == Constants.DOWN:
            self.row_intention += self.speed
        elif self.direction == Constants.LEFT:
            self.column_intention -= self.speed
        elif self.direction == Constants.RIGHT:
            self.column_intention += self.speed

    def process_events(self, events):
        pass

    def corner(self, directions):
        self.change_direction(directions)

    def accept_movement(self):
        self.row = self.row_intention
        self.column = self.column_intention

    def deny_movement(self, directions):
        self.row_intention = self.row
        self.column_intention = self.column
        self.change_direction(directions)

    def change_direction(self, directions):
        self.direction = random.choice(directions)
