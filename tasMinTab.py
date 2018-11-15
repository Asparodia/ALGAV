import scipy

#Tas min tableau
class TasTab:

    def __init__(self):

        self.tab = arange(0)
        
            

    def Ajout(self, data):
        if(len(self.tab) == 0):
            self.tab = append(self.tab,data)
        else:
            self.tab = append(self.tab,data)
            i = len(self.tab)-1
            pere = (i-1)//2
            if(pere<0):
                pere = 0
            
            while(self.tab[i] < self.tab[pere] ):
                
                tmp = self.tab[pere]
                self.tab[pere] = self.tab[i]
                self.tab[i] = tmp
                i = pere
                pere = (i-1)//2
                if(pere<0):
                    pere = 0
    def SupprMin(self):
        
        if(len(self.tab) == 0):
            print("nothing in this heap")
            return null
        if(len(self.tab)==1):
            res = self.tab[0]
            self.tab = arange(0)
            return res
        if(len(self.tab) == 2):
            res = self.tab[0]
            self.tab = array(self.tab[1])
            return res
        else:
            res = self.tab[0]
            copie = self.tab
            taille = len(self.tab)
            self.tab = arange(0)
            self.tab = append(self.tab,min(copie[1],copie[2]))
            self.tab = append(self.tab,max(copie[1],copie[2]))
            i =3
            while (i < taille-1):
                self.tab = append(self.tab,copie[i])
                i = i+1
            return res
    
    def ConsIter(self,liste):
        
        for x in liste:
            self.Ajout(x)
            
    def Union(self,tas1,tas2):
        #HYPOTHESE : les tas n'ont pas des éléments semblable
        tailleTas1 = len(tas1.tab)
        tailleTas2 = len(tas2.tab)
        
        res = arange(tailleTas1+tailleTas2)
        
        i=0
        indTas1 = 0
        indTas2 = 0
        
        while(indTas1 < tailleTas1):
            res[i]=tas1.tab[indTas1]
            i = i+ 1
            indTas1 = indTas1 + 1
            
        while(indTas2 < tailleTas2):
            res[i]=tas2.tab[indTas2]
            indTas2 = indTas2 +1
            i=i+1
        
        return self.ConsIter(res)
        
    

    def showMe(self):  
        for i in self.tab:
            print(i)

print("Test Ajout : tab1 = ")        
tab = TasTab()
tab.Ajout(5)
tab.Ajout(10)
tab.Ajout(15)
tab.Ajout(20)
tab.Ajout(30)
tab.Ajout(4)
tab.showMe()
print("\n")
print("Test Supp min : ")
print( tab.SupprMin())
print("\n")
tab.showMe()
print("\n")
print("Test ConsIter : tab2 = ")
tab2 = TasTab()
tab2.ConsIter((1,9,14,7,19))
tab2.showMe()
print("\n")
print("Test Union tab1 et tab2 dans tab3 : ")
tab3 = TasTab()
tab3.Union(tab,tab2)
tab3.showMe()