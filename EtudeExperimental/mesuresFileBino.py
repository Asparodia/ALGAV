import FileBinomiale
import time
import cle

def mesureTemps(fun,param):
    start = time.time()
    fun(param)
    end = time.time()
    return (end-start)

def mesureConsIter(name):
    
    time = 0
    param = list()
    tourn = list()
    f = open(name,'r')
    for line in f:
        param.append(cle.Cle(line))
    for c in param:
        tourn.append(FileBinomiale.TournoisBino(c))
    f = FileBinomiale.FileBinomial()
    time = time +( mesureTemps(f.ConsIter,tourn)*(10**3))
    
    return (time)
        
def mesureAjout(name):
    param = list()
    tourn = list()
    f = open(name,'r')
    for line in f:
        param.append(cle.Cle(line))
    for c in param:
        tourn.append(FileBinomiale.TournoisBino(c))
    file = FileBinomiale.FileBinomial()
    tps = 0
    for t in tourn:
        s=0
        e=0
        s = time.time()
        file.AjoutTournois(t)
        e = time.time()
        tps = (tps + (e-s))*(10**3)
    return (tps)

def mesureSuppMin(name):
    param = list()
    tourn = list()
    f = open(name,'r')
    for line in f:
        param.append(cle.Cle(line))
    for c in param:
        tourn.append(FileBinomiale.TournoisBino(c))
    file = FileBinomiale.FileBinomial()
    file.ConsIter(tourn)
    tps = 0
    for t in tourn:
        s=0
        e=0
        s = time.time()
        file.SuppMin()
        e = time.time()
        tps = (tps + (e-s))*(10**3)
    return (tps)

def mesureTemps2(a,b):
    c = FileBinomiale.FileBinomial()
    start = time.time()
    c = FileBinomiale.UnionFile(a,b)
    end = time.time()
    return (c,(end-start))
 
def mesureUnion(name):   
    time = 0
    param = list()
    tourn = list()
    f = open(name,'r')
    for line in f:
        param.append(cle.Cle(line))
    for c in param:
        tourn.append(FileBinomiale.TournoisBino(c))
    file = FileBinomiale.FileBinomial()
    file.AjoutTournois(tourn[0])
    for i in range(1,len(tourn)):
        b = FileBinomiale.FileBinomial()
        b.AjoutTournois(tourn[i])  #Initialisation (temps negligeable)
        (tasRes,tps) = mesureTemps2(file,b)
        time = time + (tps*(10**3))
        file = tasRes
    return (time)

fileName = "resultHashShakesPeare.txt"
Res =list()
Res.append(mesureConsIter(fileName))
Res.append(mesureAjout(fileName))
Res.append(mesureSuppMin(fileName))
Res.append(mesureUnion(fileName))
print(Res)
f = open("mesuresFileBino.txt","w")
    
f.write(str(Res[0]) + " milliseconde pour construire la File Binomiale avec ConsIter\n" )
f.write(str(Res[1]) + " milliseconde pour construire la File Binomiale avec AjoutTournois\n" )
f.write(str(Res[2]) + " milliseconde pour tout supprimer avec SuppMin\n" )    
f.write(str(Res[3]) + " milliseconde pour construire la File Binomiale avec des unions successives Union\n" )

f.close()
