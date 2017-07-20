
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data
from matplotlib.mlab import csv2rec

fname=get_sample_data('C:\\Users\\jhh\\workspace\\prueba2\\src2\\resultado.txt')
total=csv2rec(fname,delimiter=' ')

print(len(total))

plt.figure(1)
plt.subplot(211)
plt.plot([x[0] for x in total],[x[1] for x in total])

plt.subplot(212)
plt.plot([x[0] for x in total],[x[2] for x in total])


plt.figure(2)
plt.subplot(211)
plt.plot([x[0] for x in total],[x[3] for x in total])
plt.plot([x[0] for x in total],[x[4] for x in total])

plt.subplot(212)
plt.plot([x[0] for x in total],[x[5] for x in total])

plt.figure(3)
plt.subplot(211)
plt.plot([x[0] for x in total],[x[6] for x in total])
plt.plot([x[0] for x in total],[x[7] for x in total])

plt.subplot(212)
plt.plot([x[0] for x in total],[x[8] for x in total])
plt.plot([x[0] for x in total],[x[9] for x in total])

#plt.figure(2)
#plt.subplot(111)
#plt.plot(range(0,len(total)),[x[5] for x in total])


plt.show()




    
