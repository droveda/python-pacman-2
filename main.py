import pygame

from constants import Constants
from game_sounds import GameSounds
from ghost import Ghost
from pacman import Pacman
from scenario import Scenario

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
font = pygame.font.SysFont('arial', 24, True, False)

clock = pygame.time.Clock()

if __name__ == "__main__":
    c = Constants(pygame)

    size = 600 // 30
    game_sounds = GameSounds(pygame, c)
    game_sounds.play_start_music()

    pacman = Pacman(size, pygame)
    blinky = Ghost(Constants.RED, size, pygame)
    inky = Ghost(Constants.CYAN, size, pygame)
    clyde = Ghost(Constants.ORANGE, size, pygame)
    pinky = Ghost(Constants.PINK, size, pygame)
    scenario = Scenario(size, pacman, pygame, font, clock, game_sounds)
    scenario.add_movable(pacman)
    scenario.add_movable(blinky)
    scenario.add_movable(inky)
    scenario.add_movable(clyde)
    scenario.add_movable(pinky)



    while True:
        # calc the rules
        pacman.calc_rules()
        blinky.calc_rules()
        inky.calc_rules()
        clyde.calc_rules()
        pinky.calc_rules()
        scenario.calc_rules()

        # paint screen
        screen.fill(Constants.BLACK)
        scenario.paint(screen)
        pacman.paint(screen)
        blinky.paint(screen)
        inky.paint(screen)
        clyde.paint(screen)
        pinky.paint(screen)
        pygame.display.update()
        # pygame.time.delay(100)

        # events
        events = pygame.event.get()
        scenario.process_events(events)
        pacman.process_events(events)
        game_sounds.process_events(events)

        clock.tick(Constants.FRAME_RATE)
