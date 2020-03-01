#!/bin/bash

#####################################################################################
#######     Cobeat launcher    
#####################################################################################


#Change instalation directory for use 
BASE=/home/ubuntu/Mytest/cobeats/scm/v0.2
aaaa
aaaa


help(){
     echo "$0 option Load"
     echo "   Option: C - Conventional"
     echo "           B - Bioinspired"
     echo "           P - Prediction"
     echo "   Load: 1 - Sintetic load"
     echo "         2 - FIFA load"
     echo "         3 - NASA load" 
     exit
}

if [ "$#" -ne 2 ]; then
	help
	exit
fi


case $2 in
   1)
      echo "Option 1 - Sintetic load - "
      ORIGEN=$BASE/iofiles/system_status.csv
      CONF=$BASE/conf/cell_sint.cfg
      CONF_PREV=$BASE/conf/cell_sint_prev.cfg
      ;;
   2)
      echo "Option 2 - FIFA load"
      ORIGEN=$BASE/iofiles/system_status_fifa_corto.csv
      CONF=$BASE/conf/cell_fifa.cfg
      CONF_PREV=$BASE/conf/cell_fifa_prev.cfg
      ;;
   3)
      echo "Option 3 - NASA load"
      ORIGEN=$BASE/nasa_logs/nasa_log.csv
      CONF=$BASE/conf/cell_nasa.cfg
      CONF_PREV=$BASE/conf/cell_nasa_prev.cfg
      ;;
   *)
      echo "Option not selected"
      help
      exit

esac





#ORIGEN=../iofiles/system_status_fifa_corto.csv
#CONF=/home/ubuntu/Mytest/cobeats/scm/v0.2/conf/cell_fifa.cfg
case $1 in
  C)
     echo "Conventional"
     conda activate desa
     rm $BASE/iofiles/resultado1_compare_b.txt
     $BASE/cobeats/run_simulation_compare.py $CONF $ORIGEN $BASE/iofiles/resultado1_compare_b.txt
     $BASE/cobeats/plot1.1.py $BASE/iofiles/resultado1_compare_b.txt 1
     ;;

  B)
     echo "Bioinspirated"
     conda activate desa
     rm $BASE/iofiles/resultado1.txt
     $BASE/cobeats/run_simulation.py $CONF $ORIGEN $BASE/iofiles/resultado1.txt
     $BASE/cobeats/plot1.1.py $BASE/iofiles/resultado1.txt 1
     ;;
 
  P)
     echo "Prediction"
     conda activate desa
     rm $BASE/iofiles/resultado1_compare_b.txt
     $BASE/cobeats/run_simulation_compare.py $CONF_PREV $ORIGEN $BASE/iofiles/resultado1_compare_b.txt
     $BASE/cobeats/plot1.1.py ../iofiles/resultado1_compare_b.txt 1
     ;;

  *)
     echo "NOT suported option $1"
     help
     exit
esac
