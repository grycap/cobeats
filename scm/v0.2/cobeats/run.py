#!/usr/bin/env python

#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.mlab import detrend_linear

from container import container
#import time
import configparser
import io
#import os

import sys
#import pathlib 
#import os.path

 







#from numpy import *
#import time

single_execution=True
#cell_conf_file="cell.cfg"
cell_conf_file=""
#file_name="system_status.csv"
file_name=""
#myfileresultado=""
version="v0.2"

container_list=list()

def get_total_processing_capacity():
    total_p_capacity=0
    for mm in container_list:
        total_p_capacity+=mm.processing_capacity()
    return total_p_capacity

def run():
 
    #gprint ("hola %d" % len(sys.argv)) 
    print ("")
    print ("=================================================================")
    print ("---------------------  COBEATS " + version + " -----------------------------" )
    print ("------  COntainers Bio-inspired Enhanced AuToscaling System -----")
    print ("=================================================================")
    print ("")

    print ("Total Parameters: %d " % len(sys.argv))
    #print ("Parameters List : ",  sys.argv)
    if (len(sys.argv) < 3):    
        print ("Run :" , sys.argv); 
        quit()    
    
    print ("Load file       : %s " % sys.argv[2])
    file_name=sys.argv[2]
    print ("Config file     : %s " % sys.argv[1])
    cell_conf_file=sys.argv[1]
   # myfile=Path(cell_conf_file)
   # if not(myfile.exist()):
   #    print("File conf not exist")
   #    quit()



    results_list=list()
    
    container_count=0
    cpu_pending_asignation=0
    
    
    
    conf = configparser.ConfigParser()
    try:
        conf.readfp(open(cell_conf_file,"r"))
    except IOError:
        print ("Error Reading conf file")
        quit()
    #conf.readfp(open(r'cell.cfg'))
    minimun_cells= int (conf.get('Simulation', 'minimun_cells_running'))
    cicles_req= int (conf.get('Container', 'cicles_req'))
    load_balancing_algorithm=int(conf.get('Container','load_balancing_algoritm'))
    
    print ("Load Balancing Algorithm: %d" % load_balancing_algorithm )
    print ("Min Cells running: %d" % minimun_cells)
    print ("")
    print ("")
    print ("        D           s            S           X ")    
    print (" 0 <--------> 50 <------> 60 <------> 80 <--------> 100")
    print ("       10%          10%        20%          60% ")
    print ("")
    print ("")



    
    #Initialize seed containers 
    for x in range(0,minimun_cells):
        container_count+=1
        m=container(container_count,minimun_cells,cell_conf_file)
        container_list.append(m)
        
    
    #Read load file
    num_lines = sum(1 for line in open(file_name))
    for m in range(0,num_lines):    
        f = open(file_name,"r")
        lines = f.readlines()
        # If we need to read line 33, and assign it to some variable
        linea_leida = lines[int(m)]
        
        cpu_requested, mem1, io1 = (int(val) for val in linea_leida.split())
        
        cpu_requested=cpu_requested*cicles_req
        
        
        
        #cpu_corregido=cpu1*100/len(cell_list)
        pc=0  #processing capacity
        tp=0  #processing used
        qp=0  #requests pending
        total_x=0
        total_d=0
        total_n=0
        total_s=0
        total_S=0
        #cpu_read=cpu1
        #cpu1=cpu1*100
        pc=get_total_processing_capacity()
        
        
        
        
        
        if load_balancing_algorithm == 1 :
            #Round Robin
            try:
                reparto=int(cpu_requested/len(container_list))
            except:
                reparto=0
                
        elif load_balancing_algorithm == 2:
            #Least Connection Algorithm
            factor=cpu_requested/pc
        #elif load_balancing_algorithm == 3:
            #Maximo para los primeros
            #print ("maximo")
        #else:
        #    print ("Load Balancing Algoritm unknown")
        #    exit
           
        #print ("cpu_requested",cpu_requested)
        #print ("reparto:",reparto)
        cpu_pending_asignation=cpu_requested + cpu_pending_asignation
        for mm in container_list:
            if load_balancing_algorithm == 1 :
                acti=mm.process(reparto)
            elif load_balancing_algorithm == 2:
                acti=mm.process(mm.processing_capacity()*factor)
            elif load_balancing_algorithm == 3:
                if cpu_pending_asignation>0 :
                    acti=mm.process(mm.processing_capacity())
                    cpu_pending_asignation-=mm.processing_capacity()
                else:
                    acti=mm.process(0)    
            #print (cpu1)
            #acti=mm.actuate()
            #tp+=mm.processing_used()*mm.processing_capacity()/100
            tp+=mm.processing_used()
            #pc+=mm.processing_capacity()
            if load_balancing_algorithm != 3 :
                qp+=mm.queue_req_pending()
            
            
            
          #  if mm.queue_req_pending() > 0 :
           #          print ("Queue Pending:", mm.queue_req_pending(), "   Processing_used:", mm.processing_used(), " Processing Capacity:", mm.processing_capacity())
            # print (acti, end='')
            
            
            #if (acti == 'X'):
            if (acti.count('X')>0):
                n_container=container(container_count,minimun_cells,cell_conf_file)
                container_count=container_count+1
                container_list.append(n_container)
                total_x+=1
            if (acti.count('D')>0):
                container_list.remove(mm)
                total_d+=1
            if (acti.count('s')>0):
                total_s+=1
            if (acti.count('S')>0):
                total_S+=1
        #print ("processing_capacity", pc)    
    ########   print ("-Iter:", m, "req:",cpu1," >cells:", len(container_list),">", int(cpu1*100/len(container_list)), ">pc:",pc," tc:",tp )
    #values_list.append(iter)
        a=list()
        
        # 0 time
        a.append(m)
        
        # 1 cpu requested
        a.append(cpu_requested)
        
        # 2 Total Containers
        a.append(len(container_list))
        
        # 3 processing capacity
        a.append(pc)
        
        # 4 processing capacity used
        a.append(tp)
        
        # 5 Request Pending Queue Lengh
        if load_balancing_algorithm == 3:
            a.append(cpu_pending_asignation)
        else:  
            a.append(qp)
        
        # 6 % processing capacity used
        if pc == 0:
            a.append(100)
        else:
            a.append(tp*100/pc)
            
        # 7 Series de X
        a.append(total_x)
        
        # 8 Serie de D
        a.append(total_d)
        
        # 9 Serie de s
        a.append(total_s)
        
        # 10 Serie de S
        a.append(total_S)
        
        # 11
        if pc == 0:
            #a.append(100)
            n=100
        else:
            n=(cpu_requested)*100/pc
            #a.append((cpu_requested)*100/pc)
            #a.append((cpu_read*cicles_req)*100/pc)
        if n > 100:
            n=100
        a.append(n)
        #a.append(0)
        #print (a)
        
        # 12
        results_list.append(a)
        #myresultado.write()
        
    
    #Save single result in a file    
    myfile = io.open('../iofiles/resultado.txt', mode='wt', encoding='utf-8')
    for lines in results_list:
        for item in lines:
            myfile.write(u''+str(item)+" ")
        myfile.write(u"\n")
    myfile.close
        
        
    plt.xlabel("Iteraction")
    plt.ylabel("Y-axis")
    plt.title("A test graph")
    
    
    
    #time
    time_serie = [x[0] for x in results_list]
    #requests
    request_serie = [x[1] for x in results_list]
    #request_serie_MIPS = [x[1] for x in results_list]
    #Total Containers Running
    TotalContainer_serie = [x[2] for x in results_list]

    #Processing Capacity
    ProcessingCapacity_serie = [x[3] for x in results_list]
    
    #Processing Capacity Used
    ProcessingCapacityUsed_serie = [x[4] for x in results_list]
    
    #QueueLength
    QueueLength = [x[5] for x in results_list]
    
       
    PercentProcessingUsed = [x[6] for x in results_list]
    

    # X (container creation) serie
    X_serie = [x[7] for x in results_list]
    #D (Container Dead) serie
    D_serie = [x[8] for x in results_list]
    #s Scale UP 
    s_serie = [x[9] for x in results_list]
    #S Scale Down (S Capital)
    S_serie = [x[10] for x in results_list]
    
    
    
    z9 = [x[11] for x in results_list]
    
    
    
    y_cicle = [x[1]*100 for x in results_list]
 
    
    #suma=0
    #for i in z4:
     #   suma=suma+i
    #print (suma/len(z4))
    #myfileresultado.write(str(int(suma)/len(z4)))
    
    suma=0
    for i in QueueLength:
        suma=suma+i
    #print (suma/len(QueueLength))
    myfileresultado.write(u";" + str(int(suma)/len(QueueLength)))
    
    
    
    if single_execution :
    
    
        plt.figure(1)
        plt.subplot(211)
        plt.plot(time_serie,request_serie)
        plt.legend(['requests'])
        #plt.xlabel("Iteraction")
        
        plt.subplot(212)
        plt.plot(time_serie,TotalContainer_serie)
        plt.plot(time_serie,X_serie)
        plt.plot(time_serie,D_serie)
        plt.plot(time_serie,s_serie)
        plt.plot(time_serie,S_serie)
        plt.legend(['Containers','X','D','s','S'])
        
        plt.figure(2)
        plt.subplot(211)
        #plt.plot(time_serie,request_serie_MIPS)
        plt.plot(time_serie,ProcessingCapacity_serie)
        plt.plot(time_serie,ProcessingCapacityUsed_serie)
        plt.plot(time_serie,QueueLength)
        #plt.plot(time_serie,y_cicle)
        #plt.legend(['Tot.ProcessingCapacity','tp','qp','cicles'])
        plt.legend(['Tot.ProcessingCapacity','Tot.ProcessingCapacity_used','QueueLength'])
        plt.subplot(212)
        plt.plot(time_serie,PercentProcessingUsed)
        plt.plot(time_serie,z9)
        #plt.plot(time_serie,PercentProcessingUsed)
        #plt.plot(x,z6)
        #plt.plot(x,z7)
        #plt.plot(x,z8)
        plt.legend(['%TotalCapacityUsed', '%requested processed'])
        #print ("----->", request_list[1])
        
        
        
        plt.figure(3)
        
        plt.bar([p for p in time_serie], X_serie ,width=0.9,color='b',align='center')
        plt.bar([p for p in time_serie], D_serie,width=0.9,color='g',align='center')
        plt.bar([p for p in time_serie], s_serie,width=0.9,color='r',align='center')
        plt.bar([p for p in time_serie], S_serie,width=0.9,color='y',align='center')
    
   
        #plt.savefig('./plot.png')
       # os.system('./plot.png')
        plt.show()
        import dtw
        dtw.dtw_show()
         
       



if __name__ == '__main__':
        
#def main():        
    if single_execution  :
        #version solo una ejecucion
        myfileresultado = io.open('../iofiles/resultadocorto.txt', mode='a', encoding='utf-8')
        run()
    else:    
        #version multiple ejecucion
        myfileresultado = io.open('../iofiles/resultadogrande.txt', mode='a', encoding='utf-8')
        cont=0
        for VarDead in range(5,100,10):
            for VarDeadProvability in range(5,100,10):
                for VarCreate in range(VarDead,100,10):
                    for VarCreateProvability in range(5,100,10):
                        cont+=1
                   
               
                        myfileconf = io.open('cell.cfg', mode='wt', encoding='utf-8')
                        myfileconf.write(u'[Cell] \n' +
                        'deadprovability = ' + str(VarDeadProvability) + ' \n' +
                        'dead_cpu_use = ' + str(VarDead) +' \n'+
                        'moveprovability = 10 \n'+
                        'vscaprovability = 0 \n'+
                        'duplprovability = '+ str(VarCreateProvability) +' \n'+
                        'dupl_cpu_use = ' + str(VarCreate) +' \n'+
                        'init_process_capacity=1000 \n'+
                        'variation_process_capacity=25 \n'+
                        'max_history=30 \n'+
                        '[Simulation] \n'+
                        'minimun_cells_running = 2 \n' +
                        '[Container] \n'+
                        'cicles_req=100 \n'+
                        'init_container_cicles_capacity=1000 \n'+
                        'max_scale_limit=4000 \n'+
                        'min_scale_limit=500 \n'+
                        #'minimun_cells_running=2 \n ' +

                        '\n')
                    
                        myfileconf.close()
            
                    
                        print (cont, "-" ,VarDead, "-" , VarDeadProvability)
                        myfileresultado.write(str(VarDead)               +';' 
                                        + str(VarDeadProvability)    +';'
                                        + str(VarCreate)             +';' 
                                        + str(VarCreateProvability)  +';' )
                    
                    
                    
                    
                        myfileresultado.flush()
                        run()
                        myfileresultado.write('\n')
            
        myfileresultado.close()



 
#main()
