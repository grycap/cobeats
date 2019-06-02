# Cobeats

Cobeats (COntainers Bio-inspired Enhanced AuToscaling System) is a software to test the proposoal of use bio-inspired cells in autoscaling systems based in software containers. 

## Getting Started
This software introduces a set of bio-inspired algorithms aimed at supporting auto-scaling in container-based computing platforms.

A key feature of cloud computing is elasticity, where applications can dynamically adjust the computing and storage resources. On the one hand, vertical elasticity involves increasing or decreasing the amount of computing and memory resources of a single computing entity. On the other hand, horizontal elasticity requires changing the architecture of the application to run on a distributed fleet of computing nodes that can grow and shrink according to the values of certain metrics, such as the average CPU usage across the available nodes.

## Instalation and use
To run this code only is necesary copy software from this repository to running machine. It was executed in Python 3.5.2. No others versions are tested.
Some python libreries are necesary to run Cobeats. 

* mathplotlib 2.2.3
* numpy 1.15.1
* pandas 0.23.4
* statsmodels 0.9.0
* sklearn 0.19.2


## Basic execution example

For basic execution run ./bin/run_compare.sh with options. First parameter is algorithm used and second one is load type.

Using help in ./run_compare shell without option  you can see all posible options.

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

For example, executing ./run_compare.sh B 1  is posible run ia Bio-inspired algorithm with Sintetic load.


## Configuration
Multiple file are added in this version to run all test. Configuration file for a simulation can use next parameters in seccions:

**[Cell]** Section. This section contain information about cell behaviour.
* deadprobability - Dead probability for algorithm limits.
* dead_cpu_use - Limit for dead resource use.
* moveprobability - Not used
* vscaprobability - Vertical scaling probability
* duplprobability - Creation area probability
* dupl_cpu_use - Limit for X (creation area)
* init_process_capacity - Initial node capacity
* variation_process_capacity - Step variation for vertical scaling
* max_history - Not used
* X_total_containers - Total containers created for X actions

**[Simulation]** Section for simulation
* minimun_cells_running - Mininum running cells

**[Container]** Container part for simulation
* cicles_req - NOt operative
* slot_time - Not operative
* init_container_cicles_capacity - Not operative
* max_scale_limit - Maximun running vertical scaling capacity
* min_scale_limit - Minimun running vertical scaling capacity
* load_balancing_algorithm - Load balancing algorithm
* icm_simulation - Is a icm algoritm simulation
* icm_size - icm size for request data
* icm_neighbourhood_part - icm part for neighbouhood of NOX funciton
* icm_local_part - icm part for local part of NOX function

a simple example
```
[Cell]
dprobability = 80
dead_cpu_use = 30
moveprobability = 10
vscaprobability = 80
duplprobability = 80
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

## Authors

* **J Herrera** - *Initial work* - jherrera@upv.es
* **G Molto**

## Licence

This project is licensed under the Apache LIcense - see the LICENCE file for details.

