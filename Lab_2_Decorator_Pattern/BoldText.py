import Decorator
from simple_colors import *


class BoldText(Decorator.TextDecorator):

    def decorate_text(self) -> str:
        temp = super(BoldText, self).decorate_text()
        return '\033[1m'+temp+'\033[0m'
