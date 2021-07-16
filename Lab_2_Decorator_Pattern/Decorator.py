import TextAbstract


class TextDecorator(TextAbstract.TextAbstract):
    _component: TextAbstract.TextAbstract = None

    def __init__(self, _component: TextAbstract.TextAbstract):
        self._component = _component

    def decorate_text(self) -> str:
        return self._component.decorate_text()
