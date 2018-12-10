import FileBinomiale
import time
import cle
import os
import csv
 
def mesureTemps(a,b):
    start = time.time()
    c = FileBinomiale.UnionFile(a,b)
    end = time.time()
    return (c,(end-start))
 
def mesureUnion(allFiles):
    allFiles.sort()
    allFile = list()
    for x in allFiles:
        param = list()
        f = open("cles_alea/"+x,'r')
        for line in f:
            k = cle.Cle(line)
            t = FileBinomiale.TournoisBino(k)
            param.append(t)
        
        a = FileBinomiale.FileBinomial()
        a.ConsIter(param)
        allFile.append([x,a])
    tasJeu1 = allFile[0:8]
    tasJeu2 = allFile[8:16]
    tasJeu3 = allFile[16:24]
    tasJeu4 = allFile[24:32]
    tasJeu5 = allFile[32:40]
    
    
    res = list()
    j = 1
    tps = 0
    for i in range(0,len(tasJeu1)):
        (tasRes,t) = mesureTemps(tasJeu1[i][1],tasJeu2[i][1])
        tps = tps + t
        print(tasRes)
        res.append( (j,"union "+str(tasJeu1[i][0])+ " et "+ str(tasJeu2[i][0]),tps) )
        tps = 0
        j = j+ 1
        (tasRes2,t) = mesureTemps(tasRes,tasJeu3[i][1])
        tps = tps + t
        res.append( (j,"union "+str(tasJeu1[i][0])+ " et "+ str(tasJeu3[i][0]),tps) )
        tps = 0
        j = j+ 1
        (tasRes3,t) = mesureTemps(tasRes2,tasJeu4[i][1])
        tps = tps + t
        res.append( (j,"union "+str(tasJeu1[i][0])+ " et "+ str(tasJeu4[i][0]),tps) )
        tps = 0
        j = j+ 1
        (tasRes4,t) = mesureTemps(tasRes3,tasJeu5[i][1])
        tps = tps + t
        res.append( (j,"union "+str(tasJeu1[i][0])+ " et "+ str(tasJeu5[i][0]),tps) )
        tps = 0
        j = j+ 1
        tasRes = None
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