

import matplotlib.pyplot as plt
#from pandas.tools.plotting import scatter_matrix
#import pandas as panda

f=open('./resultadogrande.txt')
LDead=list()
PDead=list()
LCreate=list()
PCreate=list()
Value=list()
Qsize=list()
for l in f.readlines():
    #print (l.strip().split(';'))
    a=l.strip().split(';')
    LDead.append(a[0])
    PDead.append(a[1])
    LCreate.append(a[2])
    PCreate.append(a[3])
    try:
       Value.append(float(a[4]))
    except :
       Value.append(0)
       
    try:
       Qsize.append(float(a[5]))
    except :
       Qsize.append(0)
     

  
f.close()
color=range(255)
#plt.figure(1)

fig,axes=plt.subplots(6,6)



axes[0,0].scatter(LDead,LDead,c='blue',s=0.1)
axes[0,1].scatter(LDead,PDead,c='blue',s=0.1)
axes[0,2].scatter(LDead,LCreate,c='blue',s=0.1)
axes[0,3].scatter(LDead,PCreate,c='blue',s=0.1)
axes[0,4].scatter(LDead,Value,c='blue',s=0.1)
axes[0,5].scatter(LDead,Qsize,c='blue',s=0.1)

axes[1,0].scatter(PDead,LDead,c='blue',s=0.1)
axes[1,1].scatter(PDead,PDead,c='blue',s=0.1)
axes[1,2].scatter(PDead,LCreate,c='blue',s=0.1)
axes[1,3].scatter(PDead,PCreate,c='blue',s=0.1)
axes[1,4].scatter(PDead,Value,c='blue',s=0.1)
axes[1,5].scatter(PDead,Qsize,c='blue',s=0.1)

axes[2,0].scatter(LCreate,LDead,c='blue',s=0.1)
axes[2,1].scatter(LCreate,PDead,c='blue',s=0.1)
axes[2,2].scatter(LCreate,LCreate,c='blue',s=0.1)
axes[2,3].scatter(LCreate,PCreate,c='blue',s=0.1)
axes[2,4].scatter(LCreate,Value,c='blue',s=0.1)
axes[2,5].scatter(LCreate,Qsize,c='blue',s=0.1)

axes[3,0].scatter(PCreate,LDead,c='blue',s=0.1)
axes[3,1].scatter(PCreate,PDead,c='blue',s=0.1)
axes[3,2].scatter(PCreate,LCreate,c='blue',s=0.1)
axes[3,3].scatter(PCreate,PCreate,c='blue',s=0.1)
axes[3,4].scatter(PCreate,Value,c='blue',s=0.1)
axes[3,5].scatter(PCreate,Qsize,c='blue',s=0.1)

axes[4,0].scatter(Value,LDead,c='blue',s=0.1)
axes[4,1].scatter(Value,PDead,c='blue',s=0.1)
axes[4,2].scatter(Value,LCreate,c='blue',s=0.1)
axes[4,3].scatter(Value,PCreate,c='blue',s=0.1)
axes[4,4].scatter(Value,Value,c='blue',s=0.1)
axes[4,5].scatter(Value,Qsize,c='blue',s=0.1)

axes[5,0].scatter(Qsize,LDead,c='blue',s=0.1)
axes[5,1].scatter(Qsize,PDead,c='blue',s=0.1)
axes[5,2].scatter(Qsize,LCreate,c='blue',s=0.1)
axes[5,3].scatter(Qsize,PCreate,c='blue',s=0.1)
axes[5,4].scatter(Qsize,Value,c='blue',s=0.1)
axes[5,5].scatter(Qsize,Qsize,c='blue',s=0.1)







plt.show()








    
