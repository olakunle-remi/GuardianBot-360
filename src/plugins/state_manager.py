# In src/core/state_manager.py

class StateManager:
    def __init__(self, sensor, motor, logger):
        self.sensor = sensor
        self.motor = motor
        self.logger = logger
        self.state = "IDLE"

    def update(self):
        # Example of how you will use them in the future:
        distance = self.sensor.get_distance()
        self.logger.log(f"Current distance: {distance}")
        
        if distance < 10:
            self.motor.move("OFF")
        else:
            self.motor.move("ON")