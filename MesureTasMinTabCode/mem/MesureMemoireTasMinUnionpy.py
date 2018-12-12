#pip install -U memory_profiler
 
import TasMinTabCle
import cle
import os
from memory_profiler import profile
import sys
 
@profile
def mes(a,param):
    for i in range(1,len(param)):
        b = TasMinTabCle.TasMinTab()
        b.Ajout(param[i])  #Initialisation (temps negligeable)
        a.Union(b) 
    
def mesureUnion(allFiles):
    allFiles.sort()
    for x in allFiles:
        print(x)
        param = list()
        f = open("cles_alea/"+x,'r')
        for line in f:
            param.append(cle.Cle(line))
            
        a = TasMinTabCle.TasMinTab()
        a.Ajout(param[0])
        """
        for i in range(1,len(param)):
            b = TasMinTabCle.TasMinTab()
            b.Ajout(param[i])  #Initialisation (temps negligeable)
            a.Union(b) """           
        mes(a,param)  
        param = list() 

allFiles = os.listdir("cles_alea") 
orig_stdout = sys.stdout
f = open('TasMinTabUnionMemUsage.txt', 'w')
sys.stdout = f
mesureUnion(allFiles)
sys.stdout = orig_stdout
f.close()

