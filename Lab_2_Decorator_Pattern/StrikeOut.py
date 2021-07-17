import Decorator
from simple_colors import *


class StrikeOut(Decorator.TextDecorator):
    def decorate_text(self) -> str:
        temp = super(StrikeOut, self).decorate_text()
        return '\033[9m'+temp+'\033[0m'
