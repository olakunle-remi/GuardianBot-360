import datetime

class RobotLogger:
    def __init__(self, filename="robot_log.txt"):
        self.filename = filename

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        with open(self.filename, "a") as f:
            f.write(log_entry + "\n")
        print(f"Log: {message}")