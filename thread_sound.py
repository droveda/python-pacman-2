import threading


class ThreadSound(threading.Thread):
    def __init__(self, pygame, sound):
        threading.Thread.__init__(self)
        self.sound = sound
        self.pygame = pygame
        # print("init...")

    def run(self) -> None:
        # print("Playing...")
        channel = self.sound.play()

        while channel.get_busy():
            continue
            # self.pygame.time.wait(1)  # ms
            # print("Playing pac_fx1...")
