# Queuing Scheduling 

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

>[!IMPORTANT]
>It is preferable that you run this code exclusively with `Python 3.10 (and onward)`

This project showcases 4 examples of 'queuing'

## Introduction

## Methodology

Please run the following command to ensure the version of python you currently have:

```bash
$ python3 -V
```

It is important to understand that you might need to run this program with `Python3.10 (or above)`. If you wish to update to Python version `3.12` please follow the following instructions: 

```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.12
```

## Results and Analysis

1) **Single Queue Results** 
At most 511 passengers were processed.

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
At most 498 passengers were processed.

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

3) **Shortest Queue**
At most 544 passengers were processed

## License
MIT