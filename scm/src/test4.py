#!/usr/bin/env python




#from numpy import *
import matplotlib.pyplot as plt
from container import container
#import time
import time
import configparser




container_list=list()
results_list=list()

container_count=0
file_name="system_status.csv"



conf = configparser.ConfigParser()
conf.readfp(open(r'simulation.cfg'))
minimun_cells= int (conf.get('Simulation', 'minimun_cells_running'))

#Initialize seed containers 
for x in range(0,minimun_cells):
    container_count+=1
    m=container(container_count,minimun_cells)
    container_list.append(m)
    

num_lines = sum(1 for line in open(file_name))

for m in range(0,num_lines):
    #time.sleep(0.01)
   
    
    f = open(file_name,"r")
    lines = f.readlines()
    # If we need to read line 33, and assign it to some variable
    linea_leida = lines[int(m)]
    
    cpu1, mem1, io1 = (int(val) for val in linea_leida.split())
    
    
    
    
    
    #cpu_corregido=cpu1*100/len(cell_list)
    pc=0  #processing capacity
    tp=0  #processing used
    qp=0  #requests pending
    total_x=0
    total_d=0
    total_n=0
    total_s=0
    total_S=0
    cpu_read=cpu1
    cpu1=cpu1*100
    
    
    reparto=int(cpu1/len(container_list))
    #print ("cpu1",cpu1) o
    #print ("reparto:",reparto)
    for mm in container_list:
        acti=mm.process(reparto)
        #print (cpu1)
        #acti=mm.actuate()
        tp+=mm.processing_used()*mm.processing_capacity()/100
        pc+=mm.processing_capacity()
        qp+=mm.queue_req_pending()
        print (acti, end='')
        if (acti == 'X'):
            n_container=container(container_count,minimun_cells)
            container_count=container_count+1
            container_list.append(n_container)
            total_x+=1
        if (acti == 'D'):
            container_list.remove(mm)
            total_d+=1
        if (acti == 's'):
            total_s+=1
        if (acti == 'S'):
            total_S+=1
             
    print ("-Iter:", m, "req:",cpu1," >cells:", len(container_list),">", int(cpu1*100/len(container_list)), ">pc:",pc," tc:",tp )
    #values_list.append(iter)
    a=list()
    a.append(m)
    a.append(cpu_read)
    a.append(len(container_list))
    a.append(pc)
    a.append(tp)
    a.append(qp)
    a.append(tp*100/pc)
    a.append(total_x)
    a.append(total_d)
    a.append(total_s)
    a.append(total_S)
    #a.append(0)
    #print (a)
    results_list.append(a)
    
    
myfile = open('resultado.txt', mode='wt', encoding='utf-8')
for lines in results_list:
    for item in lines:
        myfile.write(str(item)+" ")
    myfile.write("\n")
myfile.close
    
    
plt.xlabel("Iteraction")
plt.ylabel("Y-axis")
plt.title("A test graph")
x = [x[0] for x in results_list]
y = [x[1] for x in results_list]
z = [x[2] for x in results_list]
z1 = [x[3] for x in results_list]
z2 = [x[4] for x in results_list]
z3 = [x[5] for x in results_list]
z4 = [x[6] for x in results_list]
z5 = [x[7] for x in results_list]
z6 = [x[8] for x in results_list]
z7 = [x[9] for x in results_list]
z8 = [x[10] for x in results_list]


plt.figure(1)
plt.subplot(211)
plt.plot(x,y)
plt.legend(['requests'])
plt.xlabel("Iteraction")
plt.subplot(212)
plt.plot(x,z)
plt.plot(x,z5)
plt.plot(x,z6)
plt.plot(x,z7)
plt.plot(x,z8)
plt.legend(['Containers','X','D','s','S'])
plt.figure(2)
plt.subplot(211)
plt.plot(x,z1)
plt.plot(x,z2)
plt.plot(x,z3)
plt.legend(['pc','tp','qp'])
plt.subplot(212)
plt.plot(x,z4)
#plt.plot(x,z5)
#plt.plot(x,z6)
#plt.plot(x,z7)
#plt.plot(x,z8)
plt.legend(['% pc tp'])
#print ("----->", request_list[1])
plt.figure(3)

plt.bar([p for p in x], z5,width=0.9,color='b',align='center')
plt.bar([p for p in x], z6,width=0.9,color='g',align='center')
plt.bar([p for p in x], z7,width=0.9,color='r',align='center')
plt.bar([p for p in x], z8,width=0.9,color='y',align='center')

plt.show()


