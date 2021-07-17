# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Components import PlainText
from Decorators.BoldText import BoldText
from Decorators.Italic import Italic
from Decorators.StrikeOut import StrikeOut


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    a = PlainText.ConcreteText('JISAN')
    print(a.decorate_text())
    b = Italic(a)
    print(b.decorate_text())
    c = BoldText(b)
    print(c.decorate_text())
    d = StrikeOut(c)
    print(d.decorate_text())
# print(''.join(chain.from_iterable(zip('abir', repeat('\u0336')))))
