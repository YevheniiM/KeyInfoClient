"""The module contains the logic of analyzing the
keyboard events."""

import sys

from keyboard import KEY_DOWN, KeyboardEvent

from common.saver import KeySaver


class KeyboardEventAnalyzer:
    """The class do the main logic of a program"""

    MAX_BUFFER_LENGTH = 10

    def __init__(self):
        self.events = []
        self.current_event = None

    def analyze(self, event: KeyboardEvent):
        """Analyzes the event and flushes the buffer if needed."""

        if not self.__check_max_buffer():
            self.__flush_buffer()
        self._print_event(event)
        self._register_event(event)

    def abort(self):
        # TODO: find the way to wrap under the context manager
        self.__flush_buffer()

    def _register_event(self, event):
        """Registers only KEY_DOWN events, ignoring KEY_UP"""
        if event.event_type == KEY_DOWN:
            self.events.append({
                "char": event.name,
                "scan_code": event.scan_code,
                "time": event.time,
                "time_after_previous": event.time - self.events[-1]["time"] if len(self.events) else 0,
            })

    @staticmethod
    def _print_event(event: KeyboardEvent):
        """Prints the key when it is pressed (only on KEY_DOWN action)."""

        if event.event_type == KEY_DOWN:
            sys.stdout.write(f"> the [{event.name}] key was pressed ({event.event_type})\n")

    def __check_max_buffer(self):
        """Checks the buffer length."""
        return len(self.events) < KeyboardEventAnalyzer.MAX_BUFFER_LENGTH

    def __flush_buffer(self):
        KeySaver().save_multiple(self.events)
        self.events = []
