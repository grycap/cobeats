#../cobeats/run_simulation.py ../conf/cell.cfg ../iofiles/system_status.csv ../iofiles/resultado2.txt

help(){
     echo "$0 opcion Load"
     echo "   option: C - Conventional"
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
echo "Opcion 1 - Sintetic load - "
ORIGEN=/home/ubuntu/Mytest/cobeats/scm/v0.2/iofiles/system_status.csv
CONF=/home/ubuntu/Mytest/cobeats/scm/v0.2/conf/cell_sint.cfg
CONF_PREV=/home/ubuntu/Mytest/cobeats/scm/v0.2/conf/cell_sint_prev.cfg
;;
2)
echo "Opcion 2 - FIFA load"
ORIGEN=/home/ubuntu/Mytest/cobeats/scm/v0.2/iofiles/system_status_fifa_corto.csv
CONF=/home/ubuntu/Mytest/cobeats/scm/v0.2/conf/cell_fifa.cfg
#CONF=/home/ubuntu/Mytest/cobeats/scm/v0.2/conf/cell_fifa.cfg.old
CONF_PREV=/home/ubuntu/Mytest/cobeats/scm/v0.2/conf/cell_fifa_prev.cfg
;;
3)
echo "Opcion 3 - NASA load"
ORIGEN=/home/ubuntu/Mytest/cobeats/scm/v0.2/nasa_logs/nasa_log.csv
#CONF=/home/ubuntu/Mytest/cobeats/scm/v0.2/conf/cell_nasa.cfg.old
CONF=/home/ubuntu/Mytest/cobeats/scm/v0.2/conf/cell_nasa.cfg
CONF_PREV=/home/ubuntu/Mytest/cobeats/scm/v0.2/conf/cell_nasa_prev.cfg
;;
*)
echo "Opcion no seleccionada"
help
exit

esac





#ORIGEN=../iofiles/system_status_fifa_corto.csv
#CONF=/home/ubuntu/Mytest/cobeats/scm/v0.2/conf/cell_fifa.cfg
case $1 in
C)
echo "Conventional"
conda activate desa
#../cobeats/run_simulation_compare.py ../conf/cell.cfg ../iofiles/system_status_fifa_corto.csv ../iofiles/resultado1_compare_b.txt
rm ../iofiles/resultado1_compare_b.txt
../cobeats/run_simulation_compare.py $CONF $ORIGEN ../iofiles/resultado1_compare_b.txt
../cobeats/plot1.1.py ../iofiles/resultado1_compare_b.txt 1
;;

B)
echo "Bioinspirated"
conda activate desa
rm ../iofiles/resultado1.txt
../cobeats/run_simulation.py $CONF $ORIGEN ../iofiles/resultado1.txt
../cobeats/plot1.1.py ../iofiles/resultado1.txt 1
;;
P)
echo "Prediction"
conda activate desa
#../cobeats/run_simulation_compare.py ../conf/cell.cfg ../iofiles/system_status_fifa_corto.csv ../iofiles/resultado1_compare_b.txt
rm ../iofiles/resultado1_compare_b.txt
../cobeats/run_simulation_compare.py $CONF_PREV $ORIGEN ../iofiles/resultado1_compare_b.txt
../cobeats/plot1.1.py ../iofiles/resultado1_compare_b.txt 1
;;

*)
echo "NOT suported option $1"
help
exit
esac
