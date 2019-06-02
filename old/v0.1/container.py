
from cell import cell
from _overlapped import NULL
import configparser

class container:
    
    total_cicles_request=0
    cell=NULL
    container_cicles_capacity=0
    internal_code=0
    cpu_used=0
    cicles_req=0
    conf=0
    min_processing_cicle_capacity=0
    min_processing_cicle_capacity=0
    
    
    def __init__(self,code,min_running):
        
        self.conf = configparser.ConfigParser()
        self.conf.readfp(open(r'cell.cfg'))
        self.cicles_req= int (self.conf.get('Container', 'cicles_req'))
        
        
        self.total_cicles_request=0
        self.cell=cell(code,min_running)
        self.container_cicles_capacity= int (self.conf.get('Container', 'init_container_cicles_capacity'))
        self.internal_code=code
        
        self.min_processing_cicle_capacity=int (self.conf.get('Container', 'min_scale_limit'))
        self.max_processing_cicle_capacity=int (self.conf.get('Container', 'max_scale_limit'))

        
        
    #def actuate(self):
        # return self.cell.actuate()
    
    def processing_capacity(self):
        return self.container_cicles_capacity  
    
    def processing_used(self):
        return self.cpu_used
    def queue_req_pending(self):
        return self.total_cicles_request
    def process(self,req):
        
        self.total_cicles_request+=(req*self.cicles_req)
        #print ("total_request",self.total_cicles_request)
        if (self.total_cicles_request<self.container_cicles_capacity):         
            # print (self.total_cicles_request,"-" , self.container_cicles_capacity)
            self.cpu_used=self.total_cicles_request*100/self.container_cicles_capacity
            self.total_cicles_request=0
            #    return_req=0
        else:
            self.cpu_used=100
            self.total_cicles_request-=self.container_cicles_capacity
        
        
        self.cell.set_system_status(self.cpu_used,0,0,self.container_cicles_capacity)
        #print ("cpu_used:", self.cpu_used)
        #print ("total_req_pending",self.total_cicles_request)
        
        result, incr, self.container_cicles_capacity =self.cell.actuate()
        
        #if (result=='s' or result=='S'):    
        #    self.container_cicles_capacity=self.container_cicles_capacity*(incr/100)
        
       
        
        #self.req_capacity=self.cell.get_processing_capacity()
        return result  
    
    
        #    return_req=req-self.container_cicles_capacity
        #return return_req
    
    