import random

class DistanceSensor:
    def __init__(self):
        self._initialize_hardware()

    def _initialize_hardware(self):
        """Simulates sensor initialization."""
        print("DistanceSensor: Initialized.")

    def get_distance(self) -> float:
        """
        Returns the current distance reading.
        In the future, replace the random value with actual GPIO/I2C logic.
        """
        # Simulated distance between 0 and 50cm
        distance = float(random.randint(0, 50))
        return distance