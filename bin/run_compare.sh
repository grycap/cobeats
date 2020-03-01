#!/bin/bash

# run_compare.sh --  Cobeat launcher    
# JHH - Cobeats -2020
# Copyright (C) GRyCAP - I3M - UPV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


#Change instalation directory for use 
#BASE=/home/ubuntu/Mytest/cobeats/scm/v0.2
BASE=/home/ubuntu/repo/cobeats

help(){
     echo "$0 option Load"
     echo "   Option: C - Conventional"
     echo "           B - Bioinspired"
     echo "           P - Prediction"
     echo "   Load: 1 - Syntetic load"
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
      echo "Option 1 - Syntetic load - "
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
     FILE=$BASE/iofiles/resultado1_compare_b.txt
     [ -e $FILE ] && rm $FILE 
     $BASE/cobeats/run_simulation_compare.py $CONF $ORIGEN $FILE
     $BASE/cobeats/plot1.1.py $FILE 1
     ;;

  B)
     echo "Bioinspirated"
     conda activate desa
     FILE=$BASE/iofiles/resultado1.txt
     [ -e $FILE ] && rm $FILE 
     $BASE/cobeats/run_simulation.py $CONF $ORIGEN $FILE
     $BASE/cobeats/plot1.1.py $FILE 1
     ;;
 
  P)
     echo "Prediction"
     conda activate desa
     FILE=$BASE/iofiles/resultado1_compare_b.txt
     [ -e $FILE ] && rm $FILE 
     $BASE/cobeats/run_simulation_compare.py $CONF_PREV $ORIGEN $FILE
     $BASE/cobeats/plot1.1.py $FILE 1
     ;;

  *)
     echo "NOT suported option $1"
     help
     exit
esac
