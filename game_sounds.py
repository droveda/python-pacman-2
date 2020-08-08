from game_element import GameElement
from game_state import GameState


class GameSounds(GameElement):

    def __init__(self, pygame, constants, game_state):
        self.pygame = pygame
        self.constants = constants
        self.munch1 = self.pygame.mixer.Sound('sound/munch_1.wav')
        self.munch2 = self.pygame.mixer.Sound('sound/munch_2.wav')
        self.death1 = self.pygame.mixer.Sound('sound/death_1.wav')
        self.scenario = None
        self.enable_sound = True
        self.state = game_state

    def set_scenario(self, scenario):
        self.scenario = scenario

    def play_start_music(self):
        if self.enable_sound:
            self.pygame.mixer.music.set_endevent(self.constants.get_event_song_ended())
            self.pygame.mixer.music.load("sound/game_start.wav")
            self.pygame.mixer.music.play(0)

    def play_siren_loop_music(self):
        if self.enable_sound:
            self.pygame.mixer.music.load("sound/siren_1.wav")
            self.pygame.mixer.music.play(-1)

    def stop_siren(self):
        self.pygame.mixer.music.stop()

    def play_munch(self):
        if self.enable_sound:
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
                self.scenario.state.set_current_state(GameState.RUNNING)
                self.play_siren_loop_music()

    def pause_music(self):
        self.pygame.mixer.music.pause()

    def resume_music(self):
        self.pygame.mixer.music.unpause()
