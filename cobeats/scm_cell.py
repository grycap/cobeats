
import configparser
from random import randint

''' This cell use shelf information to take decision. Using especially cpu use
    NO information from other nodes are used.
'''

class scm_cell:
    internal_code=0        #Unique Code number for cell
    #tic=0                  #Total tics or age
    status=1	           #1- alive  0-dead
    
    pdead=0                #dead provability
    pdupl=0                #duplication provability
    pmove=0                #move provability
    pscav=0                #scale provability
    
    action='N'	           #Result action N-None X-Duplicate D-Dead R-resize Up  r-Resize Down M-Move
    
    cpu_use=0              #System cpu use real value
    mem_use=0              #System mem use real use
    io_use=0               #System io use real use
    
    minimal_running=0      #Min number of cell alive
    maxim_running=0        #Max number of cell alive
    
    dead_cpu_use=0         #maximal cpu use to dead
    dupl_cpu_use=0         #minimal cpu use to duplicate
    
    previous_cpu_use=0    #previous cpu use
    
    cell_processing_capacity=0      #ej. MIPS
    orig_cell_processing_capacity=0
    var_processing_capacity=0       #variation processing capacity
    #processing_increase=0
    history=list()
    
    min_processing_cicle_capacity=0
    max_processing_cicle_capacity=0
    
    max_history=0
    queue=0
    
    
    
    def __init__(self, code, min_running,configfile):
        '''# Initialize cell '''
     
        self.internal_code=code
        self.status=1  
        config = configparser.ConfigParser()
        config.readfp(open(configfile))
        self.minimal_running = min_running
        self.pdead = int (config.get('Cell', 'deadprovability'))
        self.dead_cpu_use = int (config.get('Cell', 'dead_cpu_use'))
        
        
        
        
        self.pdupl = int (config.get('Cell', 'duplprovability'))

        self.dupl_cpu_use = int (config.get('Cell', 'dupl_cpu_use'))
        
        self.pmove = int (config.get('Cell', 'moveprovability'))
        self.pscav = int (config.get('Cell', 'vscaprovability'))
        
        self.orig_cell_processing_capacity=int (config.get ('Container', 'init_container_cicles_capacity'))
        self.cell_processing_capacity=self.orig_cell_processing_capacity
        
        self.var_processing_capacity=int (config.get('Cell', 'variation_process_capacity'))
        
       
        self.min_processing_cicle_capacity=int (config.get('Container', 'min_scale_limit'))
        self.max_processing_cicle_capacity=int (config.get('Container', 'max_scale_limit'))
       
        self.max_history=int (config.get('Cell', 'max_history'))
        self.xaction = int (config.get('Cell', 'X_total_containers'))
        
    def get_processing_capacity(self):
        return self.cell_processing_capacity
    
    
    def print_system_status(self):
        a = "(",self.cpu_use,"-",self.mem_use,"-",self.io_use,")"
        return a
    
    def actuate(self,xcpu_use,xmem_use,xio_use,cell_capacity,q_size):
   
        """Read system status - get values from system"""
        self.cpu_use=xcpu_use
        self.mem_use=xmem_use
        self.io_use=xio_use
        self.cell_processing_capacity=cell_capacity
        self.queue=q_size
    
        self.action='N'

        if (self.status==1):
            '''#if cell is alive'''
            if (randint(0,99) < self.pdead) and (float(self.cpu_use) <= float(self.dead_cpu_use)) :
                 '''#ACTION DEAD - HORIZONTAL SCALING'''
                 if self.internal_code >  self.minimal_running :
                      ''' only dead if is total cell is miminal running'''
                      self.status=0
                      self.action='D'
                
            elif (randint(0,99) < self.pdupl) and (self.cpu_use >= self.dupl_cpu_use):
                 '''#ACTION DUPLICATE - HORIZONTAL SCALING'''        
                 self.action='X'
                
            elif (randint(0,99) < self.pscav and self.cpu_use < self.dupl_cpu_use and self.cpu_use > self.dead_cpu_use):
                 '''#ACTION VERTICAL SCALING '''       
                    
                 if (self.previous_cpu_use < self.cpu_use):
                       '''#ACTION vertical INCREASE'''
                       if self.cell_processing_capacity+(self.cell_processing_capacity*self.var_processing_capacity/100)>=self.max_processing_cicle_capacity:
                            self.action="X"
                       else:
                            self.action='S'
                            self.cell_processing_capacity+=self.cell_processing_capacity*self.var_processing_capacity/100
        
                 else:
                       '''#ACTION vertical DECREASE'''
                       self.action='s'
                       self.cell_processing_capacity-=self.cell_processing_capacity*self.var_processing_capacity/100
                       if (self.cell_processing_capacity<=self.min_processing_cicle_capacity):
                            self.status=0
                            self.action="D"
    
            elif (False):
                 '''#ACTION MOVE'''
                 self.action='M'
            else:
                 '''#NO ACTION'''
                 self.action='N'
            

        #save history use
        self.previous_cpu_use=self.cpu_use
        self.history.append(self.cpu_use)
        if len(self.history)>self.max_history:
            self.history.pop(0)
            
        if (self.action=="X"):
             new_queue=self.queue/self.xaction  
        else:
             new_queue=0

        return str(self.action),0,self.cell_processing_capacity,new_queue



