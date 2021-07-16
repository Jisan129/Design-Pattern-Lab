import Decorator


class Italic(Decorator.TextDecorator):

    def decorate_text(self) -> str:
        return super(Italic, self).decorate_text().capitalize()
