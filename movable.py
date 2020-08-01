from abc import ABCMeta, abstractmethod


class Movable(metaclass=ABCMeta):
    @abstractmethod
    def accept_movement(self):
        pass

    @abstractmethod
    def deny_movement(self, directions):
        pass

    @abstractmethod
    def corner(self, directions):
        pass
