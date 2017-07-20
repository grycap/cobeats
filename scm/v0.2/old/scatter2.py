

import matplotlib.pyplot as plt
#import numpy as np
#from pandas.tools.plotting import scatter_matrix
#import pandas as panda









f=open('./resultadogrande.txt')
LDead=list()
PDead=list()
LCreate=list()
PCreate=list()
Value=list()
Qsize=list()
total=list()

for l in f.readlines():
    #print (l.strip().split(';'))
    a=l.strip().split(';')
    '''
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
   '''
    
    a[5]=float(a[5])
    a[4]=float(a[4])
    
    total.append(a)



  
f.close()



col_print=(0,1,2,3,4,5)
col_label=('%D','pD','%X','pX', 'pc','pt')
  


color=range(255)
#plt.figure(1)
#s=len(total[1])

s=len(col_print)

#fig=plt.figure(figsize=(s,s))
fig=plt.figure(1)




axes= [[ False for i in range(s)] for j in range(s) ]

n=1

for j in range(1,s+1):
    #n=1
   
    for i in range(1,s+1):
        print ('j:',j, ' i:', i,' n:' ,n)
        ax=fig.add_subplot(s,s,n)
        if ( i != j ):
            ax.scatter([x[col_print[j-1]] for x in total],[x[col_print[i-1]] for x in total],s=0.1)
        #ax.set_xlabel('holax') 
        #ax.set_ylabel('holay')
        else:
            #print ("iguales")
            #st=str(j)+'-'+str(i)
            ax.text(0.5,0.5,col_label[i-1])
            
        #if j <= s    :   
            #ax.xaxis.set_visible(False)
            #if i == s   :   ax.yaxix.set_visible(False)
        
        #if i==1 and j==1:
            #ax.legend(loc=2,title='XXXXXXXXXXXXXXXx')
       # print (i,'-',j)
        axes[j-1][i-1] = ax
        
    
        n+=1
        
        
        
plt.subplots_adjust(left=0.1,right=0.85,top=0.85,bottom=0.1)



plt.show()












    
