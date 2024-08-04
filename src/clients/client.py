from abc import ABC, abstractmethod
import json
import os

LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)


class Client(ABC):
    @abstractmethod
    def process_messages(self, messages):
        pass

    @abstractmethod
    def get_completion(self, messages, stream=False):
        pass

    def log(self, messages):
        with open(
            os.path.join(LOG_FOLDER, f"{self.__class__.__name__}.json"), "w"
        ) as file:
            json.dump(messages, file, indent=2)
