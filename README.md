# Queuing Scheduling 

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

>[!IMPORTANT]
>It is preferable that you run this code exclusively with `Python 3.10 (and onward)`

This project showcases 4 examples of `queuing`: Single Queue, Round Robin, Shortest Queue, Random Queue, that would try to process as many persons as possible.

## Introduction

Hearkening from the intro statement, this project basically tries to simulate a 5 vending stations which would in their turn accept customers. How and in what formation each queue would be organised will be analized in the methodology. 

## Methodology

Before you run this [program](https://github.com/Gyakobo/Queuing-Problem/blob/main/main.py) please run the following command to ensure the version of python you currently have:

```bash
$ python3 -V
```

It is important to understand that you ought need to run this program with `Python3.10 (or above)`. If you wish to update to Python version `3.12` please follow the following instructions: 

```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.12
```

1. To start off, we basically group all the passengers in one `Single Queue/Line` and process the one after the other. Nothing special here just an ordinary long queue. 

```python
def single_queue_func(self):
    self.q[0].append(self.time)
```

2. The second, option would be to use a `Round Robin Queue`. 

```python
def round_robin_func(self):
    station = self.round_robin % self.number_of_stations
    self.q[station].append(self.time)
    self.round_robin += 1
```

A `round-robin queue` is a type of scheduling algorithm used in computing where each process or task is assigned a fixed time slot in a cyclic order. This ensures that all tasks are treated equally and prevents any single task from monopolizing the CPU. It is particularly useful in time-sharing systems where multiple users or tasks require equal CPU time.

#### Characteristics of Round Robin Queue:
* Fixed Time Quantum: Each task is given a specific time slice or quantum to execute.
* Cyclic Order: Tasks are arranged in a circular queue and each task gets its turn in a cyclic manner.
* Preemption: If a task does not complete within its allocated time quantum, it is preempted and placed at the end of the queue.

3. Another option is the `Shortest Queue`. Long story short, each passenger attends the shortest queue he can find at the moment. 

```python
def shortest_queue_func(self):
    def queue_length(var):
        return len(self.q[var])

    station = min(range(self.number_of_stations), key=queue_length)
    self.q[station].append(self.time)
```

4. Lastly, we've got the `Random Queue`. Basically each passenger joins a random queue.

```python
def random_queue_func(self):
    station = randint(0, self.number_of_stations - 1)
    self.q[station].append(self.time)
```

## Results and Analysis

1) **Single Queue Results** 

At most `511` passengers were processed.

```bash
Option: Single Queue
Total Number of Passengers: 470
Station 1:
  Simulation duration:  1000
  Maximum queue length: 385
  Average waiting time: 394.376 && Maximum waiting time: 830.000
  Occupancy rate: 95.810%
Station 2:
  Simulation duration:  1000
  Maximum queue length: 385
  Average waiting time: 0.000 && Maximum waiting time: 0.000
  Occupancy rate: 0.000%
Station 3:
  Simulation duration:  1000
  Maximum queue length: 385
  Average waiting time: 0.000 && Maximum waiting time: 0.000
  Occupancy rate: 0.000%
Station 4:
  Simulation duration:  1000
  Maximum queue length: 385
  Average waiting time: 0.000 && Maximum waiting time: 0.000
  Occupancy rate: 0.000%
Station 5:
  Simulation duration:  1000
  Maximum queue length: 385
  Average waiting time: 0.000 && Maximum waiting time: 0.000
  Occupancy rate: 0.000%
```

2) **Round Robin Results**

At most `498` passengers were processed.

```bash
Option: Round Robin
Total Number of Passengers: 498
Station 1:
  Simulation duration:  1000
  Maximum queue length: 25
  Average waiting time: 23.404 && Maximum waiting time: 80.000
  Occupancy rate: 85.308%
Station 2:
  Simulation duration:  1000
  Maximum queue length: 25
  Average waiting time: 45.409 && Maximum waiting time: 128.000
  Occupancy rate: 96.173%
Station 3:
  Simulation duration:  1000
  Maximum queue length: 25
  Average waiting time: 113.400 && Maximum waiting time: 257.000
  Occupancy rate: 95.760%
Station 4:
  Simulation duration:  1000
  Maximum queue length: 25
  Average waiting time: 23.845 && Maximum waiting time: 92.000
  Occupancy rate: 83.921%
Station 5:
  Simulation duration:  1000
  Maximum queue length: 25
  Average waiting time: 45.413 && Maximum waiting time: 210.000
  Occupancy rate: 92.111%
```

3) **Shortest Queue Results**

At most `544` passengers were processed.

```bash
Option: Shortest Queue
Total Number of Passengers: 499
Station 1:
  Simulation duration:  1000
  Maximum queue length: 2
  Average waiting time: 34.312 && Maximum waiting time: 78.000
  Occupancy rate: 94.890%
Station 2:
  Simulation duration:  1000
  Maximum queue length: 2
  Average waiting time: 30.727 && Maximum waiting time: 100.000
  Occupancy rate: 94.332%
Station 3:
  Simulation duration:  1000
  Maximum queue length: 2
  Average waiting time: 28.590 && Maximum waiting time: 100.000
  Occupancy rate: 94.224%
Station 4:
  Simulation duration:  1000
  Maximum queue length: 2
  Average waiting time: 27.674 && Maximum waiting time: 105.000
  Occupancy rate: 90.925%
Station 5:
  Simulation duration:  1000
  Maximum queue length: 2
  Average waiting time: 22.056 && Maximum waiting time: 70.000
  Occupancy rate: 91.045%
```

4) **Random Queue Results**

At most `540` passengers were processed.

```bash
Option: Random Queue
Total Number of Passengers: 511
Station 1:
  Simulation duration:  1000
  Maximum queue length: 23
  Average waiting time: 51.553 && Maximum waiting time: 144.000
  Occupancy rate: 89.781%
Station 2:
  Simulation duration:  1000
  Maximum queue length: 23
  Average waiting time: 60.466 && Maximum waiting time: 158.000
  Occupancy rate: 90.702%
Station 3:
  Simulation duration:  1000
  Maximum queue length: 23
  Average waiting time: 26.030 && Maximum waiting time: 92.000
  Occupancy rate: 84.166%
Station 4:
  Simulation duration:  1000
  Maximum queue length: 23
  Average waiting time: 179.733 && Maximum waiting time: 309.000
  Occupancy rate: 97.104%
Station 5:
  Simulation duration:  1000
  Maximum queue length: 23
  Average waiting time: 17.659 && Maximum waiting time: 66.000
  Occupancy rate: 81.317%
```

## License
MIT