.. Cobeats ()
=====================================
=======
Cobeats
=======
-------------------------------
A cell based autoscaling system
-------------------------------


Cobeats (COntainers Bio-inspired Enhanced AuToscaling System) is a software to test the proposoal of use bio-inspired cells in autoscaling systems based in software containers. 

Installation and use
--------------------

To run this code only is necesary copy software from this repository to running machine. It was executed in Python 3.5.2. No others versions are tested.



Basic execution example
-----------------------

For basic execution run ./bin/run_compare.sh with options. Fires is algorithm used and second is load type

Using help in ./run_compare shell, you can see all options
run_compare.sh opcion Load
option: 
C - Conventional
B - Bioinspired
P - Prediction
Load: 
1 - Sintetic load
2 - FIFA load
3 - NASA load

For example ./run_compare.sh B 1   for run Bio-inspared algorithm with Sintetic load.



Configuration
-------------
Multiple file are added in this version to run all test. Configuration file for a simulation can use next parameters in seccions:

[Cell] Section. This section contain information about cell behaviour

deadprovability
dead_cpu_use

moveprovability
vscaprovability

duplprovability
dupl_cpu_use

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












