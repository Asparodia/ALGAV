import TasMinTabCle
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
    f = open(name,'r')
    for line in f:
        param.append(cle.Cle(line))
    a = TasMinTabCle.TasMinTab()
    time = time + (mesureTemps(a.ConsIter,param)*(10**3))
    
    return (time)
        
def mesureAjout(name):
    param = list()
    f = open(name,'r')
    for line in f:
        param.append(cle.Cle(line))
    a = TasMinTabCle.TasMinTab()
    tps = 0
    for c in param:
        s=0
        e=0
        s = time.time()
        a.Ajout(c)
        e = time.time()
        tps = (tps + (e-s))*(10**3)
    return (tps)

def mesureSuppMin(name):
    param = list()
    f = open(name,'r')
    for line in f:
        param.append(cle.Cle(line))
    a = TasMinTabCle.TasMinTab()
    a.ConsIter(param)
    tps = 0
    for c in param:
        s=0
        e=0
        s = time.time()
        a.SupMin()
        e = time.time()
        tps = (tps + (e-s))*(10**3)
    return (tps)

def mesureTemps2(a,b):
    start = time.time()
    a.Union(b)
    end = time.time()
    return (a,(end-start))
 
def mesureUnion(name):   
    time = 0
    param = list()
    f = open(name,'r')
    for line in f:
        param.append(cle.Cle(line))
    a = TasMinTabCle.TasMinTab()
    a.Ajout(param[0])
    for i in range(1,len(param)):
        b = TasMinTabCle.TasMinTab()
        b.Ajout(param[i])  #Initialisation (temps negligeable)
        (tasRes,tps) = mesureTemps2(a,b)
        time = time + (tps*(10**3))
        a = tasRes
    return (time)

fileName = "resultHashShakesPeare.txt"
Res =list()
Res.append(mesureConsIter(fileName))
Res.append(mesureAjout(fileName))
Res.append(mesureSuppMin(fileName))
Res.append(mesureUnion(fileName))
print(Res)
f = open("mesuresTasMinTab.txt","w")
    
f.write(str(Res[0]) + " miliseconde pour tout construire avec ConsIter\n" )
f.write(str(Res[1]) + " miliseconde pour tout construire avec Ajout\n" )
f.write(str(Res[2]) + " miliseconde pour tout supprimer avec SuppMin\n" )    
f.write(str(Res[3]) + " miliseconde pour tout construire avec Union\n" )

f.close()
