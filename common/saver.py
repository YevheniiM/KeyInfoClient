import datetime
import json
import os
from typing import List

from settings.settings import TEMPORARY_FOLDER_FOR_KEYS


class KeySaver:
    def __init__(self):
        self.filename = f'{datetime.datetime.now().strftime("%Y-%b-%d-%A-%I-%M-%S")}-export.json'

    def save_multiple(self, events: List[dict]) -> None:
        """Saves the list with registered events into the .json file"""
        with open(os.path.join(TEMPORARY_FOLDER_FOR_KEYS, self.filename), mode="w") as f:
            json.dump(events, f)
