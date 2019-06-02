# Cobeats

Cobeats (COntainers Bio-inspired Enhanced AuToscaling System) is a software to test the proposoal of use bio-inspired cells in autoscaling systems based in software containers. 

## Getting Started



## Instalation and use
To run this code only is necesary copy software from this repository to running machine. It was executed in Python 3.5.2. No others versions are tested.
Some python libreries are necesary to run Cobeats. 

* mathplotlib 2.2.3
* numpy 1.15.1
* pandas 0.23.4
* statsmodels 0.9.0
* sklearn 0.19.2


## Basic execution example

For basic execution run ./bin/run_compare.sh with options. Fires is algorithm used and second is load type

Using help in ./run_compare shell, you can see all options
```
./run_compare.sh Option Load
option: 
 C - Conventional
 B - Bioinspired
 P - Prediction
Load: 
 1 - Sintetic load
 2 - FIFA load
 3 - NASA load
```

For example ./run_compare.sh B 1   for run Bio-inspared algorithm with Sintetic load.


## Configuration
Multiple file are added in this version to run all test. Configuration file for a simulation can use next parameters in seccions:

* [Cell] Section. This section contain information about cell behaviour
* deadprovability 
* dead_cpu_use

* moveprovability
* vscaprovability

* duplprovability
* dupl_cpu_use

init_process_capacity
variation_process_capacity

max_history

X_total_containers




[Simulation] Section
minimun_cells_running


[Container]

cicles_req
slot_time
init_container_cicles_capacity
max_scale_limit
min_scale_limit

load_balancing_algorithm

icm_simulation
icm_size
icm_neighbourhood_part
icm_local_part

a simple example
```
dprovability = 80
dead_cpu_use = 30
moveprovability = 10
vscaprovability = 80
duplprovability = 80
dupl_cpu_use = 90
init_process_capacity=1000
variation_process_capacity=25
max_history=30
X_total_containers=1

[Simulation]
minimun_cells_running = 5
prediction=0

[Container]
cicles_req=1000000
slot_time=5000
init_container_cicles_capacity=200000
max_scale_limit=1000000000000
min_scale_limit=500
load_balancing_algoritm=2
icm_simulation=0
icm_size=20
icm_neibourhood_part=90
icm_local_part=10
```

##Authors

* **Jose Herrera** - *Initial work*

##Licence

This project is licensed under the Apache LIcense - see the [LICENCE] (LICENCE) file for details.

