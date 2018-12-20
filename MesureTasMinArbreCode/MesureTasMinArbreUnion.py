#pip install -U memory_profiler
 
import tasMinArbre
import time
import cle
import os
import csv

def mesureTemps(a,b):
    c = tasMinArbre.union(a,b)
    return c
 
def mesureUnion(allFiles):
    allFiles.sort()
    allFile = list()
    for x in allFiles:
        param = list()
        f = open("cles_alea/"+x,'r')
        for line in f:
            k = cle.Cle(line)
            param.append(k)
        
        a = tasMinArbre.consIter(param)
        allFile.append([x,a])
    tasJeu1 = allFile[0:8]
    tasJeu2 = allFile[8:16]
    tasJeu3 = allFile[16:24]
    tasJeu4 = allFile[24:32]
    tasJeu5 = allFile[32:40]
    
    res = list()
    
    for i in range(0,len(tasJeu1)):
        name = tasJeu1[i][0]
        numName = name[14:]
        d = time.time()
        tasRes = mesureTemps(tasJeu1[i][1],tasJeu2[i][1])
        tasRes2 = mesureTemps(tasRes,tasJeu3[i][1])
        tasRes3 = mesureTemps(tasRes2,tasJeu4[i][1])
        mesureTemps(tasRes3,tasJeu5[i][1])
        e = time.time()
        tps = (e-d)*(10**3)
        res.append(("5 * "+numName,tps))
        
    return res


allFiles = os.listdir("cles_alea")  
       
Res = mesureUnion(allFiles)
total = 0
for f in Res:
    total = total + f[1]
Res.append((-1,"total du temps en miliseconde pour tout les fichiers : ",total))

csvfileTime = "timeTasMinArbreUnion.csv"
with open(csvfileTime,"w") as output:
    writer = csv.writer(output,lineterminator='\n')
    writer.writerows(Res)
print(Res)

