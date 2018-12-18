import AVL
import md5
import cle
import os
import time

def shakeSpearHash(allFiles):
    allFiles.sort()
    i = 0
    ensemble = set()
    motsHash = list()
    s = time.time()
    
    for x in allFiles:
        
        f = open("Shakespeare/"+x,'r')
        for line in f:
            i = i + 1
            if(line not in ensemble ):
                ensemble.add(line[:-2])
    for e in ensemble:
        motsHash.append(cle.Cle("0x"+str(md5.md5(e))))
    
    avlTree = AVL.AVL(motsHash)
    e = time.time()
    return (avlTree,e-s,avlTree.NbColli(),ensemble,len(ensemble),i)
            

a = os.listdir("Shakespeare")
r = shakeSpearHash(a)
ShakespearAVL,motsDifferent = r[0],r[3]

f = open("allShakespear.csv","w")
f.write(str(r[5]) + " mots au total dans Shakespeare\n" )
f.write(str(r[4]) + " mots different\n" )
f.write(str(r[1]) + " seconde pour hasher les mots et construire l'AVL\n" )
f.write(str(r[2]) + " collisions dans l'AVL qui contient le hasher des mots differents\n" )

for i in ShakespearAVL.arbreBinareToTab():
    f.write(str(i)+"\n")
    
f.close()
