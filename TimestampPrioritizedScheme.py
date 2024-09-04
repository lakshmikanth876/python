import threading
import time
from queue import PriorityQueue

class TimestampPrioritizedScheme:
    def __init__(self, process_id, num_processes):
        self.process_id = process_id
        self.num_processes = num_processes
        self.timestamp = 0
        self.request_queue = PriorityQueue()
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.requests = [None] * num_processes

    def send_request(self):
        with self.lock:
            self.timestamp += 1
            self.request_queue.put((self.timestamp, self.process_id))
            for i in range(self.num_processes):
                if i != self.process_id:
                    self.send_message(i, 'request', self.timestamp, self.process_id)

    def send_message(self, target, message_type, timestamp, process_id):
        # Simulate sending message to target process
        print(f'Process {self.process_id} sending {message_type} to {target} with timestamp {timestamp}')

    def receive_message(self, message_type, timestamp, process_id):
        with self.lock:
            if message_type == 'request':
                self.requests[process_id] = (timestamp, process_id)
                self.send_message(process_id, 'reply', self.timestamp, self.process_id)
            elif message_type == 'reply':
                pass

    def enter_critical_section(self):
        with self.condition:
            while not self.is_allowed_to_enter():
                self.condition.wait()
            print(f'Process {self.process_id} entering critical section at timestamp {self.timestamp}')

    def is_allowed_to_enter(self):
        with self.lock:
            if self.request_queue.empty():
                return False
            next_timestamp, next_process_id = self.request_queue.queue[0]
            return next_process_id == self.process_id

    def run(self):
        while True:
            self.send_request()
            self.enter_critical_section()
            time.sleep(2)
            with self.lock:
                self.request_queue.get()
            print(f'Process {self.process_id} leaving critical section at timestamp {self.timestamp}')
            time.sleep(2)

# Example usage
num_processes = 3
processes = [TimestampPrioritizedScheme(i, num_processes) for i in range(num_processes)]

threads = []
for process in processes:
    t = threading.Thread(target=process.run)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
