from abc import ABC, abstractmethod


class Storage(ABC):
    """
    General interface for storage.
    """
    @abstractmethod
    def __init__(self, items: dict, capacity: int):
        self.items = items
        self.capacity = capacity

    @abstractmethod
    def add(self, name, cnt):
        """Adding an item to storage"""

    @abstractmethod
    def remove(self, name, cnt):
        """Removing an item from storage"""

    @abstractmethod
    def get_free_space(self):
        """Checking free storage space"""

    @abstractmethod
    def get_items(self):
        """Getting a list of goods in storage"""

    @abstractmethod
    def get_unique_items_count(self):
        """Getting the number of unique types of goods in storage"""
