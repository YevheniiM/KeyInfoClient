"""The module contains the logic of analyzing the
keyboard events."""

import sys

from keyboard import KEY_DOWN, KeyboardEvent


class KeyboardEventAnalyzer:
    """The class do the main logic of a program"""

    MAX_BUFFER_LENGTH = 10000

    def __init__(self):
        self.events = []

    def analyze(self, event: KeyboardEvent):
        """Analyzes the event and flushes the buffer if needed."""

        if not self.__check_max_buffer():
            self.__flush_buffer()
        self._print_event(event)
        self.events.append(event)

    @staticmethod
    def _print_event(event: KeyboardEvent):
        """Prints the key when it is pressed (only on KEY_DOWN action)."""

        if event.event_type == KEY_DOWN:
            sys.stdout.write(f"> the [{event.name}] key was pressed ({event.event_type})\n")

    def __check_max_buffer(self):
        """Checks the buffer length."""
        return len(self.events) < KeyboardEventAnalyzer.MAX_BUFFER_LENGTH

    def __flush_buffer(self):
        # TODO: properly flush the buffer
        pass
