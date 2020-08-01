from abc import ABCMeta, abstractmethod


class GameElement(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, screen):
        pass

    @abstractmethod
    def calc_rules(self):
        pass

    @abstractmethod
    def process_events(self, events):
        pass
