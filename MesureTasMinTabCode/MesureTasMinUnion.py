#pip install -U memory_profiler
 
import TasMinTabCle
import time
import cle
import os
import csv
 
def mesureTemps(a,b):
    start = time.time()
    a.Union(b)
    end = time.time()
    return (a,(end-start))
 
def mesureUnion(allFiles):
    allFiles.sort()
    res = list()
    j = 0
    for x in allFiles:
         
        time = 0
        param = list()
        f = open("cles_alea/"+x,'r')
        for line in f:
            param.append(cle.Cle(line))
            
        a = TasMinTabCle.TasMinTab()
        a.Ajout(param[0])
        
        for i in range(1,len(param)):
            b = TasMinTabCle.TasMinTab()
            b.Ajout(param[i])  #Initialisation (temps negligeable)
            (tasRes,tps) = mesureTemps(a,b)
            time = time + tps
            a = tasRes
            
        j = j + 1
        res.append((j,x,time))
        param = list()
    return res
       

allFiles = os.listdir("cles_alea")  
       
Res = mesureUnion(allFiles)
total = 0
for f in Res:
    total = total + f[2]
Res.append((-1,"total du temps en seconde pour tout les fichiers : ",total))
csvfileTime = "timeTasMinTabUnion.csv"
with open(csvfileTime,"w") as output:
    writer = csv.writer(output,lineterminator='\n')
    writer.writerows(Res)
print(Res)
