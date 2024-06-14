import numpy as np
import heapq
import random

# Given parameters
D = 1000    # Sample duration of the simulation in "minutes"
A = 2       # Average arrival time (one new passenger every A minutes)
S = 5       # Average service rate (service time per passenger in minutes)
number_of_stations = 5

# Generate arrival and service times
def generate_arrivals(duration, arrival_rate):
    arrival = []
    time = 0


