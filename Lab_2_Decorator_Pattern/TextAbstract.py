from abc import ABC, abstractmethod


class TextAbstract(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def decorate_text(self):
        pass
