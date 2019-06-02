from __future__ import print_function
from scm_cell import scm_cell
#from icm_cell import icm_cell
from com_cell import com_cell
from icm_server import server
#from _overlapped import NULL
import configparser

class container:
    
    total_cicles_request=0
    cell=""
    container_cicles_capacity=0
    internal_code=0
    cpu_used=0.0
    cicles_req=0
    conf=0
    queue=0
    slot_time=0
    min_processing_cicle_capacity=0
    max_processing_cicle_capacity=0
    icm_simulation=0
    icm_size=0
    icm_server=""
    cicles_running=0

    def living_time(self):
        return self.cicles_running
    
    
    def __init__(self,code,min_running,cellconfigfile,initial_queue_len,serv):
        
        self.conf = configparser.ConfigParser()
        self.conf.readfp(open(cellconfigfile))

        self.cicles_req= int (self.conf.get('Container', 'cicles_req'))
        self.slot_time= int (self.conf.get('Container', 'slot_time'))
        self.total_cicles_request=0

        self.icm_simulation=int (self.conf.get('Container', 'icm_simulation'))
        if self.icm_simulation==1:
             ''' is a icm simulation '''
             self.icm_size=int (self.conf.get('Container', 'icm_size'))
             self.icm_server=serv
             self.cell=icm_cell(code,min_running,cellconfigfile,self.icm_server)
        elif self.icm_simulation==100:
             #print("This is a container in a com_cell simulation")	
             self.cell=com_cell(code,min_running,cellconfigfile)
        else:
             ''' scm simulation '''
             #print("This is a container in a scm simulation")
             self.cell=scm_cell(code,min_running,cellconfigfile)

        #Ttaol FLOPS
        self.container_cicles_capacity= int (self.conf.get('Container', 'init_container_cicles_capacity'))
        self.internal_code=code
        
        self.min_processing_cicle_capacity=int (self.conf.get('Container', 'min_scale_limit'))
        self.max_processing_cicle_capacity=int (self.conf.get('Container', 'max_scale_limit'))
     
        self.queue=initial_queue_len
        self.proc_used=0

    
    def processing_capacity(self):
        return self.container_cicles_capacity*self.slot_time/1000  
    
    def processing_used(self):
        return self.proc_used
    def queue_req_pending(self):
        return self.queue
        
    
    def process(self,req):

        self.cicles_running+=1
        self.total_cicles_request+=req
        
        if (self.total_cicles_request<(self.container_cicles_capacity*self.slot_time/1000)):         
            self.cpu_used=int((self.total_cicles_request*100)/(self.container_cicles_capacity*self.slot_time/1000))
            self.proc_used=self.total_cicles_request
            self.total_cicles_request=0
            self.queue=0
    
        else:
            self.proc_used=self.container_cicles_capacity*self.slot_time/1000
            self.cpu_used=100
            self.total_cicles_request-=self.proc_used
            self.queue=self.total_cicles_request

        result, incr, self.container_cicles_capacity,queue_new = self.cell.actuate(self.cpu_used,0,0,self.container_cicles_capacity,self.queue)

        if (result == "X"):
            self.queue=queue_new
        
        
        if (result == "D" and self.icm_simulation==1 ):
            self.icm_server.remove_(self.internal_code)       
        
        return result,queue_new  
    
