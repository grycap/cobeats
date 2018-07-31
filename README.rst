.. Cobeats ()
=====================================

Cobeats
=======

Cobeats (COntainers Bio-inspired Enhanced AuToscaling System) is a software to test the proposoal of use bio-inspired cells in autoscaling systems based in software containers. 

Installation and use
--------------------

To run this code only is necesary copy software from this repository to running machine. It was executed in Python 3.5.2. No others versions are tested.



Basic execution example
-----------------------


To execute


Configuration
-------------
Configuration file for a simulation can use next parameters in seccions:

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












