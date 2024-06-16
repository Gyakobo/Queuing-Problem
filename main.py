# DISCLAIMOR: Please run this program with python3.10 (or above). Any version lower will not work

# Import mean function from stats library, and expovariate and randint functions from random library 
from statistics import mean
from random import expovariate, randint 

# Once again it is important to run this program with Python3.10 (or above)
import sys
assert sys.version_info >= (3, 10)

# We are going to stick all simulation types(single queue, round robin, shortest queue, random queue) all into one class
class Custom_simulation:
    def __init__(self, number_of_stations, arrival_rate, service_rate, type_of_option, simulation_duration):
        self.number_of_stations = number_of_stations
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.type_of_option = type_of_option
        self.simulation_duration = simulation_duration

        self.queues             = []
        self.waiting_times      = []
        self.occupancy_times    = []
        self.service_end_times  = []

        for _ in range(number_of_stations): 
            self.queues.append([])
            self.waiting_times.append([])
            self.occupancy_times.append(0)
            self.service_end_times.append(0)

        self.total_passengers = 0
        self.current_time = 0
        self.next_arrival_time = expovariate(1.0 / self.arrival_rate)
        self.round_robin = 0
        
    def run(self):
        while self.current_time < self.simulation_duration:
            self.current_time += 1
            if self.current_time >= self.next_arrival_time:
                self.total_passengers += 1

                match self.type_of_option:
                    case "single_queue":
                        self.assign_single_queue()
                    case "round_robin":
                        self.assign_round_robin()
                    case "shortest_queue":
                        self.assign_shortest_queue()
                    case "random_queue":
                        self.assign_random_queue()
                
                '''
                if self.type_of_option == 'single_queue':
                    self.assign_single_queue()
                elif self.type_of_option == 'round_robin':
                    self.assign_round_robin()
                elif self.type_of_option == 'shortest_queue':
                    self.assign_shortest_queue()
                elif self.type_of_option == 'random_queue':
                    self.assign_random_queue()
                '''
                self.next_arrival_time += expovariate(1.0 / self.arrival_rate)
            
            for i in range(self.number_of_stations):
                if self.current_time >= self.service_end_times[i] and self.queues[i]:
                    arrival_time = self.queues[i].pop(0)
                    waiting_time = self.current_time - arrival_time
                    self.waiting_times[i].append(waiting_time)
                    service_time = expovariate(1.0 / self.service_rate)
                    self.occupancy_times[i] += service_time
                    self.service_end_times[i] = self.current_time + service_time
        
    def assign_single_queue(self):
        self.queues[0].append(self.current_time)
    
    def assign_round_robin(self):
        station = self.round_robin % self.number_of_stations
        self.queues[station].append(self.current_time)
        self.round_robin += 1
    
    def assign_shortest_queue(self):
        station = min(range(self.number_of_stations), key=lambda x: len(self.queues[x]))
        self.queues[station].append(self.current_time)
    
    def assign_random_queue(self):
        station = randint(0, self.number_of_stations - 1)
        self.queues[station].append(self.current_time)
        
def run_simulation(type_of_option, number_of_stations=5, arrival_rate=1, service_rate=5, simulation_duration=1000):
    sim = Custom_simulation(number_of_stations, arrival_rate, service_rate, type_of_option, simulation_duration)
    sim.run()
    return sim

# Example usage
simulation_duration = 100 
arrival_rate = 2
service_rate = 10

# Option 1: Single Queue
sim_single_queue = run_simulation('single_queue', simulation_duration=simulation_duration, arrival_rate=arrival_rate, service_rate=service_rate)

# Option 2.A: Round Robin
sim_round_robin = run_simulation('round_robin', simulation_duration=simulation_duration, arrival_rate=arrival_rate, service_rate=service_rate)

# Option 2.B: Shortest Queue
sim_shortest_queue = run_simulation('shortest_queue', simulation_duration=simulation_duration, arrival_rate=arrival_rate, service_rate=service_rate)

# Option 2.C: Random Queue
sim_random_queue = run_simulation('random_queue', simulation_duration=simulation_duration, arrival_rate=arrival_rate, service_rate=service_rate)

# Function to calculate and print results
def print_results(sim, type_of_option_name):
    print(f"Results for {type_of_option_name} type_of_option")
    print(f"Total passengers: {sim.total_passengers}")
    for i in range(sim.number_of_stations):
        avg_waiting_time = mean(sim.waiting_times[i]) if sim.waiting_times[i] else 0
        max_waiting_time = max(sim.waiting_times[i]) if sim.waiting_times[i] else 0
        max_queue_length = max(len(queue) for queue in sim.queues) if sim.queues else 0
        occupancy_rate = sim.occupancy_times[i] / sim.simulation_duration * 100
        
        print(f"Station {i+1}:")
        print(f"  Average waiting time: {avg_waiting_time:.3f}")
        print(f"  Maximum waiting time: {max_waiting_time:.3f}")
        print(f"  Maximum queue length: {max_queue_length}")
        print(f"  Occupancy rate: {occupancy_rate:.3f}%")
    print(end="++++++++++++++++++++++++++++++++++++++++++++++++")
    print(end="\n\n")

# Print results for each type_of_option
print_results(sim_single_queue, "Single Queue")
print_results(sim_round_robin, "Round Robin")
print_results(sim_shortest_queue, "Shortest Queue")
print_results(sim_random_queue, "Random Queue")
