#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#pip install -U memory_profiler

import tasMinTab
import time
import cle
import os
import csv

def mesureTemps(fun,param1):
    start = time.time()
    fun(param1)
    end = time.time()
    return (end-start)

def mesure(fun,file):
    param = list()
    f= open(file,'r')
    for line in f:
        param.append(cle.Cle(line))
    time = 0
    for i in range(0,len(param)):
        tmp = tasMinTab.TasTab()
        tmp.Ajout(param[i])
        time = time + mesureTemps(fun,tmp)
        
    return time
        

a=tasMinTab.TasTab()
a.Ajout(cle.Cle("0x00000000000000000000000000000000"))
print(mesure(a.Union,"cles_alea/jeu_1_nb_cles_100.txt"))



allFiles = os.listdir("cles_alea")
allFiles.sort()

Res = list()

i = 0
for x in allFiles:
    a=tasMinTab.TasTab()
    a.Ajout(cle.Cle("0x00000000000000000000000000000000"))
    Res.append((i,mesure(a.Union,"cles_alea/"+x),x))
    i = i+1

csvfileTime = "Uniontime.csv"
with open(csvfileTime,"w") as output:
    writer = csv.writer(output,lineterminator='\n')
    writer.writerows(Res)
print(Res)

total = 0
for x in Res:
    total = total + x[1]
print("total time Union pour nos ficher = "+str(total))