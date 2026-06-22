class StateManager:
    def __init__(self):
        self.state = "IDLE"

    def set_state(self, new_state):
        if self.state != new_state:
            print(f"State Change: {self.state} -> {new_state}")
            self.state = new_state
            
    def get_state(self):
        return self.state