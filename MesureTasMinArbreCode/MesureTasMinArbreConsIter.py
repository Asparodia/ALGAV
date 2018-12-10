
import tasMinArbre
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
        #print(x)
        time = 0
        param = list()
        f = open("cles_alea/"+x,'r')
        for line in f:
            param.append(cle.Cle(line))
            
        time = time + mesureTemps(tasMinArbre.consIter,param)
        j = j + 1
        res.append((j,x,time))
        param = list()
        
    return res
        

allFiles = os.listdir("cles_alea")

Res = mesureConsIter(allFiles)

csvfileTime = "ConsIterTime.csv"
with open(csvfileTime,"w") as output:
    writer = csv.writer(output,lineterminator='\n')
    writer.writerows(Res)
print(Res)

total = 0
for f in Res:
    total = total + f[2]
print(str(total))