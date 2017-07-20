import matplotlib
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data
from matplotlib.mlab import csv2rec

fname=get_sample_data('C:\\Users\\jhh\\workspace\\prueba2\\src2\\resultadogrande.txt')
total=csv2rec(fname,delimiter=';')


col_print=(0,1,2,3,4,5)
col_label=('%D','pD','%X','pX', 'pc','pt')
  


color=range(255)

s=len(col_print)

fig=plt.figure(1)


matplotlib.rc('xtick',labelsize=6)
matplotlib.rc('ytick',labelsize=6)

axes= [[ False for i in range(s)] for j in range(s) ]

n=1

for j in range(1,s+1):
    #n=1
   
    for i in range(1,s+1):
        #print ('j:',j, ' i:', i,' n:' ,n)
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












    
