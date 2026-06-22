class MotorController:
    def __init__(self, pin: int):
        self.pin = pin
        self.state = "OFF"
        self._initialize_hardware()

    def _initialize_hardware(self):
        """Simulates initializing the GPIO pins."""
        # In a real scenario, you would use RPi.GPIO here:
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.pin, GPIO.OUT)
        print(f"Mock: Pin {self.pin} setup as output")
        print(f"MotorController: Initialized on pin {self.pin}")

    def move(self, action: str):
        """
        Controls the motor state.
        :param action: "ON" or "OFF"
        """
        if action == "ON":
            self.state = "ON"
            self._set_pin(1)
        else:
            self.state = "OFF"
            self._set_pin(0)

    def _set_pin(self, value: int):
        """Low-level method to set the physical pin state."""
        # Real hardware: GPIO.output(self.pin, value)
        print(f"Mock: Pin {self.pin} set to {value}")

    def get_status(self):
        return self.state