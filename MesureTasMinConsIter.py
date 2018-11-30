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

def mesureConsIter(allFiles):
    allFiles.sort()
    
    res = list()
    
    for x in allFiles:
        j = 0 
        time = 0
        param = list()
        print(x)
        f = open("cles_alea/"+x,'r')
        for line in f:
            param.append(cle.Cle(line))
            
        a = tasMinTab.TasTab()
        time = time + mesureTemps(a.ConsIter,param)

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