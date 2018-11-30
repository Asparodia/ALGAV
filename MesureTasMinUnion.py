#pip install -U memory_profiler
 
import tasMinTab
import time
import cle
import os
import csv
 
def mesureTemps(fun,param1):
    start = time.time()
    fun(param1)
    end = time.time()
    return (end-start)
 
def mesureUnion(allFiles):
    allFiles.sort()
    
    res = list()
    
    for x in allFiles:
        j = 0 
        time = 0
        param = list()
        print(x)
        f = open("cles_alea/"+x,'r')
        for line in f:
            param.append(cle.Cle(line))
            
        a = tasMinTab.TasTab()
        a.Ajout(param[0])
        #Initialisation du tas a unir (temps negligeable)
        
        for i in range(1,len(param)):
            b = tasMinTab.TasTab()
            b.Ajout(param[i])  #Initialisation (temps negligeable)
            
            time = time + mesureTemps(a.Union,b)

        j = j + 1
        res.append((j,x,time))
        param = list()
    return res
       

allFiles = os.listdir("cles_alea")  
       
Res = mesureUnion(allFiles[0:9])

csvfileTime = "Uniontime.csv"
with open(csvfileTime,"w") as output:
    writer = csv.writer(output,lineterminator='\n')
    writer.writerows(Res)
print(Res)