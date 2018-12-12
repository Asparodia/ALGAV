#pip install -U memory_profiler
 
import FileBinomiale
import time
import cle
import os
import csv
 
def mesureTemps(a,b):
    c = FileBinomiale.FileBinomial()
    start = time.time()
    c = FileBinomiale.UnionFile(a,b)
    end = time.time()
    
    return (c,(end-start))
 
def mesureUnion(allFiles):
    allFiles.sort()
    res = list()
    j = 0
    for x in allFiles:
         
        time = 0
        param = list()
        tourn = list()
        f = open("cles_alea/"+x,'r')
        for line in f:
            param.append(cle.Cle(line))
        for c in param:
            tourn.append(FileBinomiale.TournoisBino(c))
        
        f = FileBinomiale.FileBinomial()
        f.AjoutTournois(tourn[0])
        
        for i in range(1,len(tourn)):
            b = FileBinomiale.FileBinomial()
            b.AjoutTournois(tourn[i])  #Initialisation (temps negligeable)
            (tasRes,tps) = mesureTemps(f,b)
            time = time + (tps*(10**3))
            f = tasRes
            
        j = j + 1
        res.append((j,x,time))
        param = list()
    return res
       

allFiles = os.listdir("cles_alea")  
       
Res = mesureUnion(allFiles)
total = 0
for f in Res:
    total = total + f[2]
Res.append((-1,"total du temps en miliseconde pour tout les fichiers : ",total))

csvfileTime = "timeFileBinoUnion.csv"
with open(csvfileTime,"w") as output:
    writer = csv.writer(output,lineterminator='\n')
    writer.writerows(Res)
print(Res)



