#pip install -U memory_profiler
 
import tasMinArbre
import time
import cle
import os
import csv
 
def mesureTemps(fun,a,b):
    
    start = time.time()
    c = fun(a,b)
    end = time.time()
    
    return (c,(end-start))
 
def mesureUnion(allFiles):
    allFiles.sort()
    res = list()
    j = 0
    for x in allFiles:
        print(x)
        time = 0
        param = list()
        f = open("cles_alea/"+x,'r')
        for line in f:
            param.append(cle.Cle(line))
            
        a = tasMinArbre.TasMinArbre(param[0])
        
        for i in range(1,len(param)):
            b = tasMinArbre.TasMinArbre(param[i])
            #Initialisation (temps negligeable)
            (tasRes,tps) = mesureTemps(tasMinArbre.union,a,b)
            time = time + tps
            a = tasRes
            
        j = j + 1
        print(j)
        res.append((j,x,time))
        param = list()
    return res
       

allFiles = os.listdir("cles_alea")  
       
Res = mesureUnion(allFiles)

csvfileTime = "Uniontime.csv"
with open(csvfileTime,"w") as output:
    writer = csv.writer(output,lineterminator='\n')
    writer.writerows(Res)
print(Res)


total = 0
for f in Res:
    total = total + f[2]
print(str(total))