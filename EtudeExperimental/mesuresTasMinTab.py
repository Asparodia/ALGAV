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
 
def mesureUnion(name):   
    param = list()
    f = open(name,'r')
    for line in f:
        param.append(cle.Cle(line))
    a = TasMinTabCle.TasMinTab()
    a.Ajout(param[0])
    
    for i in range(1,len(param)//2):
        a.Ajout(param[i])  
    b = TasMinTabCle.TasMinTab()
    b.Ajout(param[len(param)//2])
    for j in range((len(param)//2)+1,len(param)):
        a.Ajout(param[j]) 
    
    start = time.time()
    a.Union(b)
    end = time.time()
    
    
    return (end-start)*10**3

def mesureUnion2(name):   
    param = list()
    f = open(name,'r')
    for line in f:
        param.append(cle.Cle(line))
    a = TasMinTabCle.TasMinTab()
    a.Ajout(param[0])
    
    for i in range(1,len(param)//2):
        a.Ajout(param[i])  
    b = TasMinTabCle.TasMinTab()
    b.Ajout(param[len(param)//2])
    for j in range((len(param)//2)+1,len(param)):
        a.Ajout(param[j]) 
    
    start = time.time()
    a.Union2(b)
    end = time.time()
    
    
    return (end-start)*10**3

fileName = "resultHashShakesPeare.txt"
Res =list()
Res.append(mesureConsIter(fileName))
Res.append(mesureAjout(fileName))
Res.append(mesureSuppMin(fileName))
Res.append(mesureUnion(fileName))
Res.append(mesureUnion2(fileName))
print(Res)
f = open("mesuresTasMinTab.txt","w")
    
f.write(str(Res[0]) + " milliseconde pour construire le Tas Min tableau avec ConsIter\n" )
f.write(str(Res[1]) + " milliseconde pour construire le Tas Min tableau avec Ajout\n" )
f.write(str(Res[2]) + " milliseconde pour tout supprimer avec SuppMin\n" )    
f.write(str(Res[3]) + " milliseconde pour construire le Tas Min tableau avec Union\n" )
f.write(str(Res[3]) + " milliseconde pour construire le Tas Min tableau avec Union2\n" )

f.close()
