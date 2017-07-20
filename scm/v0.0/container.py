
from cell import cell
from _overlapped import NULL

class container:
    
    total_requests=0
    cell=NULL
    process_req_capacity=0
    internal_code=0
    cpu_used=0
    
    
    def __init__(self,code,min_running):
        self.total_requests=0
        self.cell=cell(code,min_running)
        self.process_req_capacity=500
        self.internal_code=code
        
    #def actuate(self):
       # return self.cell.actuate()
    
    def processing_capacity(self):
        return self.process_req_capacity  
    
    def processing_used(self):
        return self.cpu_used
    def queue_req_pending(self):
        return self.total_requests
    def process(self,req):
        self.total_requests+=req
        #print ("total_request",self.total_requests)
        if (self.total_requests<=self.process_req_capacity):         
           # print (self.total_requests,"-" , self.process_req_capacity)
            self.cpu_used=self.total_requests*100/self.process_req_capacity
            self.total_requests=0
        #    return_req=0
        else:
            self.cpu_used=100
            self.total_requests-=self.process_req_capacity
        self.cell.set_system_status(self.cpu_used,0,0)
        #print ("cpu_used:", self.cpu_used)
        #print ("total_req_pending",self.total_requests)
        return self.cell.actuate()  
        #    return_req=req-self.process_req_capacity
        #return return_req
    
    