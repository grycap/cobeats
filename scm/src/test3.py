#!/usr/bin/env python





from cell import cell
import logging
import time

import sys





from numpy import *
import matplotlib.pyplot as plt
#x = range(0.,10.,0.1)
#y = sin(x)
#ll = plt.plot(x,y)
#plt.show()




#x = arange(0.,10,0.1)
#a = cos(x)
#b = sin(x)
#c = exp(x/10)
#d = exp(-x/10)
#la = plt.plot(x,a,'b-',label='cosine')
#lb = plt.plot(x,b,'r--',label='sine')
#lc = plt.plot(x,c,'gx',label='exp(+x)')
#ld = plt.plot(x,d,'y-', linewidth = 5,label='exp(-x)')
#ll = plt.legend(loc='upper left')
#lx = plt.xlabel('xaxis')
#ly = plt.ylabel('yaxis')
#plt.show()












logging.basicConfig( level=logging.DEBUG,format='[%(levelname)s] - %(threadName)-10s : %(message)s')

cell_list=list()
request_list=list()
values_list=list()
cell_counter=1
#for x in xrange(0, 50):
for x in range(0,10):
    x=cell(cell_counter)
	#lista.append(x)
    cell_list.append(x)
    cell_counter=cell_counter+1

iter=int(0)


#for m in xrange(0,47):
for m in range(0,152):
    time.sleep(0.01)
    cont=0
    iter=iter+1
    pc=0
    
    f = open("system_status.csv","r")
    lines = f.readlines()
    # If we need to read line 33, and assign it to some variable
    linea_leida = lines[int(iter)]
    #print (x)
    cpu1, mem1, io1 = (int(val) for val in linea_leida.split())
    
    cpu_corregido=cpu1*100/len(cell_list)
    
    for x in cell_list :
        cont=cont+1
		#print ('si')
		
		#print (x.get_status())
		##action=''
        if (x.is_alive()==1):
           
            #request_list.append(cpu1) 
            
            #x.set_system_status(cpu1,mem1,io1)
            x.set_system_status(cpu_corregido,mem1,io1)
            pc+=x.get_processing_capacity()
            acti=x.actuate()
            #sys.stdout.write(acti)
            print (acti, end='')
            if (acti == 'X'):
                x=cell(cell_counter)
                cell_counter=cell_counter+1
                cell_list.append(x)
            if (acti == 'D'):
                cell_list.remove(x) 
                #sys.stdout.write('o')
                #else:
                #sys.stdout.write('x')
                ##sys.stdout.write('o')
             
    print ("-Iter:", iter, ">cells:", len(cell_list),">", int(cpu1*100/len(cell_list)), ">" , pc )
    #values_list.append(iter)
    a=list()
    a.append(iter)
    a.append(cpu1*100/len(cell_list))
    a.append(pc)
    a.append(cpu1)
    a.append(len(cell_list))
    a.append(pc/100)
    #a.append(0)
    #print (a)
    request_list.append(a)
    
    #request_list2= 5*[2*[0]]
#for i in request_list:
#    print (i)


#print(values_list)

#x = [1,2,3]
#y = [[1,2,3],[4,5,6],[7,8,9]]
plt.xlabel("Iteraction")
plt.ylabel("Y-axis")
plt.title("A test graph")
#for i in range(len(y)):
#    plt.plot(x,[pt[i] for pt in y],label = 'id %s'%i)
#y=request_list(x)
x = [x[0] for x in request_list]
y = [x[1] for x in request_list]
z = [x[2] for x in request_list]
z1 = [x[3] for x in request_list]
z2 = [x[4] for x in request_list]
z3 = [x[5] for x in request_list]
#testList2 = [(elem1, log) for elem1, elem2 in request_list]

#for i in request_list:
     #plt.plot(values_list,i)
#plt.plot( request_list[:] )
#plt.legend()
plt.figure(1)
plt.subplot(311)
plt.plot(x,y)
plt.legend(['cpu1*100/len(cell_list)'])
plt.xlabel("Iteraction")
plt.subplot(312)
plt.plot(x,z)
plt.legend(['pc'])
plt.subplot(313)
plt.plot(x,z1)
plt.plot(x,z2)
plt.plot(x,z3)
plt.legend(['cpu1','Total cells','pC/100'])
#print ("----->", request_list[1])
plt.show()


