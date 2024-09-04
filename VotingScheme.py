# Voting Schemes
import threading
import random
import time

class VotingScheme:
    def __init__(self, process_id, num_processes, voters):
        self.process_id = process_id
        self.num_processes = num_processes
        self.voters = voters
        self.votes = 0
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.voted = [False] * num_processes

    def send_request(self):
        with self.lock:
            self.votes = 0
            for voter in self.voters:
                if voter != self.process_id:
                    self.send_message(voter, 'request')

    def send_message(self, target, message_type):
        # Simulate sending message to target process
        print(f'Process {self.process_id} sending {message_type} to {target}')

    def receive_message(self, message_type, process_id):
        with self.lock:
            if message_type == 'request' and not self.voted[process_id]:
                self.voted[process_id] = True
                self.send_message(process_id, 'vote')
            elif message_type == 'vote':
                self.votes += 1
                if self.votes > len(self.voters) // 2:
                    self.condition.notify_all()

    def enter_critical_section(self):
        with self.condition:
            while self.votes <= len(self.voters) // 2:
                self.condition.wait()
            print(f'Process {self.process_id} entering critical section')

    def run(self):
        while True:
            self.send_request()
            self.enter_critical_section()
            time.sleep(2)
            print(f'Process {self.process_id} leaving critical section')
            time.sleep(2)
            with self.lock:
                self.voted = [False] * self.num_processes

# Example usage
num_processes = 3
voters = [[0, 1], [0, 2], [1, 2]]  # Example voter sets for each process
processes = [VotingScheme(i, num_processes, voters[i]) for i in range(num_processes)]

threads = []
for process in processes:
    t = threading.Thread(target=process.run)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
