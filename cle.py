#(ptdr ca marche on a bien un ordre entre les caractere qui fait que
# 1<2<3<4<5<6<7<8<9<a<b<c<d<e<f et quand on compare deux chaine "abc" et "baa"
# la deuxieme l'emporte parce que dans premiers caracteres il prend a et b et les compare et a l'emporte

"""Classe qui vas nous servir a contenir nos clés sont des representation en hexadecimal d'un nombre codé sur 128 bits et a faire des comparaisons entre les clés"""
class Cle:

    def __init__(self,cleStr):

        self.A=cleStr[2:10]
        self.B=cleStr[10:18]
        self.C=cleStr[18:26]
        self.D=cleStr[26:24]
        
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


#Pour faire des test avec inf et eg :
a="0x9c1f03a0d9cf510f2765bd0f226ff5dc"
b="0x10fd1015413104a2f26018d0ab77a727"
c1=Cle(a)    
c2=Cle(b)

print(c2.inf(c1))
print(c2.eg(c2))


""" AVANT :
    
    inf : string * string -> Boolean
    clef1 et clef2 sont des representation en hexadecimal d'un nombre codé sur 128 bits
    fonction qui determine si clef1 est strictement plus petite que clef 2

def inf(clef1, clef2):
    listeClef1 = []
    listeClef2 = []
    listeClef1.append(clef1[2:10])
    listeClef1.append(clef1[10:18])
    listeClef1.append(clef1[18:26])
    listeClef1.append(clef1[26:34])

    listeClef2.append(clef2[2:10])
    listeClef2.append(clef2[10:18])
    listeClef2.append(clef2[18:26])
    listeClef2.append(clef2[26:34])
    for i in range(3, 0, -1):
        if listeClef1[i] < listeClef2[i]:
            return True
        elif listeClef1[i] > listeClef2[i]:
            return False



    inf : string * string -> Boolean
    clef1 et clef2 sont des representation en hexadecimal d'un nombre codé sur 128 bits
    fonction qui rend vrais quand clef1 et clef2 sont égale sinon false
    
def eg(clef1, clef2):
    listeClef1 = []
    listeClef2 = []
    listeClef1.append(clef1[2:10])
    listeClef1.append(clef1[10:18])
    listeClef1.append(clef1[18:26])
    listeClef1.append(clef1[26:34])

    listeClef2.append(clef2[2:10])
    listeClef2.append(clef2[10:18])
    listeClef2.append(clef2[18:26])
    listeClef2.append(clef2[26:34])
    for i in range(3, 0, -1):
        if listeClef1[i] < listeClef2[i]:
            return False
        elif listeClef1[i] > listeClef2[i]:
            return False
    
    return True
"""