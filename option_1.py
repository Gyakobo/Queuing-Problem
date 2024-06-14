import numpy as np
import random

# Given parameters
D = 1000    # Sample duration of the simulation in "minutes"
A = 2       # Average arrival time (one new passenger every A minutes)
S = 5       # Average service rate (service time per passenger in minutes)
number_of_stations = 5 

# Generate arrival and service times
def generate_arrivals(duration, arrival_rate):
    arrivals = []
    time = 0

    while time < duration:
        time += np.random.exponential(arrival_rate)
        arrivals.append(time)
    return arrivals

def generate_service_time(service_rate):
    return np.random.exponential(service_rate)

# Option 1 - Single queue for all service stations
# Assuming we are given 5 servers to process the single queue
def single_queue(arrivals, service_rate, number_of_stations):
    queue           = []
    servers         = [0] * number_of_stations
    waiting_times   = [] 

    for arrival_time in arrivals:
        queue.append((arrival_time, generate_service_time(service_rate)))

    while queue:
        arrival_time, service_time = queue.pop(0)
        next_free_time = min(servers)
        if next_free_time > arrival_time:
            waiting_time = next_free_time - arrival_time 
        else:
            waiting_time = 0
        waiting_times.append(waiting_time)
        next_free_time = max(next_free_time, arrival_time) + service_time
        servers[servers.index(min(servers))] = next_free_time

    return np.mean(waiting_time)


# Run simulation
arrivals = generate_arrivals(D, A)
average_waiting_time_1 = single_queue(arrivals, S, number_of_stations)

print(f'Option 1: Average waiting time for "Single Queue" {average_waiting_time_1:.2f} minutes')
