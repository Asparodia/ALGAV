import TasMinTabCle
import cle
import os
import sys

def mesureConsIter(allFiles):
    allFiles.sort()
    
    for x in allFiles:
        print(x)
        param = list()
        f = open("cles_alea/"+x,'r')
        for line in f:
            param.append(cle.Cle(line))
            
        a = TasMinTabCle.TasMinTab()
        
        a.ConsIter(param)
        param = list()
        

allFiles = os.listdir("cles_alea") 

orig_stdout = sys.stdout
f = open('TasMinTabConsIterMemUsage.txt', 'w')
sys.stdout = f

mesureConsIter(allFiles)

sys.stdout = orig_stdout
f.close()

