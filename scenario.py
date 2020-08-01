from constants import Constants
from game_element import GameElement
from game_state import GameState
from ghost import Ghost
from pacman import Pacman
from scenario_matrix import ScenarioMatrix


class Scenario(GameElement):

    def __init__(self, size, pac, pygame, font):
        self.font = font
        self.pygame = pygame
        self.pacman = pac
        self.state = GameState.RUNNING
        self.movables = []
        self.size = size
        self.score = 0
        self.lifes = 3
        self.matrix = ScenarioMatrix().get_matrix()

    def add_movable(self, movable):
        self.movables.append(movable)

    def paint_row(self, screen, row_number, row):
        for column_number, column in enumerate(row):
            x = column_number * self.size
            y = row_number * self.size
            half = self.size // 2
            color = Constants.BLACK
            if column == 2:
                color = Constants.BLUE
            self.pygame.draw.rect(screen, color, (x, y, self.size, self.size), 0)

            if column == 1:
                self.pygame.draw.circle(screen, Constants.YELLOW, (x + half, y + half), self.size // 10, 0)

    def paint(self, screen):
        if self.state == GameState.RUNNING:
            self.paint_playing(screen)
        elif self.state == GameState.PAUSED:
            self.paint_playing(screen)
            self.paint_paused(screen)
        elif self.state == GameState.GAME_OVER:
            self.paint_playing(screen)
            self.paint_game_over(screen)
        elif self.state == GameState.FINISH:
            self.paint_playing(screen)
            self.paint_finish(screen)

    def paint_finish(self, screen):
        self.paint_text_center(screen, "Congratulations - You Win")

    def paint_text_center(self, screen, text):
        text_img = self.font.render(text, True, Constants.YELLOW)
        x_text = (800 - text_img.get_width()) // 2
        y_text = (600 - text_img.get_height()) // 2
        screen.blit(text_img, (x_text, y_text))

    def paint_game_over(self, screen):
        self.paint_text_center(screen, "G A M E - O V E R")

    def paint_paused(self, screen):
        self.paint_text_center(screen, "P A U S E D")

    def paint_playing(self, screen):
        for row_number, row in enumerate(self.matrix):
            self.paint_row(screen, row_number, row)
        self.show_score(screen)

    def calc_rules(self):
        if self.state == GameState.RUNNING:
            self.calc_rules_playing()
        elif self.state == GameState.PAUSED:
            self.calc_rules_paused()
        elif self.state == GameState.GAME_OVER:
            self.calc_rules_game_over()

    def calc_rules_game_over(self):
        pass

    def calc_rules_paused(self):
        pass

    def calc_rules_playing(self):
        for movable in self.movables:
            row = int(movable.row)
            column = int(movable.column)
            row_intention = int(movable.row_intention)
            column_intention = int(movable.column_intention)
            directions = self.get_directions(row, column)
            if len(directions) >= 3:
                movable.corner(directions)
            if isinstance(movable, Ghost) and movable.row == self.pacman.row and movable.column == self.pacman.column:
                self.lifes -= 1
                if self.lifes <= 0:
                    self.state = GameState.GAME_OVER
                    self.pacman.row = 1
                    self.pacman.column = 1
                else:
                    self.pacman.row = 1
                    self.pacman.column = 1
            else:
                if 0 <= column_intention < 28 and 0 <= row_intention < 29 and self.matrix[row_intention] \
                        [column_intention] != 2:
                    movable.accept_movement()
                    if isinstance(movable, Pacman) and self.matrix[row][column] == 1:
                        self.score += 1
                        self.matrix[row][column] = 0
                        if self.score >= 306:
                            self.state = GameState.FINISH
                else:
                    movable.deny_movement(directions)

    def show_score(self, screen):
        score_x = 30 * self.size
        img_score = self.font.render("Score: {}".format(self.score), True, Constants.YELLOW)
        lifes_img = self.font.render("Life {}".format(self.lifes), True, Constants.YELLOW)
        screen.blit(img_score, (score_x, 50))
        screen.blit(lifes_img, (score_x, 100))

    def process_events(self, events):
        for e in events:
            if e.type == self.pygame.QUIT:
                exit()
            if e.type == self.pygame.KEYDOWN:
                if e.key == self.pygame.K_p:
                    self.pause_game()
                if e.key == self.pygame.K_s:
                    self.reboot_game()

    def pause_game(self):
        if self.state != GameState.GAME_OVER and self.state != GameState.FINISH:
            if self.state == GameState.RUNNING:
                self.state = GameState.PAUSED
            else:
                self.state = GameState.RUNNING

    def reboot_game(self):
        if self.state == GameState.GAME_OVER or self.state == GameState.FINISH:
            self.state = GameState.RUNNING
            self.lifes = 3
            self.pacman.row = 1
            self.pacman.column = 1
            self.matrix = ScenarioMatrix().get_matrix()
            self.score = 0
            for movable in self.movables:
                if isinstance(movable, Ghost):
                    movable.column = 12.0
                    movable.row = 15.0

    def get_directions(self, row, column):
        directions = []
        # checking if the ghost can go up
        if self.matrix[int(row - 1)][int(column)] != 2:
            directions.append(Constants.UP)
        # checking if the ghost can go down
        if self.matrix[int(row + 1)][int(column)] != 2:
            directions.append(Constants.DOWN)
        # checking if the ghost can go left
        if self.matrix[int(row)][int(column - 1)] != 2:
            directions.append(Constants.LEFT)
        # checking if the ghost can go right
        if self.matrix[int(row)][int(column + 1)] != 2:
            directions.append(Constants.RIGHT)

        return directions
