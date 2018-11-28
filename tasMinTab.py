from scipy import arange,append,array
import cle



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
            
            while( (self.tab[i].inf(self.tab[pere]))):
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
            return None
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
            
            if(copie[1].inf(copie[2])):
                mini = copie[1]
                maxi = copie[2]
            else:
                mini = copie[2]
                maxi = copie[1]
            
            self.tab = append(self.tab,mini)
            self.tab = append(self.tab,maxi)
            i =3
            while (i < taille-1):
                self.tab = append(self.tab,copie[i])
                i = i+1
            return res
    
    def getMin(self):
        if(len(self.tab) == 0):
            print("nothing in this heap")
            return None
        else:
            res = self.tab[0]
            return res
    
    def ConsIter(self,liste):
        
        for x in liste:
            self.Ajout(x)
            
    def Union(self,tas2):
        #HYPOTHESE : les tas n'ont pas des éléments semblable
        
        tailleTas1 = len(self.tab)
        tailleTas2 = len(tas2.tab)
        indTas1 = 0
        indTas2 = 0
        
        
        if(self.getMin().inf(tas2.getMin())):
            
            while(indTas2 < tailleTas2):
                add = (tas2.tab[indTas2])
                indTas2 = indTas2 + 1
                self.Ajout(add)
            return self
        else:
            while(indTas1 < tailleTas1):
                add = (self.tab[indTas1])
                tas2.Ajout(add)
                indTas1 = indTas1 + 1
            return tas2
        
        
            

    def showMe(self):  
        for i in self.tab:
            i.print()



"""
a=cle.Cle("0x9c1f03a0d9cf510f2765bd0f226ff5dc")
b=cle.Cle("0x10fd1015413104a2f26018d0ab77a727")
c=cle.Cle("0x2e73d8ce4bd45923286e966bc8cf2d95")
d=cle.Cle("0x767accd0c60c603f71a68be994019c7e")
e=cle.Cle("0x34c63c08abab99722b945e57081288e7")
f=cle.Cle("0x6d481adc2aeed025f0374a5982b5c23c")
print("     Test Ajout : tabTest  ")  
tabTest = TasTab()
tabTest.Ajout(f)
tabTest.Ajout(b)
tabTest.Ajout(c)
tabTest.Ajout(d)
tabTest.Ajout(a)
tabTest.Ajout(e)
tabTest.showMe()
print("========================================")
print("     Test SuppMin sur tabTest :   ")  
print("min = : "+(tabTest.SupprMin().getKey()))
print("     tabTest apres suppression : " )
tabTest.showMe()
print("========================================")
print("     Test ConsIter : tabTestConstIter :   ") 
L = [a,b,c,d,e,f]
tabTestConstIter = TasTab()
tabTestConstIter.ConsIter(L)
tabTestConstIter.showMe()
print("========================================")
print("     Test Union :    ") 
L1 = [a,b,c]
L2 = [d,e,f]
tas1 = TasTab()
tas1.ConsIter(L1)
tas2 = TasTab()
tas2.ConsIter(L2)
print(" Tas1 : ")
tas1.showMe()
print(" Tas2 : ")
tas2.showMe()
print(" TAS UNION :")
(tas1.Union(tas2)).showMe()

print("========================================")"""