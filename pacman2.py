import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
font = pygame.font.SysFont('arial', 24, True, False)

YELLOW = (250, 250, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
SPEED = 1


class Scenario:
    def __init__(self, size, pac):
        self.pacman = pac
        self.size = size
        self.score = 0
        self.matrix = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def paint_row(self, screen, row_number, row):
        for column_number, column in enumerate(row):
            x = column_number * self.size
            y = row_number * self.size
            half = size // 2
            color = BLACK
            if column == 2:
                color = BLUE
            pygame.draw.rect(screen, color, (x, y, self.size, self.size), 0)

            if column == 1:
                pygame.draw.circle(screen, YELLOW, (x + half, y + half), self.size // 10, 0)

    def paint(self, screen):
        for row_number, row in enumerate(self.matrix):
            self.paint_row(screen, row_number, row)
        self.show_score(screen)

    def calculate_rules(self):
        column = self.pacman.column_intention
        row = self.pacman.row_intention
        if 0 <= column < 28 and 0 <= row < 29:
            if self.matrix[row][column] != 2:
                self.pacman.accept_movement()
                if self.matrix[row][column] == 1:
                    self.score += 1
                    self.matrix[row][column] = 0

    def show_score(self, screen):
        score_x = 30 * self.size
        img_score = font.render("Score: {}".format(self.score), True, YELLOW)
        screen.blit(img_score, (score_x, 50))


class Pacman:
    def __init__(self, size):
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

    def calc_rules(self):
        self.column_intention = self.column + self.speed_x
        self.row_intention = self.row + self.speed_y
        self.x_center = int(self.column * self.size + self.radius)
        self.y_center = int(self.row * self.size + self.radius)

    def paint(self, screen):
        # draw pacman body
        pygame.draw.circle(screen, YELLOW, (self.x_center, self.y_center), self.radius, 0)

        # draw pacman mouth
        mouth_edge = (self.x_center, self.y_center)
        upper_lip = (self.x_center + self.radius, self.y_center - self.radius)
        bottom_lip = (self.x_center + self.radius, self.y_center)
        dots = [mouth_edge, upper_lip, bottom_lip]
        pygame.draw.polygon(screen, BLACK, dots, 0)

        # draw pacman eye
        eye_x = int(self.x_center + self.radius / 3)
        eye_y = int(self.y_center - self.radius * 0.7)
        eye_radius = int(self.radius / 10)
        pygame.draw.circle(screen, BLACK, (eye_x, eye_y), eye_radius, 0)

    def process_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.speed_x = SPEED
                elif e.key == pygame.K_LEFT:
                    self.speed_x = -SPEED
                elif e.key == pygame.K_UP:
                    self.speed_y = -SPEED
                elif e.key == pygame.K_DOWN:
                    self.speed_y = SPEED
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.speed_x = 0
                elif e.key == pygame.K_LEFT:
                    self.speed_x = 0
                elif e.key == pygame.K_UP:
                    self.speed_y = 0
                elif e.key == pygame.K_DOWN:
                    self.speed_y = 0

    def accept_movement(self):
        self.row = self.row_intention
        self.column = self.column_intention


if __name__ == "__main__":
    size = 600 // 30
    pacman = Pacman(size)
    scenario = Scenario(size, pacman)

    while True:
        # calc the rules
        pacman.calc_rules()
        scenario.calculate_rules()

        # paint screen
        screen.fill(BLACK)
        scenario.paint(screen)
        pacman.paint(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
        pacman.process_events(events)
