### GuardianBot-360: Project Documentation

#### Phase 2: Sensory Integration & Logic (Day 2)

**Date:** June 22, 2026
**Status:** Completed
**Objective:** Transition from static automation to autonomous decision-making by integrating environmental sensing into the control loop.

---

### 1. Code Analysis

#### **`src/plugins/motor_controller.py`**

* **Purpose:** Acts as the "Muscle" driver. It abstracts the physical hardware (or simulation) from the core logic.
* **Key Mechanism:** It uses a **Hardware Abstraction Layer (HAL)** to check the operating system.
* **`__init__(self, pin)`:** Configures the GPIO pin as an `OUT` device, setting the initial state.
* **`move(self, state)`:** Converts human-readable commands ("ON"/"OFF") into machine-level signals (`HIGH`/`LOW`), isolating the core logic from specific electrical implementation details.



#### **`src/plugins/sensor_plugin.py`**

* **Purpose:** Acts as the "Sense" interface. It provides real-time data from the robot's environment.
* **Key Mechanism:** * **`get_distance(self)`:** In this mock implementation, it utilizes the `random` library to emulate an Ultrasonic Sensor (like an HC-SR04). This returns an integer representing centimeters, providing the "Think" logic in `main.py` with the raw data required for safety calculations.

---

### 2. Functional Roles in Robotic Engineering

In robotics, sensors and motors form the primary feedback loop of any autonomous machine.

| Component | Engineering Function | Analogy |
| --- | --- | --- |
| **Motor (Actuator)** | Converts electrical energy into physical motion. It is the primary means for a robot to exert force on its environment. | **The Muscles** |
| **Sensor (Input)** | Converts physical phenomena (distance, light, pressure) into data signals. It allows the robot to perceive environmental changes. | **The Senses** |

#### **The Sense-Think-Act Cycle**

Your code demonstrates the fundamental closed-loop control system used in almost all professional robotics:

1. **Sense (Input):** The `DistanceSensor` polls the environment for state data.
2. **Think (Processing):** The `main.py` logic processes the data (`if distance < 10`). This determines the **Control Law**—the rule by which the robot behaves.
3. **Act (Output):** The `MotorController` executes the command based on the processed data, modifying the robot's state in the physical world.

---

### 3. Summary of Day 2 Achievements

* **Decoupled Input/Output:** Your architecture now cleanly separates input (`sensor_plugin`) from output (`motor_controller`).
* **Autonomous Safety:** The robot now autonomously manages safety thresholds, preventing collisions without human intervention.
* **Scalable Logic:** Because of the modular approach, replacing the `MockGPIO` or the random `DistanceSensor` with actual physical drivers will require zero changes to your core patrol logic.

