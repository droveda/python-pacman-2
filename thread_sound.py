import threading
from game_state import GameState


class ThreadSound(threading.Thread):
    def __init__(self, pygame, sound, game_state):
        threading.Thread.__init__(self)
        self.sound = sound
        self.pygame = pygame
        self.state = game_state
        # print("init...")

    def run(self) -> None:
        # print("Playing...")
        channel = self.sound.play()

        while channel.get_busy():
            continue

        print("Terminou...")
        self.state.set_current_state(GameState.RUNNING)
        # self.pygame.time.wait(1)  # ms
        # print("Playing pac_fx1...")
