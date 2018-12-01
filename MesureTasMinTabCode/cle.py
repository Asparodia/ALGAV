#(ptdr ca marche on a bien un ordre entre les caractere qui fait que
# 1<2<3<4<5<6<7<8<9<a<b<c<d<e<f et quand on compare deux chaine "abc" et "baa"
# la deuxieme l'emporte parce que dans premiers caracteres il prend a et b et les compare et a l'emporte

"""Classe qui vas nous servir a contenir nos clés sont des representation en hexadecimal d'un nombre codé sur 128 bits et a faire des comparaisons entre les clés"""
class Cle:

    def __init__(self,cleStr):
        
        self.name = cleStr

        """self.A=int(cleStr[2:10],base=32)
        self.B=int(cleStr[10:18],base=32)
        self.C=int(cleStr[18:26],base=32)
        self.D=int(cleStr[26:34],base=32)"""
        
        self.A= cleStr[2:10]
        self.B= cleStr[10:18]
        self.C= cleStr[18:26]
        self.D= cleStr[26:34]
        
        self.listeCle = []
        self.listeCle.append(self.A)
        self.listeCle.append(self.B)
        self.listeCle.append(self.C)
        self.listeCle.append(self.D)
        
    """
    fonction qui determine si la clef qui appelle cette methode est strictement plus petite que cle2 passer en parametre
    """    
    def inf(self, cle2):
        
        for i in range(3, 0, -1):
            if self.listeCle[i] < cle2.listeCle[i]:
                return True
            elif self.listeCle[i] > cle2.listeCle[i]:
                return False
    
    def sup(self, cle2):
        
        for i in range(3, 0, -1):
            if self.listeCle[i] > cle2.listeCle[i]:
                return True
            elif self.listeCle[i] < cle2.listeCle[i]:
                return False
        
    """
    fonction qui determine si la clef qui appelle cette methode est egale a cle2 passer en parametre
    """ 
    def eg(self, cle2):

        for i in range(3,0,-1):
            if self.listeCle[i]<cle2.listeCle[i]:
                return False
            elif self.listeCle[i]>cle2.listeCle[i]:
                return False
        return True

	
    def print(self):
        print(self.A+self.B+self.C+self.D)
        #print(self.name)

    def getKey(self):
        #return "0x"+self.name[2:10]+self.name[10:18]+self.name[18:26]+self.name[26:34]
        return self.name[2:10]+self.name[10:18]+self.name[18:26]+self.name[26:34]
    
    def __repr__(self):
        return self.getKey()
	

