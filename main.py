import random
import time
import statistics
import matplotlib.pyplot as plt

class Simulation:
    def __init__(self, num_stations, arrival_rate, service_rate, policy, sim_duration):
        self.num_stations = num_stations
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.policy = policy
        self.sim_duration = sim_duration
        
        self.queues = [[] for _ in range(num_stations)]
        self.waiting_times = [[] for _ in range(num_stations)]
        self.occupancy_times = [0] * num_stations
        self.total_passengers = 0
        self.current_time = 0
        self.next_arrival_time = random.expovariate(1.0 / self.arrival_rate)
        self.service_end_times = [0] * num_stations
        self.round_robin_counter = 0
        
    def run(self):
        while self.current_time < self.sim_duration:
            self.current_time += 1
            if self.current_time >= self.next_arrival_time:
                self.total_passengers += 1
                if self.policy == 'single_queue':
                    self.assign_single_queue()
                elif self.policy == 'round_robin':
                    self.assign_round_robin()
                elif self.policy == 'shortest_queue':
                    self.assign_shortest_queue()
                elif self.policy == 'random_queue':
                    self.assign_random_queue()
                self.next_arrival_time += random.expovariate(1.0 / self.arrival_rate)
            
            for i in range(self.num_stations):
                if self.current_time >= self.service_end_times[i] and self.queues[i]:
                    arrival_time = self.queues[i].pop(0)
                    waiting_time = self.current_time - arrival_time
                    self.waiting_times[i].append(waiting_time)
                    service_time = random.expovariate(1.0 / self.service_rate)
                    self.occupancy_times[i] += service_time
                    self.service_end_times[i] = self.current_time + service_time
        
    def assign_single_queue(self):
        self.queues[0].append(self.current_time)
    
    def assign_round_robin(self):
        station = self.round_robin_counter % self.num_stations
        self.queues[station].append(self.current_time)
        self.round_robin_counter += 1
    
    def assign_shortest_queue(self):
        station = min(range(self.num_stations), key=lambda x: len(self.queues[x]))
        self.queues[station].append(self.current_time)
    
    def assign_random_queue(self):
        station = random.randint(0, self.num_stations - 1)
        self.queues[station].append(self.current_time)
        
def run_simulation(policy, num_stations=5, arrival_rate=1, service_rate=5, sim_duration=1000):
    sim = Simulation(num_stations, arrival_rate, service_rate, policy, sim_duration)
    sim.run()
    return sim

# Example usage
sim_duration = 10000
arrival_rate = 1
service_rate = 6

# Option 1: Single Queue
sim_single_queue = run_simulation('single_queue', sim_duration=sim_duration, arrival_rate=arrival_rate, service_rate=service_rate)

# Option 2.A: Round Robin
sim_round_robin = run_simulation('round_robin', sim_duration=sim_duration, arrival_rate=arrival_rate, service_rate=service_rate)

# Option 2.B: Shortest Queue
sim_shortest_queue = run_simulation('shortest_queue', sim_duration=sim_duration, arrival_rate=arrival_rate, service_rate=service_rate)

# Option 2.C: Random Queue
sim_random_queue = run_simulation('random_queue', sim_duration=sim_duration, arrival_rate=arrival_rate, service_rate=service_rate)

# Function to calculate and print results
def print_results(sim, policy_name):
    print(f"Results for {policy_name} Policy")
    print(f"Total passengers: {sim.total_passengers}")
    for i in range(sim.num_stations):
        avg_waiting_time = statistics.mean(sim.waiting_times[i]) if sim.waiting_times[i] else 0
        max_waiting_time = max(sim.waiting_times[i]) if sim.waiting_times[i] else 0
        max_queue_length = max(len(queue) for queue in sim.queues) if sim.queues else 0
        occupancy_rate = sim.occupancy_times[i] / sim.sim_duration * 100
        
        print(f"Station {i+1}:")
        print(f"  Average waiting time: {avg_waiting_time:.2f}")
        print(f"  Maximum waiting time: {max_waiting_time:.2f}")
        print(f"  Maximum queue length: {max_queue_length}")
        print(f"  Occupancy rate: {occupancy_rate:.2f}%")

# Print results for each policy
print_results(sim_single_queue, "Single Queue")
print_results(sim_round_robin, "Round Robin")
print_results(sim_shortest_queue, "Shortest Queue")
print_results(sim_random_queue, "Random Queue")
