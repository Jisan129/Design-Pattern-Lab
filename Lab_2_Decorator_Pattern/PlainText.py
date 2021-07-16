import TextAbstract


class ConcreteText(TextAbstract.TextAbstract):
    userText = ''

    def __init__(self, userText) :
        self.userText = userText

    def decorate_text(self):
        return self.userText
