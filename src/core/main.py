import time
from src.plugins.motor_controller import MotorController
from src.plugins.sensor_plugin import DistanceSensor
from src.plugins.logger_plugin import RobotLogger
from src.plugins.state_manager import StateManager

def run_patrol_loop():
    motor = MotorController(pin=17)
    sensor = DistanceSensor()
    logger = RobotLogger()
    states = StateManager()
    
    logger.log("System Initialized.")
    
    try:
        while True:
            distance = sensor.get_distance()
            
            # Logic: Assign state based on distance
            if distance < 10:
                states.set_state("AVOIDING")
                motor.move("OFF")
            else:
                states.set_state("PATROL")
                motor.move("ON")
            
            logger.log(f"Current State: {states.get_state()} | Dist: {distance}cm")
            time.sleep(1)
            
    except KeyboardInterrupt:
        logger.log("System Halted.")

if __name__ == "__main__":
    run_patrol_loop()