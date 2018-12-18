"""Classe qui vas nous servir a contenir nos clés qui sont des representation en hexadecimal d'un nombre codé sur 128 bits 
cette classe vas aussi nous servir a faire des comparaisons entre les clés"""
class Cle:

    def __init__(self,cleStr):
        
        self.name = cleStr

        self.A= cleStr[2:10]
        self.B= cleStr[10:18]
        self.C= cleStr[18:26]
        self.D= cleStr[26:34]
        
        self.listeCle = []
        self.listeCle.append(self.A)
        self.listeCle.append(self.B)
        self.listeCle.append(self.C)
        self.listeCle.append(self.D)
        
    
    #fonction qui determine si la clef qui appelle cette methode est strictement plus petite que cle2 passer en parametre   
    def inf(self, cle2):
        
        for i in range(0,4):
            if self.listeCle[i] < cle2.listeCle[i]:
                return True
            elif self.listeCle[i] > cle2.listeCle[i]:
                return False
    
    #fonction qui determine si la clef qui appelle cette methode est strictement plus grande que cle2 passer en parametre 
    def sup(self, cle2):
        
        for i in range(0,4):
            if self.listeCle[i] > cle2.listeCle[i]:
                return True
            elif self.listeCle[i] < cle2.listeCle[i]:
                return False
        
    
    #fonction qui determine si la clef qui appelle cette methode est egale a cle2 passer en parametre
    def eg(self, cle2):

        for i in range(0,4):
            if self.listeCle[i]<cle2.listeCle[i]:
                return False
            elif self.listeCle[i]>cle2.listeCle[i]:
                return False
        return True

	
    def print(self):
        print(self.A+self.B+self.C+self.D)

    def getKey(self):
        return self.name[2:10]+self.name[10:18]+self.name[18:26]+self.name[26:34]
    
    def __repr__(self):
        return self.getKey()
	

