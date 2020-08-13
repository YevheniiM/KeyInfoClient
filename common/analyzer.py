import sys

from keyboard import KEY_DOWN, KeyboardEvent


class KeyboardEventAnalyzer:
    MAX_BUFFER_LENGTH = 10000

    def __init__(self):
        self.events = []

    def analyze(self, event: KeyboardEvent):
        if not self.__check_max_buffer():
            self.__flush_buffer()
        self._print_event(event)
        self.events.append(event)

    @staticmethod
    def _print_event(event: KeyboardEvent):
        if event.event_type == KEY_DOWN:
            sys.stdout.write(f"The [{event.name}] key was pressed ({event.event_type})")

    def __check_max_buffer(self):
        return len(self.events) < KeyboardEventAnalyzer.MAX_BUFFER_LENGTH

    def __flush_buffer(self):
        # TODO: properly flush the buffer
        pass
