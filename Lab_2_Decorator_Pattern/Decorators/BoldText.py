import Decorators.Decorator


class BoldText(Decorators.Decorator.TextDecorator):

    def decorate_text(self) -> str:
        temp = super(BoldText, self).decorate_text()
        return '\033[1m'+temp+'\033[0m'
