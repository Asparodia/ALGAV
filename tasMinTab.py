from scipy import *
a = array([1, 2, 3, 4, 5, 1j, 1+3j])


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

    def showMe(self):  
        for i in self.tab:
            print(i)

        
tab = TasTab()
tab.Ajout(5)
tab.Ajout(10)
tab.Ajout(15)
tab.Ajout(20)
tab.Ajout(30)
tab.Ajout(4)
tab.showMe()
"""print("Supp min : ")
print(tab.SupprMin())
print("\n")
tab.showMe()"""
