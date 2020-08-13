import sys

import keyboard
from keyboard import KeyboardEvent

from common.analyzer import KeyboardEventAnalyzer

analyzer = KeyboardEventAnalyzer()


def analyze(event: KeyboardEvent):
    """The function calls each time the key is pressed and
    make some analysis."""

    analyzer.analyze(event)
    sys.stdout.flush()


def main():
    """The entry point of a program"""

    keyboard.hook(analyze)
    keyboard.wait()


if __name__ == '__main__':
    main()
