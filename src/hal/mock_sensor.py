from .sensor_interface import SensorInterface
import random

class MockDistanceSensor(SensorInterface):
    def get_distance(self) -> float:
        # Simulate sensor readings between 0 and 50cm
        return float(random.randint(0, 50))