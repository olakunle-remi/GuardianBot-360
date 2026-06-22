import time
import sys
import os

# 1. Path Setup: Ensure the project root is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# 2. Imports: Clean, organized, and no duplicates
from src.hal.motor_controller import MotorController
from src.hal.mock_sensor import MockDistanceSensor
from src.plugins.logger_plugin import RobotLogger
from src.plugins.state_manager import StateManager

# 3. Execution
def run_patrol_loop():
    # ... rest of your code ...
    # Use the specific Mock class
    motor = MotorController(pin=17)
    sensor = MockDistanceSensor() 
    logger = RobotLogger()
    
    bot_brain = StateManager(sensor=sensor, motor=motor, logger=logger)
    
    logger.log("System Initialized.")
    
    try:
        while True:
            bot_brain.update()
            time.sleep(1)
    except KeyboardInterrupt:
        logger.log("System Halted.")

if __name__ == "__main__":
    run_patrol_loop()