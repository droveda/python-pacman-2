import threading

from game_state import GameState


class ThreadDeath(threading.Thread):
    def __init__(self, pygame, sound, scenario):
        threading.Thread.__init__(self)
        self.sound = sound
        self.pygame = pygame
        self.scenario = scenario
        # print("init...")

    def run(self) -> None:
        self.scenario.state.set_current_state(GameState.PAUSED)
        self.scenario.pacman.death = True
        # print("Playing...")
        channel = self.sound.play()

        while channel.get_busy():
            continue

        print("death finish...")
        self.scenario.pacman.death = False
        self.scenario.pacman.reset_radius()
        self.scenario.reset_ghosts()
        self.scenario.state.set_current_state(GameState.RUNNING)
        self.scenario.lifes -= 1
        if self.scenario.lifes <= 0:
            self.scenario.state.set_current_state(GameState.GAME_OVER)
            self.scenario.pacman.row = 1
            self.scenario.pacman.column = 1
            self.scenario.game_sound.stop_siren()
        else:
            self.scenario.pacman.row = 1
            self.scenario.pacman.column = 1

        # self.pygame.time.wait(1)  # ms
        # print("Playing pac_fx1...")
