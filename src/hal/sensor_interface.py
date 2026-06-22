from abc import ABC, abstractmethod

class SensorInterface(ABC):
    @abstractmethod
    def get_distance(self) -> float:
        """Must return the distance as a float."""
        pass