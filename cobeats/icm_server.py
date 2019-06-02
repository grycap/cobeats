import configparser
from random import randint
import random
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib
''' This server retur mean value for sel.size right and self.size left, includin node value, for list of nodes 
    it store data in nodes in a list that where add in last position and remove node desired
    list is continuous and next value for last node is first one and previous value for first one is last value 
'''

class Node:
    code=0
    value=0
    def __init__(self,cod,v):
         self.code=cod
         self.value=v
    def set(self,v):
         self.value=v 
    def get_value(self):
         return self.value
    def get_code(self):
         return self.code
    def set_code(self,c):
         self.code=c
    def show(self):
         return self.code
      

class server:
    list_nodes=list()
    size=0
    
    def __init__(self,area):
         self.list_nodes[:] = []
         self.size=area
    def add(self,node):
        for n in self.list_nodes:
            if n.get_code() == node.get_code():
               return False
        self.list_nodes.append(node)
        return True
    def len(self):
       return len(self.list_nodes)
    def remove(self,n):
       self.list_nodes.remove(n)
    def remove_(self,cod):
      # print ("Removing ...", cod)
       aux=0
       for m in self.list_nodes:
           if m.get_code()==cod:
               #print ("For removing",aux)
              # self.list_nodes.remove(aux)
               del self.list_nodes[aux]
               return 1
           else:
               aux+=1
       return None
    def get(self,number):
       return self.list_nodes[number]
    def get_(self,number):
       #print ("Getting --", number)
       for n in self.list_nodes:
           if n.get_code()==number:
                return n
     #  print ("Getting not found")
       return None
    def set_(self,code,value):
        n=self.get_(code)
        if n is not None:
           n.set(value)
           
    def set(self,number,value):
       n=self.list_nodes[number]
       n.set(value)
    def get_pos(self,cod):
       aux=0
       for m in self.list_nodes:
           if m.get_code()==cod:
               return aux
           else:
               aux+=1
       return -1
    def get_zone_value_cod______(self,cod):
        aux=self.get_pos(cod)
        print("Posicion del nodo",aux)
        if aux==-1:
            return 0
        else:
            return self.get_zone_value(aux)
    def get_zone_value(self,v):
          aux=-1
          sum=0
          t=0
          tt=0
          siz=0
          
          if (self.size*2)+1 >= len(self.list_nodes):
                  siz=(len(self.list_nodes)-1)/2
          else:
                  siz=self.size
          #print ("nueva size", siz)
          for n in self.list_nodes:
               aux+=1
               if n.get_code() == v:
                    t=aux+siz+len(self.list_nodes)
                    tt=aux-siz+len(self.list_nodes)
                    break
                   # if tt < 0 :
                   #    tt+=len(self.list_nodes)
                    #print ("Encontrado en posicion ", aux , "mostrar de:" ,t%len(self.list_nodes) , " a ", tt%len(self.list_nodes))
               #print ("[",tt%len(self.list_nodes)," -", aux , " - " ,t%len(self.list_nodes) , " ] ")
          print ("Actuando en :", v ,"en rango[",tt,t,"] - list len:",len(self.list_nodes))
          for d in range (tt%len(self.list_nodes), tt%len(self.list_nodes) + 1 + siz*2):
                r=d%len(self.list_nodes)
                sum+=self.list_nodes[r].get_value()
                print ("pos:",r,"Cod.",self.list_nodes[r].get_code(),"Val.", self.list_nodes[r].get_value(),"Size:",siz,"len:",len(self.list_nodes), "Area:",self.size)
                   
          #print ("suma",sum,sum/len(self.list_nodes), siz) 
         # return sum/len(self.list_nodes)
          return sum/((siz*2)+1)
               
    def show(self):
        print (len(self.list_nodes)) 
        aux=0
        for x in self.list_nodes:
               print ("Pos.",aux," Cod.",x.show(),"-", x.get_value(), "-", x.get_code())
               aux+=1


           




