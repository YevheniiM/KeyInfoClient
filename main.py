import sys

import keyboard

from common.analyzer import KeyboardEventAnalyzer

analyzer = KeyboardEventAnalyzer()


def analyze(event):
    analyzer.analyze(event)
    sys.stdout.flush()


def main():
    keyboard.hook(analyze)
    keyboard.wait()


if __name__ == '__main__':
    main()
