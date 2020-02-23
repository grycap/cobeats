# Cobeats

COBEATS (COntainers Bio-inspired Enhanced AuToscaling System) is a software to test the proposal of using bio-inspired cells in autoscaling systems based on software containers. 

## Getting Started
This software introduces a set of bio-inspired algorithms aimed at supporting auto-scaling in Container Orchestration Platforms.

A key feature of cloud computing is elasticity, where applications can dynamically adjust the computing and storage resources. On the one hand, vertical elasticity involves increasing or decreasing the amount of computing and memory resources of a single computing entity. On the other hand, horizontal elasticity involves running on a distributed fleet of computing nodes that can grow and shrink according to the values of certain metrics, such as the average CPU usage across the available nodes.  This simulation software studies the impact of integrating bio-inspired approaches for dynamic distributed auto-scaling on container orchestration platforms. 

## Instalation and use
To run this code only (tested on Python 3.5.2), you need to install the following libraries:
* mathplotlib 2.2.3
* numpy 1.15.1
* pandas 0.23.4
* statsmodels 0.9.0
* sklearn 0.19.2

This repository includes the information about the simulated workloads.

## Basic execution example

For basic execution run ```bin/run_compare.sh``` with options. The first parameter is the algorithm used and the second one is the workload type.

The help is shown by running ```bin/run_compare.sh``` without options:

```sh
./run_compare.sh Option Load
option: 
 C - Conventional
 B - Bioinspired
 P - Prediction
Load: 
 1 - Synthetic load
 2 - FIFA load
 3 - NASA load
```

For example, executing ```bin/run_compare.sh B 1``` will run a bio-inspired algorithm with synthetic load.


## Configuration
Multiple file are added in this version to run all the tests. The configuration file for a simulation can use the following parameters in the corresponding sections:

**[Cell]** Section. This section contain information about the cell behaviour.
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
* cicles_req - Not operative
* slot_time - Not operative
* init_container_cicles_capacity - Not operative
* max_scale_limit - Maximum running vertical scaling capacity
* min_scale_limit - Minimum running vertical scaling capacity
* load_balancing_algorithm - Load balancing algorithm
* icm_simulation - Is an ICM algoritm simulation
* icm_size - ICM size for request data
* icm_neighbourhood_part - ICM part for neighbouhood of NOX funciton
* icm_local_part - ICM part for local part of NOX function

Notice the following example:
```
[Cell]
deadprobability = 80
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
* **G Moltó** - *Supervisor* - gmolto@dsic.upv.es  

## Licence

This project is licensed under the Apache 2.0 License - see the LICENSEE file for details.

