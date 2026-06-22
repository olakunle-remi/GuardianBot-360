import platform

# --- Hardware Abstraction Layer ---
# This layer ensures your code runs on both Windows (for testing) 
# and Raspberry Pi (for hardware control).
if platform.system() == "Windows":
    class MockGPIO:
        BCM = 1
        OUT = 1
        HIGH = 1
        LOW = 0
        def setmode(self, mode): print("Mock: Mode set to BCM")
        def setup(self, pin, mode): print(f"Mock: Pin {pin} setup as output")
        def output(self, pin, value): print(f"Mock: Pin {pin} set to {value}")
    GPIO = MockGPIO()
else:
    import RPi.GPIO as GPIO

# --- Plugin: Motor Controller ---
class MotorController:
    """Controls a motor attached to a specific GPIO pin."""
    
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        print(f"MotorController: Initialized on pin {self.pin}")

    def move(self, state):
        """Moves the motor to 'ON' or 'OFF' state."""
        value = GPIO.HIGH if state == "ON" else GPIO.LOW
        GPIO.output(self.pin, value)