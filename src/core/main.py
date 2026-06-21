import time
from src.plugins.motor_controller import MotorController

def run_patrol_loop():
    left_motor = MotorController(pin=17)
    
    print("Patrol Mode Active. Press Ctrl+C to stop.")
    try:
        while True:
            left_motor.move("ON")
            time.sleep(1)
            left_motor.move("OFF")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSystem Halted.")

if __name__ == "__main__":
    run_patrol_loop()