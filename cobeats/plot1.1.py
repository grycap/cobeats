#!/usr/bin/env python

import csv
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.cbook import get_sample_data
from matplotlib.mlab import csv2rec
import sys
from dtw import DTW
import numpy as np
#from sklearn.metrics import mean_absolute_error
#from sklearn.metrics import mean_squared_error
from sklearn import metrics

'''
def mae(pred_list, true_list):
    if len(pred_list) != len(true_list):
        raise Exception('Error: number of elements not match!')
    return sum(map(lambda t:float(t[0]-t[1]),zip(pred_list, true_list)))/len(true_list)
'''

def rmse(predictions, targets):
    differences = predictions - targets                       #the DIFFERENCEs.
    differences_squared = differences ** 2                    #the SQUAREs of ^
    mean_of_differences_squared = differences_squared.mean()  #the MEAN of ^
    rmse_val = np.sqrt(mean_of_differences_squared)           #ROOT of ^
    return rmse_val                                           #get the ^

if (len(sys.argv) < 3):
	print ("Run : %d" % len(sys.argv))
	print ("sample : %s file_name show_images" % sys.argv[0])
	print ("sample : %s ../iofiles/resultado2.txt 1" % sys.argv[0])
	quit()

file_name=sys.argv[1]

print (sys.maxsize)
print ("================================================================")
print ("----------------------COBEATS v0.2------------------------------")
print ("-----  COntainers Bio-inspired Enhanced AuToscaling System -----")
print ("----------------------- Analizer  ------------------------------")
print ("================================================================")



print ("Analizing file                          : %s" % file_name)

show_images=float(sys.argv[2])
print ("Show images                             : %s" % show_images)

with open(file_name) as f:
        
	reader=csv.reader(f,delimiter=' ',quoting=csv.QUOTE_NONE)
    #time_serie=list()
    #request_serie=list()
	list_csv=list(reader)
	print ("Total lines readed                      : %d " %(len(list_csv) ))
    #for row in reader:
        #print row[2]
        #time_serie.append(row[0])
        #request_serie.append(row[1])


#print (a)

#Remove virt line
list_csv.pop(0)

time_serie=[x[0] for x in list_csv]
request_serie=[x[1] for x in list_csv]
totalContainer_serie = [x[2] for x in list_csv]
ProcessingCapacity_serie = [x[3] for x in list_csv]
ProcessingCapacityUsed_serie = [x[4] for x in list_csv]
QueueLength = [x[5] for x in list_csv]
PercentProcessingUsed = [x[6] for x in list_csv]
X_serie = [x[7] for x in list_csv]
D_serie = [x[8] for x in list_csv]
s_serie = [x[9] for x in list_csv]
S_serie = [x[10] for x in list_csv]
z9 = [x[11] for x in list_csv]
liv_time_max = [int(x[12]) for x in list_csv]
liv_time_min = [x[13] for x in list_csv]
liv_time_sum = [x[14] for x in list_csv]



sum_total_containers=0
for i in totalContainer_serie:
    sum_total_containers+=int(i)

sum_q=0.0
for i in QueueLength:
    #sum_q+=int(i)
	sum_q+=float(i)
  

#print (time_serie)

if show_images==1:
	plt.figure(1)

	plt.subplot(211)
	AAA=[float(p) for p in request_serie]
	TTT=[float(p) for p in time_serie]
	#plt.plot(time_serie,request_serie)
	plt.plot(TTT,AAA)
	plt.legend(['Requests'])
	plt.xlabel('Time --->')
	plt.ylabel('FLOPS requested --->')
	plt.subplot(212)
	BBB=[float(p) for p in totalContainer_serie]
	#plt.plot(time_serie,totalContainer_serie)
	plt.plot(TTT,BBB)
	plt.xlabel('Time --->')
	plt.ylabel('#Containers or Decisions --->')
	#plt.plot(time_serie,X_serie)
	#plt.plot(time_serie,D_serie)
	#plt.plot(time_serie,s_serie)
	#plt.plot(time_serie,S_serie)
	#SXX=[float(p) for p in X_serie]
	#SDD=[float(p) for p in D_serie]
	#Sss=[float(p) for p in s_serie]
	#SSS=[float(p) for p in S_serie]
	#plt.plot(TTT,SXX)
#	plt.plot(TTT,SDD)
#	plt.plot(TTT,Sss)
#	plt.plot(TTT,SSS)
	plt.legend(['Containers','X Dec.','D Dec.','s Dec.','S Dec.'])
#	plt.show()
	plt.figure(3)
     #plt.bar(time_serie, X_serie ,width=0.9,color='b',align='center')
	plt.xlabel('Time --->')
	plt.ylabel('# Decisions --->')
	XS=[float(p) for p in X_serie]
	DS=[float(p) for p in D_serie]
	sS=[float(p) for p in s_serie]
	SS=[float(p) for p in S_serie]
	#plt.bar([float(p) for p in time_serie], X_serie ,width=0.9,color='b',align='center')
	w=0.25
	ind = np.arange(len(TTT))
	plt.bar(ind-w*2,XS,width=w,color='b',align='center')
	plt.bar(ind-w,DS,width=w,color='r',align='center')
	#plt.bar(TTT,DS,width=w,color='g',align='center',stacked=False)
	#plt.bar(TTT,sS,width=w,color='r',align='center',stacked=False)
	#plt.bar(TTT,SS,width=0.9,color='y',align='center')
	#plt.bar(TTT,DS,width=0.9,color='g',align='center')
	plt.bar(ind+w,sS,width=w,color='g',align='center')
	plt.bar(ind+w*2,SS,width=w,color='y',align='center')
	plt.legend(['X Dec.','D Dec.', 's Dec.', 'S Dec.'])
	print ("Container peak                          : %d"% int(max(BBB)))
	print ("X Peak                                  : %d" % int(max(XS)))
	print ("D Peak                                  : %d" % int(max(DS)))
	print ("S Peak                                  : %d" % int(max(SS)))
	print ("s Peak                                  : %d" % int(max(sS)))
	print ("Live Time max                           : %d "% max(liv_time_max))
	print ("Live Time min                           : %d "% min(liv_time_max))
	print ("Live Time sum                           : %d "% sum(liv_time_max))
	print ("Live Time mean                          : %f "% np.mean(liv_time_max))
	print ("Max and Mean values for X action serie  : %d - %f"% (int(max(XS)),np.mean(XS)))
	print ("Max and Mean values for D action serie  : %d - %f"% (int(max(DS)),np.mean(DS)))
	print ("Max and Mean values for S action serie  : %d - %f"% (int(max(SS)),np.mean(SS)))
	print ("Max and Mean values for s action serie  : %d - %f"% (int(max(sS)),np.mean(sS)))
'''

	plt.figure(2)

	plt.subplot(211)
	plt.xlabel('Time --->')
	plt.ylabel('FLOPS --->')
	PC=[float(p) for p in ProcessingCapacity_serie]
	#plt.plot(time_serie,ProcessingCapacity_serie)
	plt.plot(TTT,PC)
	PCU=[float(p) for p in ProcessingCapacityUsed_serie]
	#plt.plot(time_serie,ProcessingCapacityUsed_serie)
	plt.plot(TTT,PCU)
	QL=[float(p) for p in QueueLength]
	#plt.plot(time_serie,QueueLength)
	plt.plot(TTT,QL)
	plt.legend(['Tot.ProcessingCapacity','Tot.ProcessingCapacity_used','QueueLength'])
	plt.subplot(212)
	plt.xlabel('Time --->')
	plt.ylabel('Ratio --->')
	#plt.plot(time_serie,PercentProcessingUsed)
#	plt.plot(time_serie,z9)
	PPU=[float(p) for p in PercentProcessingUsed]
	plt.plot(TTT,PPU)
	#Z9=[float(p) for p in z9]
	plt.plot(TTT,z9)
	#plt.plot(TTT,Z9)
	plt.legend(['%TotalCapacityUsed', '%requested processed'])
'''


#type(request_serie)
#A = request_serie.astype(np.float)
#A = np.array(request_serie, dtype=np.float16)
#B = np.array(ProcessingCapacity_serie, dtype=np.float16)
A=[float(p) for p in request_serie]
B=[float(p) for p in ProcessingCapacity_serie]
cost, path = DTW(A, B, window = 4)
temp=cost/(len(list_csv))
#print 'Total Distance is              :', cost,' (',cost/1000000,' MFLOPS) - (', cost/1000000000, 'GFLOPS)'
print ('Total DTW Distance is                   : %f ( %f MFLOPS)(  %f GFLOPS)'% (cost,cost/1000000,cost/1000000))
#print 'Mean Distance                  :', temp,' (',temp/1000000 ,' MFLOPS) - (', temp/1000000000, ' GFLOPS)'
print ('Mean DTW Distance                       : %f ( %f MFLOPS) - ( %f GFLOPS)' %(temp,temp/1000000,temp/1000000000))
print ('Sum Total Processing Containers in sim  : %f' %( sum_total_containers))
temp=cost/sum_total_containers
#print 'Mean Distance total/Container  :', temp, ' (', temp /1000000 ,' MFLOPS) -(', temp /1000000000 , ' GFLOPS)'
print ('Mean Distance total/Container           : %f (%f MFLOPS) (%f GFLOPS)' % (temp, temp/1000000,temp/1000000000))
#print ('Mean Distance total/Container  : %d  ( %d MFLOPS) -( %d GFLOPS)' %(f,f/1000000,f/1000000000))
#print ('Distancia %d' % temp)
#aux=f
#print ('Mean Distance total/Container  : %f  ( %f MFLOPS) -( %f GFLOPS)' %(tempaux,aux/1000000,aux/1000000000))
#print 'Total Queue                    :', sum_q,' (', sum_q/1000000 ,' MFLOPS) -(', sum_q/1000000000 , ' GFLOPS)'
#print 'Total Queue                    :','{:15.2f}'.format(round(sum_q,3)),' (', sum_q/1000000  ,'  MFLOPS) -(',sum_q/1000000000, ' GFLOPS)'
print ('Total Queue                             : %d (%f MFLOPS) -(%f GFLOPS)' %(sum_q,sum_q/1000000,sum_q/1000000000))

print ("--------------------------------------------")
rs=[float(x[1]) for x in list_csv]
tcs = [float(x[3]) for x in list_csv]
#print ("RMSE:::",metrics.mean_squared_error(rs,tcs))
print ("Mean Absolute Error (MAE)               :",metrics.mean_absolute_error(rs,tcs),metrics.mean_absolute_error(rs,rs))
#print ("MEI                                     :")
print ("RMSE                                    :",np.sqrt(metrics.mean_squared_error(rs,tcs)),np.sqrt(metrics.mean_squared_error(rs,rs)))
#y_true, y_pred = check_arrays(rs, tcs)
#print ("MAPE:", np.mean(np.abs((y_true - y_pred) / y_true)) * 100)
print ("MSE(Mean Square Error - Mayor mas error):",metrics.mean_squared_error(rs,tcs),metrics.mean_squared_error(rs,rs))
#print ("MAPE:",metrics.mean_absolute_percentage_error(rs,tcs)) 

print ("EVS(Variance regression score)          :",metrics.explained_variance_score(rs, tcs), metrics.explained_variance_score(rs, rs))
print ("R2S(coefficient of determinacion  best1):",metrics.r2_score(rs,tcs),metrics.r2_score(rs,rs))
#print ("BAS(Balanced Accuracy score):",metrics.balanced_accuracy_score(rs,tcs))
print ("Max min values for Requested            :", max(rs), min(rs))
print ("Max min values for Processing Capacity  :", max(tcs), min(tcs))
print ("Dif Max and min                         :",max(tcs)-max(rs), min(tcs)-min(rs))




if show_images==1:
	plt.figure(4)
	import matplotlib.pyplot as plt
	offset = 0
	plt.xlim([-1, max(len(A), len(B)) + 1])
	plt.plot(A)
	plt.plot(B)
      #plt.plot(B + offset)
	for (x1, x2) in path:
		plt.plot([x1, x2], [A[x1], B[x2] + offset])
           #plt.show()
	plt.show()
'''
print(max(request_serie))
print(min(request_serie))
print(sum(rs))
print (sum(tcs))
print (len(list_csv))
print ("MAE:",(sum(rs)-sum(tcs))/len(list_csv))
print ("MAE::",mean_absolute_error(rs,tcs))
#print ("RMSE:",rmse(rs,tcs))
#print ("RMSE::",mean_squared_error(rs,tcs))
'''


#print(sum(request_serie))

#dtw.dtw_show([float(p) for p in request_serie],[float(p) for p in ProcessingCapacity_serie])



#fname=get_sample_data('..\iofiles\resultado.txt')
#total=csv2rec(fname,delimiter=' ')

#print (len(reader))

