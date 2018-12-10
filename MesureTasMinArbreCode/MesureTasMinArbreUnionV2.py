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
    allTas = list()
    for x in allFiles:
        param = list()
        f = open("cles_alea/"+x,'r')
        for line in f:
            param.append(cle.Cle(line))
        a = tasMinArbre.consIter(param)
        allTas.append([x,a])
        
    tasJeu1 = allTas[0:8]
    tasJeu2 = allTas[8:16]
    tasJeu3 = allTas[16:24]
    tasJeu4 = allTas[24:32]
    tasJeu5 = allTas[32:40]
    
    tps = 0
    res = list()
    j = 1
    for i in range(0,len(tasJeu1)):
        (tasRes,t) = mesureTemps(tasMinArbre.union,tasJeu1[i][1],tasJeu2[i][1])
        tps = tps + t
        res.append( (j,"union "+str(tasJeu1[i][0])+ " et "+ str(tasJeu2[i][0]),tps) )
        tps = 0
        j = j+ 1
        (tasRes,t) = mesureTemps(tasMinArbre.union,tasJeu1[i][1],tasJeu3[i][1])
        tps = tps + t
        res.append( (j,"union "+str(tasJeu1[i][0])+ " et "+ str(tasJeu3[i][0]),tps) )
        tps = 0
        j = j+ 1
        (tasRes,t) = mesureTemps(tasMinArbre.union,tasJeu1[i][1],tasJeu4[i][1])
        tps = tps + t
        res.append( (j,"union "+str(tasJeu1[i][0])+ " et "+ str(tasJeu4[i][0]),tps) )
        tps = 0
        j = j+ 1
        (tasRes,t) = mesureTemps(tasMinArbre.union,tasJeu1[i][1],tasJeu5[i][1])
        tps = tps + t
        res.append( (j,"union "+str(tasJeu1[i][0])+ " et "+ str(tasJeu5[i][0]),tps) )
        tps = 0
        j = j+ 1
        
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

