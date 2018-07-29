from abc import ABCMeta, abstractmethod

class Screener(metaclass=ABCMeta):

    @abstractmethod
    def screen(self, **kwargs):
        return