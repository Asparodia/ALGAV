import TasMinTabCle
import time
import cle
import os
import csv

def mesureTemps(fun,param):
    start = time.time()
    fun(param)
    end = time.time()
    return (end-start)

def mesureConsIter(allFiles):
    allFiles.sort()
    
    res = list()
    j = 0 
    for x in allFiles:
        
        time = 0
        param = list()
        f = open("cles_alea/"+x,'r')
        print(x)
        for line in f:
            param.append(cle.Cle(line))
            
        a = TasMinTabCle.TasMinTab()
        time = time + (mesureTemps(a.ConsIter,param)*(10**3))

        j = j + 1
        res.append((j,x,time))
        param = list()
    return res
        

allFiles = os.listdir("cles_alea")
total = 0
Res = mesureConsIter(allFiles)
for f in Res:
    total = total + f[2]
Res.append((-1,"total du temps en milliseconde pour tout les fichiers : ",total))
csvfileTime = "timeTasMinTabConsIter.csv"
with open(csvfileTime,"w") as output:
    writer = csv.writer(output,lineterminator='\n')
    writer.writerows(Res)
print(Res)