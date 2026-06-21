# src/core/main.py
import time
from src.plugins.motor_controller import MotorController
from src.plugins.sensor_plugin import DistanceSensor
from src.plugins.logger_plugin import RobotLogger

def run_patrol_loop():
    """
    Main logic: Coordinates hardware modules and logs autonomous decisions.
    """
    # Initialize modules
    motor = MotorController(pin=17)
    sensor = DistanceSensor()
    logger = RobotLogger()
    
    logger.log("System Started. Patrol Initiated.")
    
    try:
        while True:
            # 1. SENSE
            distance = sensor.get_distance()
            
            # 2. THINK & 3. ACT
            if distance < 10:
                msg = f"Obstacle at {distance}cm. Stopping motor."
                motor.move("OFF")
            else:
                msg = f"Path clear ({distance}cm). Moving forward."
                motor.move("ON")
            
            # Log the decision and wait
            logger.log(msg)
            time.sleep(1)
            
    except KeyboardInterrupt:
        logger.log("System Halted by user.")
    except Exception as e:
        logger.log(f"System Error: {e}")

if __name__ == "__main__":
    run_patrol_loop()