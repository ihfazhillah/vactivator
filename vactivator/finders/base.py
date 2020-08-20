from abc import ABCMeta, abstractmethod
from pathlib import Path


class BaseFinder(metaclass=ABCMeta):
    def __init__(self, path: str):
        self.path = Path(path)

    @abstractmethod
    def test(self):
        pass

    @abstractmethod
    def get_venv_activator(self):
        pass