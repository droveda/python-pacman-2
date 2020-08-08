from constants import Constants
from game_element import GameElement
from game_state import GameState
from ghost import Ghost
from pacman import Pacman
from scenario_matrix import ScenarioMatrix
from thread_death import ThreadDeath


class Scenario(GameElement):

    def __init__(self, size, pac, pygame, font, clock, game_sound, game_state):
        self.font = font
        self.pygame = pygame
        self.pacman = pac
        self.state = game_state
        self.movables = []
        self.size = size
        self.score = 0
        self.lifes = 3
        self.matrix = ScenarioMatrix().get_matrix()
        self.clock = clock
        self.is_playing = False
        self.game_sound = game_sound
        self.game_sound.set_scenario(self)

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
        if self.state.is_game_running():
            self.paint_playing(screen)
        elif self.state.is_paused_by_user():
            self.paint_playing(screen)
            self.paint_paused(screen)
        elif self.state.is_game_over():
            self.paint_playing(screen)
            self.paint_game_over(screen)
        elif self.state.is_finished():
            self.paint_playing(screen)
            self.paint_finish(screen)
        elif self.state.is_paused():
            self.paint_playing(screen)

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
        if self.state.is_game_running():
            self.calc_rules_playing()
        elif self.state.is_paused_by_user():
            self.calc_rules_paused_user()
        elif self.state.is_game_over():
            self.calc_rules_game_over()
        elif self.state.is_paused():
            self.calc_rules_paused()

    def calc_rules_game_over(self):
        pass

    def calc_rules_paused_user(self):
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
                self.death()
            else:
                if 0 <= column_intention < 28 and 0 <= row_intention < 29 and self.matrix[row_intention] \
                        [column_intention] != 2:
                    movable.accept_movement()
                    if isinstance(movable, Pacman) and self.matrix[row][column] == 1:
                        self.score += 1
                        self.game_sound.play_munch()
                        self.matrix[row][column] = 0
                        if self.score >= 306:
                            self.state.set_current_state(GameState.FINISH)
                    else:
                        self.is_playing = False
                else:
                    movable.deny_movement(directions)

    def death(self):
        thread = ThreadDeath(self.pygame, self.game_sound.death1, self)
        thread.start()

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
        if self.state.get_current_state() != GameState.GAME_OVER and self.state.get_current_state() != GameState.FINISH:
            if self.state.get_current_state() == GameState.RUNNING:
                self.state.set_current_state(GameState.PAUSED_USER)
                self.game_sound.pause_music()
            else:
                self.state.set_current_state(GameState.RUNNING)
                self.game_sound.resume_music()

    def reboot_game(self):
        self.lifes = 3
        self.pacman.row = 1
        self.pacman.column = 1
        self.matrix = ScenarioMatrix().get_matrix()
        self.score = 0
        self.reset_ghosts()
        self.state.set_current_state(GameState.PAUSED)
        self.game_sound.play_start_music()

    def reset_ghosts(self):
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
