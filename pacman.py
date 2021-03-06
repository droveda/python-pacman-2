from constants import Constants
from game_element import GameElement
from game_state import GameState
from movable import Movable


class Pacman(GameElement, Movable):
    def __init__(self, size, pygame, game_state):
        self.pygame = pygame
        self.column = 1
        self.row = 1
        self.x_center = 30
        self.y_center = 30
        self.size = size
        self.speed_x = 0
        self.speed_y = 0
        self.radius = int(self.size / 2)
        self.fixed_radius = int(self.size / 2)
        self.column_intention = self.column
        self.row_intention = self.row
        self.gap = 0
        self.gap_speed = 1
        self.state = game_state
        self.radius_speed = -0.5
        self.death = False

    def reset_radius(self):
        self.radius = int(self.size / 2)

    def calc_rules(self):
        if self.state.get_current_state() != GameState.PAUSED_USER:
            self.column_intention = self.column + self.speed_x
            self.row_intention = self.row + self.speed_y
            self.x_center = int(self.column * self.size + self.fixed_radius)
            self.y_center = int(self.row * self.size + self.fixed_radius)

    def paint(self, screen):
        # draw pacman body
        self.pygame.draw.circle(screen, Constants.YELLOW, (self.x_center, self.y_center), self.radius, 0)

        if self.death:
            self.death_animation()

        self.calc_mouth_animation()

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

    def death_animation(self):
        self.radius += int(self.radius_speed)
        if self.radius >= 10:
            self.radius_speed = -1
        if self.radius == 0:
            self.radius_speed = 0

    def calc_mouth_animation(self):
        self.gap += self.gap_speed
        # print(self.gap)
        if self.gap > self.radius:
            self.gap_speed = -1
        if self.gap <= 0:
            self.gap_speed = 1

    def process_events(self, events):
        self.movement_method2(events)

    def movement_method1(self, events):
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

    def movement_method2(self, events):
        for e in events:
            if e.type == self.pygame.KEYDOWN:
                if e.key == self.pygame.K_RIGHT:
                    self.speed_x = Constants.SPEED
                    self.speed_y = 0
                elif e.key == self.pygame.K_LEFT:
                    self.speed_x = -Constants.SPEED
                    self.speed_y = 0
                elif e.key == self.pygame.K_UP:
                    self.speed_y = -Constants.SPEED
                    self.speed_x = 0
                elif e.key == self.pygame.K_DOWN:
                    self.speed_y = Constants.SPEED
                    self.speed_x = 0

    def accept_movement(self):
        self.row = self.row_intention
        self.column = self.column_intention

    def deny_movement(self, directions):
        self.row_intention = self.row
        self.column_intention = self.column

    def corner(self, directions):
        pass

    # def play_effect(self):
    #     thread = ThreadSound(self.pygame, self.munch1)
    #     thread.start()
    #
    #     thread2 = ThreadSound(self.pygame, self.munch2)
    #     thread2.start()
    #
    #     thread.join()
    #     thread2.join()
