import AVL
import md5
import cle
import os
import time

def shakeSpearHash(allFiles):
    allFiles.sort()
    i = 0
    ensemble = set()
    s = time.time()
    motsHash = list()
    for x in allFiles:
        
        f = open("Shakespeare/"+x,'r')
        for line in f:
            i = i + 1
            if(line not in ensemble ):
                ensemble.add(line)
    for i in ensemble:
        motsHash.append(cle.Cle("0x"+str(md5.md5(i))))
    print(len(motsHash))  
    avlTree = AVL.AVL(motsHash)
    
    e = time.time()
    return (avlTree,e-s)
            

a = os.listdir("Shakespeare")
r = shakeSpearHash(a)
ShakespearAVL,tps = r[0],r[1]

f = open("allShakespear.csv","w")
for i in ShakespearAVL.arbreBinareToTab():
    f.write(str(i)+"\n")
    
f.write(str(tps) + " seconde pour tout construire\n" )
f.write(str(ShakespearAVL.NBColli()) + " collisions\n" )
    
f.close()
