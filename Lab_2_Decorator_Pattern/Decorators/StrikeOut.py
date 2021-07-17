import Decorators.Decorator


class StrikeOut(Decorators.Decorator.TextDecorator):
    def decorate_text(self) -> str:
        temp = super(StrikeOut, self).decorate_text()
        return '\033[9m'+temp+'\033[0m'
