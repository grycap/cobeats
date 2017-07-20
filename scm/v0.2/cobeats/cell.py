
#import logging
import configparser
from random import randint


#import psutil
#import ConfigParser
#import sys


class cell:
    internal_code=0        #Unique Code number for cell
    tic=0                  #Total tics or age
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
        # Initialize cell
     
        self.internal_code=code
        self.status=1  
        #print "Inicialize cell ", self.internal_code
        #logging.debug("Initialize", self.internal_code)
        #config = ConfigParser.ConfigParser()
        config = configparser.ConfigParser()
        config.readfp(open(configfile))
        #param1 = config.get('Cell', 'param1')
        #self.minimal_running = int (config.get('Cell', 'minimal_number_running'))
        self.minimal_running = min_running
        #self.maxim_running = int (config.get('Cell', 'max_number_running'))
        #self.max_running=int (config.get('Cell', 'max_number_running'))
        self.pdead = int (config.get('Cell', 'deadprovability'))
        self.dead_cpu_use = int (config.get('Cell', 'dead_cpu_use'))
        
        
        
        
        self.pdupl = int (config.get('Cell', 'duplprovability'))
        self.dupl_cpu_use = int (config.get('Cell', 'dupl_cpu_use'))
        
        self.pmove = int (config.get('Cell', 'moveprovability'))
        self.pscav = int (config.get('Cell', 'vscaprovability'))
        
        self.orig_cell_processing_capacity=int (config.get('Cell', 'init_process_capacity'))
        self.cell_processing_capacity=self.orig_cell_processing_capacity
        
        self.var_processing_capacity=int (config.get('Cell', 'variation_process_capacity'))
        
       
        self.min_processing_cicle_capacity=int (config.get('Container', 'min_scale_limit'))
        self.max_processing_cicle_capacity=int (config.get('Container', 'max_scale_limit'))
       
        self.max_history=int (config.get('Cell', 'max_history'))
        
        #print ("param1", param1)
        #print ("pdead", self.pdead)
        #print(randint(0,99))
    #def run(self):
        #print ("Run cell")
    
    #def get_status(self):
        #return str("ok")
        #print ("-----",self.status)
    #   return self.status
    #def is_alive(self):
    #   return self.status
    def get_processing_capacity(self):
        return self.cell_processing_capacity
    
    
    def print_system_status(self):
        a = "(",self.cpu_use,"-",self.mem_use,"-",self.io_use,")"
        return a
    
    def set_system_status(self,cpu2,mem2,io2,cpc,q):
        #Read system status - get values from system
        self.cpu_use=cpu2
        #self.cpu_use=cpu2*100/self.cell_processing_capacity
        self.mem_use=mem2
        self.io_use=io2
        self.cell_processing_capacity=cpc
        self.queue=q
        #print (self.cpu_use)
        
        #print("cpu_use:",self.cpu_use)
        
        #   def get_system_status(self):
        #      	f = open("system_status.csv","r")
        #     	lines = f.readlines()
        # If we need to read line 33, and assign it to some variable
        #    	x = lines[self.tic]
        #print (x)
        #   	self.cpu_use, self.mem_use, self.io_use = (int(val) for val in x.split())

    
    def actuate(self):
        
        #if (self.queue>0):
        #    print ("Queue:" , self.queue, "processing:",self.cpu_use)
        
        
        self.action='N'
        self.tic=self.tic+1
        #print self.internal_code
        #print "Running Action", self.internal_code
        #logging.debug('Runnig Action ', self.internal_code)
        if (self.status==1):
            #if cell is alive
            
            
            #self.cpu_use=randint(0,100)  
            #self.mem_use=randint(0,100)
            #self.io_use=randint(0,100)
            ##self.get_system_status()
            #processing_increase=0
            #Acciones dead
            #print (self.internal_code,"-",self.pdead, " scpuuse:",self.cpu_use, "deadcpuuse:",self.dead_cpu_use, float(self.cpu_use) < float(self.dead_cpu_use))
            if (self.queue > 10000000000000000000000 ):
                #if (self.cell_processing_capacity >= self.max_processing_cicle_capacity * 2):
                #if self.cell_processing_capacity>=self.max_processing_cicle_capacity:
                #if (randint(0,99) < self.pdupl):
                    self.action="XS"
                    self.cell_processing_capacity+=self.cell_processing_capacity*self.var_processing_capacity/100
                #else:
                #    self.action="XS"
                #    self.cell_processing_capacity+=self.cell_processing_capacity*self.var_processing_capacity/100
                    
            else:
                #ACTION DEAD
                if (randint(0,99) < self.pdead) and (float(self.cpu_use) < float(self.dead_cpu_use)) :
                    if self.internal_code >  self.minimal_running :
                        self.status=0
                        self.action='D'
                        #self.cell_processing_capacity=0
                
                #ACTION DUPLICATE        
                elif (randint(0,99) < self.pdupl) and (self.cpu_use > self.dupl_cpu_use):
                    #if self.internal_code > self.maxim_running: 
                        #Acciones duplicate
                        self.action='X'
                        #self.cell_processing_capacity=self.orig_cell_processing_capacity
                
                
                #ACTION VERTICAL SCALING        
                elif (randint(0,99) < self.pscav and self.cpu_use <= self.dupl_cpu_use and self.cpu_use >= self.dead_cpu_use):
                    
                    #ACTION vertical INCREASE
                    if (self.previous_cpu_use < self.cpu_use):
                        self.action='S'
                        
                        self.cell_processing_capacity+=self.cell_processing_capacity*self.var_processing_capacity/100
                        if self.cell_processing_capacity>=self.max_processing_cicle_capacity:
                            self.action="X"
                            #if (self.queue<=0):
                            #     self.cell_processing_capacity=self.orig_cell_processing_capacity
                            
        
                        
                        #self.processing_increase=1+self.var_processing_capacity
                        #if (self.cell_processing_capacity>100):
                        #    self.cell_processing_capacity=100
                        
                    #ACTION vertical DECREASE
                    else:
                        self.action='s'
                        self.cell_processing_capacity-=self.cell_processing_capacity*self.var_processing_capacity/100
                        #self.processing_increase = 1-self.var_processing_capacity
                        if (self.cell_processing_capacity<=self.min_processing_cicle_capacity):
                            #self.cell_processing_capacity=0
                            self.status=0
                            self.action="D"
    
                elif (False):
                    #ACTION MOVE
                    self.action='M'
                else:
                    #NO ACTION
                    self.action='N'
        else:
            #print ("Is dead")
            self.action='N'
            
        #save history use
        self.previous_cpu_use=self.cpu_use
        self.history.append(self.cpu_use)
        if len(self.history)>self.max_history:
            self.history.pop(0)
            
        #return str(self.action),self.processing_increase,self.cell_processing_capacity
        return str(self.action),0,self.cell_processing_capacity



