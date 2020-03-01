#!/usr/bin/env python
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


from prevision import prevision
import matplotlib.pyplot as plt
from matplotlib.mlab import detrend_linear
from container import container
from icm_server import server
import configparser
import io
import sys

 








previsor=prevision("prevision")

single_execution=True
cell_conf_file=""
file_name=""
version="v0.2"

container_list=list()
add_c=list()
del_c=list()
ncontainer=None
liv_time=list()

def get_total_processing_capacity():
	global container_list
	total_p_capacity=0
	for mmc in container_list:
		total_p_capacity+=mmc.processing_capacity()
	return total_p_capacity

def run():
 
	global container_list
	global add_c
	global del_c
	print ("")
	print ("=================================================================")
	print ("---------------------  COBEATS " + version + " -----------------------------" )
	print ("------  COntainers Bio-inspired Enhanced AuToscaling System -----")
	print ("--------------------  Simulation --------------------------------")
	print ("=================================================================")
	print ("")
	print('Python: {}'.format(sys.version))
	print ("Total Parameters          : %d " % len(sys.argv))
	if (len(sys.argv) < 4):    
		print ("Run :" , sys.argv); 
		print (" expeced: conf_file load_file  output_file");
		quit()    

	print ("Load file                 : %s " % sys.argv[2])
	file_name=sys.argv[2]
	print ("Output file               : %s " % sys.argv[3])
	file_output_name=sys.argv[3]
	print ("Config file               : %s " % sys.argv[1])
	cell_conf_file=sys.argv[1]

	results_list=list()
    
	container_count=0
	cpu_pending_asignation=0
    
    
    
	conf = configparser.ConfigParser()
	try:
		conf.readfp(open(cell_conf_file,"r"))
	except IOError:
		print ("Error Reading conf file")
		quit()
	minimun_cells= int (conf.get('Simulation', 'minimun_cells_running'))
	cicles_req= int (conf.get('Container', 'cicles_req'))
	load_balancing_algorithm=int(conf.get('Container','load_balancing_algoritm'))
    
	print ("Load Balancing Algorithm  : %d (1-Equal, 2-less Used , 3-Processing Capacity) " % load_balancing_algorithm )
	print ("Min Cells running         : %d" % minimun_cells)

	pdead_value = int (conf.get('Cell', 'deadprobability'))
	dead_cpu_use_value = int (conf.get('Cell', 'dead_cpu_use'))
	pdupl_value = int (conf.get('Cell', 'duplprobability'))
	dupl_cpu_use_value = int (conf.get('Cell', 'dupl_cpu_use'))
	pscav_value = int (conf.get('Cell', 'vscaprobability'))

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

    
	s=server(icm_size)

	for x in range(0,minimun_cells):
		container_count+=1
        
		m=container(container_count,minimun_cells,cell_conf_file,0,s)
		container_list.append(m)
        
	num_lines = sum(1 for line in open(file_name))
	for m in range(0,num_lines):    
		print ("===================================================", m)
		f = open(file_name,"r")
		lines = f.readlines()
		linea_leida = lines[int(m)]
        
		cpu_requested, mem1, io1 = (int(val) for val in linea_leida.split())
        
		cpu_requested=cpu_requested*cicles_req
        
         
        
		pc=0  #processing capacity
		tp=0  #processing used
		qp=0  #requests pending
		total_x=0
		total_d=0
		total_n=0
		total_s=0
		total_S=0
		pc=get_total_processing_capacity()

		print ("-cpu_requested read:",cpu_requested,"PC",pc)        
        
		reparto=0.0 
		if load_balancing_algorithm == 1 :
			try:
				reparto=(cpu_requested/len(container_list))
			except:
				reparto=0
			print ("Reparto:",reparto)

		elif load_balancing_algorithm == 2:
			try:
				factor=0.0
				factor=float(cpu_requested)/float(pc)
				print ("factor:",factor)
			except:
				print ("Error en ", m)
		queue_val=0
		cpu_pending_asignation=cpu_requested + cpu_pending_asignation
		tot=0
		for mm in container_list:
			tot+=1
			acti=""
			if load_balancing_algorithm == 1 :
				acti,queue_val=mm.process(reparto)
			elif load_balancing_algorithm == 2:
				acti,queue_val=mm.process(int(mm.processing_capacity()*factor))
			elif load_balancing_algorithm == 3:
				if cpu_pending_asignation>0 :
					acti,queue_val=mm.process(mm.processing_capacity())
					cpu_pending_asignation-=mm.processing_capacity()
				else:
					acti,queue_val=mm.process(0)    




			tp+=mm.processing_used()

			if load_balancing_algorithm != 3 :
				qp+=mm.queue_req_pending()
            
            
            
			if (acti.count('X')>0 and False):
				total_x+=1
				for x in range(0,xaction):
					container_count+=1
					add_c.append([container_count,minimun_cells,cell_conf_file,queue_val])

			if (acti.count('D')>0 and False):
				del_c.append(mm)
				total_d+=1
			if (acti.count('s')>0 and False):
				total_s+=1
			if (acti.count('S')>0 and False):
				total_S+=1
		for mm in del_c:
			liv_time.append(0)
			container_list.remove(mm)
		for xx in add_c:
			n_container=container(xx[0],xx[1],xx[2],xx[3],s)
			container_list.append(n_container)
		add_c=[]
		del_c=[]
        
		a=list()
		a.append(m)
		a.append(cpu_requested)
		a.append(len(container_list))
		a.append(pc)
		if (calcular_prevision==1):
			previsor.add(cpu_requested)
			aux_prev=float(previsor.calculate())
		else:
			aux_prev=1
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
			container_list.pop()
			container_count-=1

                      
		print ("container count:",container_count)


		a.append(tp)
		if load_balancing_algorithm == 3:
			a.append(cpu_pending_asignation)
		else:  
			a.append(qp)
        
		if pc == 0:
			a.append(100)
		else:
			a.append(tp*100/pc)
            
		a.append(total_x)
        
		a.append(total_d)
        
		a.append(total_s)
        
		a.append(total_S)
        
		if pc == 0:
			n=100
		else:
			n=(cpu_requested)*100/pc
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

		results_list.append(a)
        
    
	print ("writing results in file -... ",file_output_name)
	myfile = io.open(file_output_name, mode='wt', encoding='utf-8')
	for lines in results_list:
		for item in lines:
			myfile.write(u''+str(item)+" ")
		myfile.write(u"\n")
	myfile.close
    
	time_serie = [x[0] for x in results_list]
	request_serie = [x[1] for x in results_list]
	TotalContainer_serie = [x[2] for x in results_list]

	ProcessingCapacity_serie = [x[3] for x in results_list]
	ProcessingCapacityUsed_serie = [x[4] for x in results_list]
	QueueLength = [x[5] for x in results_list]
	PercentProcessingUsed = [x[6] for x in results_list]
	X_serie = [x[7] for x in results_list]
	D_serie = [x[8] for x in results_list]
	s_serie = [x[9] for x in results_list]
	S_serie = [x[10] for x in results_list]
    
	y_cicle = [x[1]*100 for x in results_list]
 
	suma=0
	for i in QueueLength:
		suma=suma+i
	myfileresultado.write(u";" + str(int(suma)/len(QueueLength)))
    
	print ("Cobeats Simulation Ended")     
	print ("")
	print ("")

if __name__ == '__main__':




        
	if single_execution  :
		myfileresultado = io.open('../iofiles/resultadocorto.txt', mode='a', encoding='utf-8')
		run()
	else:    
		myfileresultado = io.open('../iofiles/resultadogrande.txt', mode='a', encoding='utf-8')
		cont=0
		for VarDead in range(5,100,10):
			for VarDeadProvability in range(5,100,10):
				for VarCreate in range(VarDead,100,10):
					for VarCreateProvability in range(5,100,10):
						cont+=1
                   
               
						myfileconf = io.open('cell.cfg', mode='wt', encoding='utf-8')
						myfileconf.write(u'[Cell] \n' +
						'deadprobability = ' + str(VarDeadProvability) + ' \n' +
						'dead_cpu_use = ' + str(VarDead) +' \n'+
						'moveprobability = 10 \n'+
						'vscaprobability = 0 \n'+
						'duplprobability = '+ str(VarCreateProvability) +' \n'+
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



 
