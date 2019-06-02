#!/usr/bin/env python

#import matplotlib
#matplotlib.use('Agg')
from prevision import prevision
import matplotlib.pyplot as plt
from matplotlib.mlab import detrend_linear

from container import container
from icm_server import server
#import time
import configparser
import io
#import os

import sys
#import pathlib 
#import os.path

 







#from numpy import *
#import time

previsor=prevision("prevision")

single_execution=True
#cell_conf_file="cell.cfg"
cell_conf_file=""
#file_name="system_status.csv"
file_name=""
#myfileresultado=""
version="v0.2"

#container_list=list()
#add_cl=list()
container_list=list()
add_c=list()
del_c=list()
ncontainer=None
liv_time=list()
#mm=None

def get_total_processing_capacity():
	global container_list
	total_p_capacity=0
    #print ("cl:" , len (container_list))
	for mmc in container_list:
       # print (mmc.queue_req_pending())
		total_p_capacity+=mmc.processing_capacity()
	return total_p_capacity

def run():
 
	global container_list
	global add_c
	global del_c
    #gprint ("hola %d" % len(sys.argv)) 
	print ("")
	print ("=================================================================")
	print ("---------------------  COBEATS " + version + " -----------------------------" )
	print ("------  COntainers Bio-inspired Enhanced AuToscaling System -----")
	print ("--------------------  Simulation --------------------------------")
	print ("=================================================================")
	print ("")
	print('Python: {}'.format(sys.version))


    #import os
    #for k, v in os.environ.items():
    #      print "%s=%s" % (k,v)



	print ("Total Parameters          : %d " % len(sys.argv))
    #print ("Parameters List : ",  sys.argv)
	if (len(sys.argv) < 4):    
		print ("Run :" , sys.argv); 
		print (" expeced: conf_file load_file  output_file");
		quit()    
    

    #print('scipy: {}'.format(scipy.__version__))
    #print('numpy: {}'.format(numpy.__version__))
    # matplotlib
    #print('matplotlib: {}'.format(matplotlib.__version__))
    # pandas
    #import pandas
    #print('pandas: {}'.format(pandas.__version__))
    #    scikit-learn
     #import sklearn
    #print('sklearn: {}'.format(sklearn.__version__))



	print ("Load file                 : %s " % sys.argv[2])
	file_name=sys.argv[2]
	print ("Output file               : %s " % sys.argv[3])
	file_output_name=sys.argv[3]
	print ("Config file               : %s " % sys.argv[1])
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
    
	print ("Load Balancing Algorithm  : %d (1-Equal, 2-less Used , 3-Processing Capacity) " % load_balancing_algorithm )
	print ("Min Cells running         : %d" % minimun_cells)

	pdead_value = int (conf.get('Cell', 'deadprovability'))
	dead_cpu_use_value = int (conf.get('Cell', 'dead_cpu_use'))
	pdupl_value = int (conf.get('Cell', 'duplprovability'))
	dupl_cpu_use_value = int (conf.get('Cell', 'dupl_cpu_use'))
    #pmove = int (config.get('Cell', 'moveprovability'))
	pscav_value = int (conf.get('Cell', 'vscaprovability'))

	xaction = int (conf.get('Cell', 'X_total_containers'))
	print ("Tot Container in X action : %d" % (xaction))
	print ("Action Limits Average     : %d (%d - %d)" % (((dupl_cpu_use_value-dead_cpu_use_value)/2)+dead_cpu_use_value,dead_cpu_use_value, dupl_cpu_use_value))


	is_icm=int(conf.get('Container','icm_simulation'))
	icm_size=int(conf.get('Container','icm_size'))
	print ("Is icm simulation         : %d" % (is_icm))
	print ("icm size                  : %d" % (icm_size))


	calcular_prevision=int(conf.get('Simulation','prediction'))
	print ("Prevision                 : %d" % (calcular_prevision))

	

	print ("")
	print ("")
	print ("        D           s      S           X ")    
	print (" 0 <--------> %d <------------> %d <--------> 100" % (dead_cpu_use_value, dupl_cpu_use_value))
	print ("       %d              %d              %d " % (pdead_value, pscav_value, pdupl_value))
	print ("")
	print ("")




	print ("Starting Cobeats Simulation.....")
	print ("")


    
    #del container_list[:]

    #Initialize seed containers 
	s=server(icm_size)

	for x in range(0,minimun_cells):
		container_count+=1
        
		m=container(container_count,minimun_cells,cell_conf_file,0,s)
        #add_c.append(m)
		container_list.append(m)
        #print ("len:",len(container_list))
        
    #for x in add_c:
    #     print ("init",x)
    

    #Read load file
	num_lines = sum(1 for line in open(file_name))
	for m in range(0,num_lines):    
		print ("===================================================", m)
        #print (m)
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

        #pc=0
        #for mmc in container_list:
           # pc+=mmc.processing_capacity()

        
        
		print ("-cpu_requested read:",cpu_requested,"PC",pc)        
        
		reparto=0.0 
		if load_balancing_algorithm == 1 :
            #Round Robin
			try:
                #reparto=int(cpu_requested/len(container_list))
				reparto=(cpu_requested/len(container_list))
			except:
				reparto=0
			print ("Reparto:",reparto)

		elif load_balancing_algorithm == 2:
            #Least Connection Algorithm
			try:
				factor=0.0
				factor=float(cpu_requested)/float(pc)
				print ("factor:",factor)
			except:
				print ("Error en ", m)
        #elif load_balancing_algorithm == 3:
            #Maximo para los primeros
            #print ("maximo")
        #else:
        #    print ("Load Balancing Algoritm unknown")
        #    exit
           
        #print ("cpu_requested",cpu_requested)
        #print ("reparto:",reparto)
		queue_val=0
		cpu_pending_asignation=cpu_requested + cpu_pending_asignation
        #print ("pending....", cpu_pending_asignation, "container total:", len(container_list))
		tot=0



        #del add_cl[:]

       # for x in add_c:
         #     print ("remove",x)
          #     add_c.remove(x)
        #print ("=======")
		for mm in container_list:
			tot+=1
           # print (tot, len(container_list))
			acti=""
			if load_balancing_algorithm == 1 :
                #print ("Processing....")
				acti,queue_val=mm.process(reparto)
			elif load_balancing_algorithm == 2:
				acti,queue_val=mm.process(int(mm.processing_capacity()*factor))
			elif load_balancing_algorithm == 3:
				if cpu_pending_asignation>0 :
					acti,queue_val=mm.process(mm.processing_capacity())
					cpu_pending_asignation-=mm.processing_capacity()
				else:
					acti,queue_val=mm.process(0)    
            #print (cpu1)
            #acti=mm.actuate()
            #tp+=mm.processing_used()*mm.processing_capacity()/100




			tp+=mm.processing_used()



           # print ("acti:", acti)
            #pc+=mm.processing_capacity()
			if load_balancing_algorithm != 3 :
				qp+=mm.queue_req_pending()
            
            
            
          #  if mm.queue_req_pending() > 0 :
           #          print ("Queue Pending:", mm.queue_req_pending(), "   Processing_used:", mm.processing_used(), " Processing Capacity:", mm.processing_capacity())
            # print (acti, end='')
            
            
            #if (acti == 'X'):
			if (acti.count('X')>0 and False):
                #print ("----> X: %d" % (queue_val)) 
				total_x+=1
                #queue_val=queue_val/xaction
				for x in range(0,xaction):
                    #print (x)
                   # n_container=container(container_count,minimun_cells,cell_conf_file,queue_val)
                    #container_count=container_count+1
                    #container_list.append(n_container)
                   # add_c.append(ncontainer)
					container_count+=1
					add_c.append([container_count,minimun_cells,cell_conf_file,queue_val])
                    #print ("Creada %d - %d - %d" % (x,queue_val, xaction))
                #n_container2=container(container_count,minimun_cells,cell_conf_file,queue_val/2)
                #container_count=container_count+1
                #container_list.append(n_container2)
                #total_x+=1
                #print (container_count)
                #print ("ContCount  : %d " % (container_count))
                #print ("ContListLen: %d " % (len(container_list)))

			if (acti.count('D')>0 and False):
                #container_list.remove(mm)
                #container_count=container_count-1
				del_c.append(mm)
				total_d+=1
			if (acti.count('s')>0 and False):
				total_s+=1
			if (acti.count('S')>0 and False):
				total_S+=1
        #print ("processing_capacity", pc)    
    ########   print ("-Iter:", m, "req:",cpu1," >cells:", len(container_list),">", int(cpu1*100/len(container_list)), ">pc:",pc," tc:",tp )
    #values_list.append(iter)

        #if debug==True then print("--", pc,tp)
        #print("--", pc,tp) 
       # print ("Adding new container for next step....")

       # print ("Container Existing ", len(container_list), "Adding...", len(add_c))
       # container_list=container_list+add_cla
       # for xxx in container_list:
       #        print ("container_list",xxx
		for mm in del_c:
			liv_time.append(0)
			container_list.remove(mm)
		for xx in add_c:
               #print ("cl",xx[0],xx[1],xx[2],xx[3])
			n_container=container(xx[0],xx[1],xx[2],xx[3],s)
			container_list.append(n_container)
               #container_list.append(n_container)
               #container_list.extend(add_cl)
        #container_list.append(add_cl[:])
       # print ("Lengs:", len(container_list), len(add_c))
        #del add_cl[:]
		add_c=[]
		del_c=[]
        #print ("Lengs:", len(container_list), len(add_c))
        #print ("PC:", get_total_processing_capacity())


       # print ("Appending result information ...")
        
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

		#calcular_prevision=False
		if (calcular_prevision==1):
			previsor.add(cpu_requested)
			aux_prev=float(previsor.calculate())
		else:
			aux_prev=1
		#previsor.print()

		
		print ("container count:",container_count)
		print ("pc             :",pc)
		print ("tp             :",tp)
		print ("--> tp/pc      :",tp/pc)
		print ("pc/tp          :",pc/tp)
		if (calcular_prevision==1):
			calc_value=aux_prev
			print ("Prevision      :",aux_prev)
			print ("prevision/pc   :",aux_prev/pc)
		else:
			calc_value=float(cpu_requested)
		value_v=calc_value/pc
		print ("Value_v          :",value_v)	
		print ("Parte entera   :",int(value_v))
		if (value_v > 1.5):
		#if (tp/pc > 0.8):
            # n_container=container(xx[0],xx[1],xx[2],xx[3],s)
            #container_list.append(n_container)
			if (int(value_v)<1):
				add=1
			else:
				add=int(value_v)
			for t in range(1,int(value_v)):
				container_count+=1
				print (container_count)
				m=container(container_count,minimun_cells,cell_conf_file,0,s)
				container_list.append(m)
		if (value_v < 0.5 and container_count>minimun_cells ):
	#	if (tp/pc < 0.3 and container_count>minimun_cells ):
			container_list.pop()
			container_count-=1

                      
		print ("container count:",container_count)


		a.append(tp)
        #a.append(0)
        
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

		if (len(liv_time)>0) : 
			a.append(max(liv_time))
			a.append(min(liv_time))
			a.append(sum(liv_time))
		else:
			a.append(0)
			a.append(0)
			a.append(0)

		#a.append(0)
	#	a.append(0.0)
		#a.append("test")
        #a.append(0)
        #print (a)
        
         #12	
		results_list.append(a)
        #myresultado.write()
        
    
	print ("writing results in file -... ",file_output_name)
    #Save single result in a file    
    #myfile = io.open('../iofiles/resultado.txt', mode='wt', encoding='utf-8')
	myfile = io.open(file_output_name, mode='wt', encoding='utf-8')
	for lines in results_list:
		for item in lines:
			myfile.write(u''+str(item)+" ")
		myfile.write(u"\n")
	myfile.close
        
        
    
    
    
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
    
    
    
#	z9 = [x[11] for x in results_list]
    
    
    
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
    
	print ("Cobeats Simulation Ended")     
	print ("")
	print ("")
 



#global container_list
#global add_cl

#container_list=list()
#add_cl=list()


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
