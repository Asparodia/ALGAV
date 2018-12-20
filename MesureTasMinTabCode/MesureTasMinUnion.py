import TasMinTabCle
import time
import cle
import os
import csv

def mesureTemps(a,b):
    a.Union(b)

def mesureUnion(allFiles):
    allFiles.sort()
    allTas = list()
    for x in allFiles:
        param = list()
        f = open("cles_alea/"+x,'r')
        for line in f:
            k = cle.Cle(line)
            param.append(k)
        
        a = TasMinTabCle.TasMinTab()
        a.ConsIter(param)
        allTas.append([x,a])
        
    tasJeu1 = allTas[0:8]
    tasJeu2 = allTas[8:16]
    tasJeu3 = allTas[16:24]
    tasJeu4 = allTas[24:32]
    tasJeu5 = allTas[32:40]
    
    
    res = list()
    
    for i in range(0,len(tasJeu1)):
        name = tasJeu1[i][0]
        numName = name[14:]
        d = time.time()
        mesureTemps(tasJeu1[i][1],tasJeu2[i][1])
        mesureTemps(tasJeu1[i][1],tasJeu3[i][1])
        mesureTemps(tasJeu1[i][1],tasJeu4[i][1])
        mesureTemps(tasJeu1[i][1],tasJeu5[i][1])
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
csvfileTime = "timeTasMinTabUnion.csv"
with open(csvfileTime,"w") as output:
    writer = csv.writer(output,lineterminator='\n')
    writer.writerows(Res)
print(Res)