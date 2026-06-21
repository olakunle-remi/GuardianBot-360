### GuardianBot-360: Project Documentation

#### Phase 1: Foundation (Day 1)

**Date:** June 21, 2026
**Status:** Completed
**Objective:** Establish a modular, scalable software architecture and verify hardware-software communication using a Hardware Abstraction Layer (HAL).

---

### 1. Architectural Overview

To ensure the project remains maintainable as it grows, we implemented a **Decoupled Architecture**. This separates the "Brain" (Core logic) from the "Limbs" (Hardware drivers).

* **Core (`src/core/`):** Contains the main execution logic. It is unaware of the physical hardware details, communicating only through defined class methods.
* **Plugins (`src/plugins/`):** Contains independent hardware drivers. This allows us to swap hardware or add new components (sensors, cameras) without modifying the core logic.
* **HAL (Hardware Abstraction Layer):** A conditional logic block within the plugins that detects the host environment (Windows vs. Raspberry Pi). This allows for local development and testing on non-robot hardware.

---

### 2. Implementation Details

#### **File Structure**

The project utilizes Python packages, necessitating `__init__.py` files in each directory to ensure proper module resolution.

```text
GuardianBot-360/
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── main.py       # The Brain: Manages high-level behavior
│   └── plugins/
│       ├── __init__.py
│       └── motor_controller.py # The Driver: Manages GPIO hardware

```

#### **Key Components**

* **`MotorController` Class:** Encapsulates motor initialization and movement commands. By using a class, we can instantiate multiple motors independently.
* **`MockGPIO`:** A simulation class used on Windows systems. It mimics the behavior of the Raspberry Pi `RPi.GPIO` library, allowing for syntax and logic testing without physical hardware.

---

### 3. Verification of Results

Day 1 concluded with a successful test execution from the project root:
`python -m src.core.main`

**Expected Console Output:**

* `MotorController: Initialized on pin 17`
* `Patrol Mode Active. Press Ctrl+C to stop.`
* `Mock: Pin 17 set to 1` (Motor ON)
* `Mock: Pin 17 set to 0` (Motor OFF)

---

### 4. Next Steps (Day 2)

With the motor control and modular architecture successfully established, Phase 2 will focus on:

1. **Sensor Integration:** Implementing an input plugin (e.g., Distance Sensor) to allow the robot to perceive the environment.
2. **Logic Expansion:** Updating `main.py` to utilize sensor data for conditional navigation (e.g., "If an obstacle is detected, stop or turn").

---

**Documentation Status:** The foundational framework is 
stable and ready for expansion. 
Does this documentation capture the essence of your 
Day 1 progress, or would you like to add specific technical notes 
regarding the GPIO mapping?








Error Day1 
To get your project back on track, let's address these two issues as the final tasks for Day 1.

### **Error 1: Installation (Missing Libraries)**

Since you are likely trying to run this on Windows, you don't actually need to install `RPi.GPIO` (which only works on a Raspberry Pi). If you try to run `pip install RPi.GPIO` on Windows, it will fail.

**The Fix:**
Ensure your `motor_controller.py` has the **Hardware Abstraction Layer (HAL)** we wrote earlier. This allows your code to run on Windows **without** needing that library. If you get a "Module Not Found" error, it means you have an `import RPi.GPIO` at the top of your file that is running *outside* of an `if` statement.

**Check your code:**

```python
# THIS IS WRONG (Will cause install error on Windows):
import RPi.GPIO as GPIO 

# THIS IS CORRECT:
import platform
if platform.system() == "Windows":
    # Define Mock class...
else:
    import RPi.GPIO as GPIO

```

---

### **Error 2: `MotorController` Class Missing**

As we discovered, the `ImportError` happens because `main.py` is looking for a blueprint (`class`) that isn't defined inside `motor_controller.py`.

**The Fix:**
Ensure the class is defined **exactly** like this in `src/plugins/motor_controller.py`:

```python
class MotorController:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        print(f"MotorController: Initialized on pin {self.pin}")

    def move(self, state):
        value = GPIO.HIGH if state == "ON" else GPIO.LOW
        GPIO.output(self.pin, value)

```

---

### **Troubleshooting Checklist**

1. **Delete the Cache:** If you've fixed the code but still see errors, run this in your terminal to clear old "memory":
`find . -name "__pycache__" -type d -exec rm -rf {} +`
2. **Run from Root:** Always ensure you are in the `GuardianBot-360` folder and run:
`python src/core/main.py`
3. **No `pip` needed:** Because we used the `MockGPIO` approach, you do **not** need to install any external robotics libraries on your Windows machine.

**If you make these two changes, the "Installation" error (trying to find `RPi.GPIO`) and the "Class" error will both disappear.**

**Does the error message change when you run it after these adjustments? (If so, please paste the new error!)**




sugested correction and execution 
=================================

To resolve these two specific errors (Installation/Module Import and the Missing Class), please follow these exact steps. This is the "Gold Standard" correction for your project.

### 1. Correction for `src/plugins/motor_controller.py`

Replace the **entire content** of this file. The error happens because the code is either trying to install a library it doesn't need or is missing the `class` structure.

```python
import platform

# --- Hardware Abstraction Layer ---
# This block prevents "ModuleNotFoundError" for RPi.GPIO on Windows
if platform.system() == "Windows":
    class MockGPIO:
        BCM = 1; OUT = 1; HIGH = 1; LOW = 0
        def setmode(self, mode): pass
        def setup(self, pin, mode): pass
        def output(self, pin, value): print(f"Mock: Pin {pin} set to {value}")
    GPIO = MockGPIO()
else:
    import RPi.GPIO as GPIO

# --- Plugin Class ---
# This resolves your "Class MotorController not found" error
class MotorController:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        print(f"MotorController: Initialized on pin {self.pin}")

    def move(self, state):
        value = GPIO.HIGH if state == "ON" else GPIO.LOW
        GPIO.output(self.pin, value)

```

### 2. Correction for `src/core/main.py`

Ensure this file imports the class correctly from the now-fixed plugin file.

```python
import time
from src.plugins.motor_controller import MotorController

def run_patrol_loop():
    # Instantiate the class
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

```

### 3. Execution Procedure

Do not use `pip` to install Raspberry Pi libraries on Windows. Instead, run the code using the following clean execution steps:

1. **Clear the cache** (removes the "ghost" errors where Python remembers the old broken code):
* In your terminal, navigate to `~/Desktop/Robotic/GuardianBot-360`.
* Run: `rm -rf src/*/__pycache__` (or `del /s *.pyc` on Windows CMD).


2. **Execute the module** from the project root:
```bash
python -m src.core.main

```



**Why this works:**

* **Installation Error:**
 By using the `if platform.system() == "Windows"` check, 
 the code never attempts to load `RPi.GPIO` on your PC,
 meaning you don't need to install anything.
* **Class Error:** By explicitly declaring `class MotorController:` 
in the plugin file, you provide the exact "object" that `main.py` is looking for.
