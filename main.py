# DISCLAIMOR: Please run this program with python3.10 (or above). Any version lower will not work

# Import mean function from stats library, and expovariate and randint functions from random library 
from statistics import mean
from random import expovariate, randint 

# Once again it is important to run this program with Python3.10 (or above)
import sys
if not sys.version_info >= (3, 10):
    print("Please run code on 'Python3.10 (or above)'")
    exit(-1)


# Given Parameters 
simulation_duration = 1000 # D = 1000 (minutes) 
arrival_rate = 2           # A = 2 (minute/passenger)
service_rate = 10          # S = 5 * A => 5 * 2 => 10; Given by the assignment
number_of_given_stations = 5


# We are going to stick all simulation types(single queue, round robin, shortest queue, random queue) all into one class
class Custom_simulation:
    def __init__(self, number_of_stations, arrival_rate, service_rate, type_of_option, simulation_duration):

        # Mutual Variables
        self.type_of_option = type_of_option
        self.simulation_duration = simulation_duration
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.queues             = []
        self.waiting_times      = []
        self.occupancy_times    = []
        self.service_end_times  = []


        # Option 1 && 2 var(s)
        self.number_of_stations = number_of_stations
        for _ in range(number_of_stations): 
            # The mutual occupiable queue
            self.queues.append([])
            # Wait time per service station 
            self.waiting_times.append([])
            
            self.occupancy_times.append(0)
            self.service_end_times.append(0)

        self.round_robin = 0
        self.total_passengers = 0

        # Current time 
        self.time = 0

        # It's preferable to use random.expovariate instead of
        self.next_arrival_time = expovariate(1.0 / self.arrival_rate)
        
    def single_queue_func(self):
        self.queues[0].append(self.time)
    
    def round_robin_func(self):
        station = self.round_robin % self.number_of_stations
        self.queues[station].append(self.time)
        self.round_robin += 1
    
    def shortest_queue_func(self):
        def queue_length(var):
            return len(self.queues[var])

        station = min(range(self.number_of_stations), key=queue_length)
        self.queues[station].append(self.time)
    
    def random_queue_func(self):
        station = randint(0, self.number_of_stations - 1)
        self.queues[station].append(self.time)
        
    def run(self):
        while self.time < self.simulation_duration:
            self.time += 1
            if self.time >= self.next_arrival_time:
                self.total_passengers += 1

                match self.type_of_option:
                    case "single_queue":
                        self.single_queue_func()
                    case "round_robin":
                        self.round_robin_func()
                    case "shortest_queue":
                        self.shortest_queue_func()
                    case "random_queue":
                        self.random_queue_func()
                
                self.next_arrival_time += expovariate(1.0 / self.arrival_rate)
            
            for i in range(self.number_of_stations):
                if self.time >= self.service_end_times[i] and self.queues[i]:

                    # Adjust the arrival time
                    arrival_time = self.queues[i].pop(0)

                    # Adjust the wating time
                    waiting_time = self.time - arrival_time

                    self.waiting_times[i].append(waiting_time)
                    service_time = expovariate(1.0 / self.service_rate)
                    self.occupancy_times[i] += service_time
                    self.service_end_times[i] = self.time + service_time
        
def run_simulation(type_of_option, number_of_stations=5, arrival_rate=1, service_rate=5, simulation_duration=1000):
    sim = Custom_simulation(number_of_stations, arrival_rate, service_rate, type_of_option, simulation_duration)
    sim.run()
    return sim


# Option 1: Single Queue
sim_single_queue = Custom_simulation(number_of_given_stations, arrival_rate, service_rate, "single_queue", simulation_duration)
sim_single_queue.run()

# Option 2.A: Round Robin
sim_round_robin = Custom_simulation(number_of_given_stations, arrival_rate, service_rate, "round_robin", simulation_duration)
sim_round_robin.run()

# Option 2.B: Shortest Queue
sim_shortest_queue = Custom_simulation(number_of_given_stations, arrival_rate, service_rate, "shortest_queue", simulation_duration)
sim_shortest_queue.run()

# Option 2.C: Random Queue
sim_random_queue = Custom_simulation(number_of_given_stations, arrival_rate, service_rate, "random_queue", simulation_duration)
sim_random_queue.run()


# Function to calculate and print results
def print_analysis(sim, type_of_option_name):
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
print_analysis(sim_single_queue, "Single Queue")
print_analysis(sim_round_robin, "Round Robin")
print_analysis(sim_shortest_queue, "Shortest Queue")
print_analysis(sim_random_queue, "Random Queue")