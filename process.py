class Process:
    def __init__(self, pid):
        self.pid = pid
        self.clock = 0

    def send_message(self, receiver):
        self.clock += 1
        receiver.receive_message(self.clock)
        print(f"Process {self.pid} sends message to Process {receiver.pid} with clock {self.clock}")

    def receive_message(self, sender_clock):
        self.clock = max(self.clock, sender_clock) + 1
        print(f"Process {self.pid} receives message with clock {sender_clock}. Updated clock: {self.clock}")

    def __str__(self):
        return f"Process {self.pid} Clock: {self.clock}"

def simulate_process_communication():
    # Create processes
    p1 = Process(1)
    p2 = Process(2)
    p3 = Process(3)

    # Simulate message exchanges
    p1.send_message(p2)
    p2.send_message(p3)
    p3.send_message(p1)
    p2.send_message(p1)
    p3.send_message(p2)

    # Print final logical clocks
    print(p1)
    print(p2)
    print(p3)

if __name__ == "__main__":
    simulate_process_communication()
