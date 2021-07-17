import Decorators.Decorator


class Italic(Decorators.Decorator.TextDecorator):

    def decorate_text(self) -> str:
        temp = super(Italic, self).decorate_text()
        return '\033[3m'+temp+'\033[0m'
