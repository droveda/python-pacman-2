from game_element import GameElement


class GameSounds(GameElement):

    def __init__(self, pygame, constants):
        self.pygame = pygame
        self.constants = constants
        self.munch1 = self.pygame.mixer.Sound('sound/munch_1.wav')
        self.munch2 = self.pygame.mixer.Sound('sound/munch_2.wav')

    def play_start_music(self):
        self.pygame.mixer.music.set_endevent(self.constants.get_event_song_ended())
        self.pygame.mixer.music.load("sound/game_start.wav")
        self.pygame.mixer.music.play(0)

    def play_siren_loop_music(self):
        self.pygame.mixer.music.load("sound/siren_1.wav")
        self.pygame.mixer.music.play(-1)

    def play_munch(self):
        channel = self.pygame.mixer.Channel(0)
        # channel.queue(self.munch1)
        channel.queue(self.munch2)
        channel.play(self.munch1)
        while channel.get_busy():
            continue

    def paint(self, screen):
        pass

    def calc_rules(self):
        pass

    def process_events(self, events):
        for e in events:
            if e.type == self.constants.get_event_song_ended():
                print("the song ended!")
                self.play_siren_loop_music()
