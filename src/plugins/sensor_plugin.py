import random

class DistanceSensor:
    def __init__(self):
        print("DistanceSensor: Initialized.")

    def get_distance(self):
        """Simulates reading a distance in centimeters."""
        # Returns a random distance between 2cm and 50cm
        return random.randint(2, 50)