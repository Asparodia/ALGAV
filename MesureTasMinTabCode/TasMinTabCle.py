import cle

class TasMinTab():
    """La classe TasMinTab represente un tas min dont les donnÃ©es 
    sont stocker dans un tableau (nous avons ici utiliser les list()
    car elles sont plus facile a utiliser).
    Dans ce tableau nous pouvons avoir l'indice d'un parent P grace a l'indice de son fils F
    ind(P) = ind(F)//2
    """

    def __init__(self):
         
        """ la premiere case de notre liste est initialiser a 0 et n'est pas utiliser directement 
        nous l'utilisons pour rendre plus simple nos calculs d'indice parent et d'indice fils(pour evite le cas ou l'indice deviens negatif apres avoir voulus trouver le pere)
        la racine de notre tas min sera a l'indice 1 de notre liste.
        tailleTas nous servira a suivre la taille de notre tas et nous donnera par la meme occasion l'indice du dernier element du tas"""
        self.tas = [cle.Cle("0x00000000000000000000000000000000")]
        
        self.tailleTas = 0 

    def getMin(self):
        if(self.estVide()):
            return None
        return self.tas[1]

    def estVide(self):
        if (self.tailleTas == 0):
            return True
        else:
            return False

    def getTaille(self):
        return self.tailleTas
    
    def copie(self):
        res = TasMinTab()
        res.tas = self.tas.copy()
        res.tailleTas = self.tailleTas
        return res

    def remonte(self, ind):
        """
        Regarde si la valeur a l'indice ind est plus petite que son pere si oui elle echange les deux valeurs de place
        tant qu'elle peut faire remontrer cette valeur elle continue.
        """
        while ind != 0:
            if (self.tas[ind//2].sup(self.tas[ind])):
                tmp = self.tas[ind//2]
                self.tas[ind//2] = self.tas[ind]
                self.tas[ind] = tmp
                ind = ind//2
            else:
                break

    def descend(self,ind):
        """
        Regarde si la valeur a l'indice ind est plus grande que ses fils, si oui elle echange les deux valeurs de place
        tant qu'elle peut faire descendre cette valeur elle continue .
        ind * 2 est le fils droit et ind * 2 +1 le fils gauche
        """
        while ((ind * 2) <= self.tailleTas):
            if (ind * 2 + 1 > self.tailleTas):
                minFils = ind * 2
            else:
                if( self.tas[ind*2].inf( self.tas[ind*2+1])):
                    minFils = ind * 2
                else:
                    minFils = ind * 2 + 1
            
            if (self.tas[minFils].inf(self.tas[ind])):
                tmp = self.tas[ind]
                self.tas[ind] = self.tas[minFils]
                self.tas[minFils] = tmp

            ind = minFils

    def Ajout(self,val):
        """Pour ajouter une valeur dans notre tas min nous allons l'ajouter a la fin de notre tableau puis nous allons la faire remonter
        jusqu'Ã  ce qu'elle arrive a la bonne place (c'est a dire elle est superieur a la valeur de son pere si elle en a un 
        et inferieur aux valeurs de ses fils si elle en a).
        La methode remonte vas se charger de remonter la valeur val Ã  l'indice i si necessaire.
        """
        self.tas.append(val)
        self.tailleTas = self.tailleTas + 1
        self.remonte(self.tailleTas)

    
    

    def SupMin(self):
        """
        On renvoie la valeur minimal du tas c'est a dire sa racine et ensuite on la supprime du tas en veillant a laisser le tas dans un Ã©tat valide qui satisfait les contraintes du tas min.
        Pour cela une fois que nous avons pris le minimum nous allons prendre la plus grande valeur du tas (celle a la fin de notre liste donc)
        et la faire descendre jusqu'a la fin cela vas nous permettre de faire tout les echanges necessaire pour conserver un tas min, ensuite nous allons
        supprimer la derniere valeur car elle sera en double.
        """
        val = self.getMin()
        self.tas[1] = self.tas[self.tailleTas]
        self.descend(1)
        self.tas.pop()
        self.tailleTas = self.tailleTas - 1
        return val


   
    def ConsIter(self, vals):
        """
        Construit un tas qui aura pour valeurs les elements de la liste vals
        """
        self.tas.extend(vals)
        self.tailleTas = len(vals)
        for i in range((len(self.tas)//2),0,-1):
            self.descend(i)
        
    
    def Union(self,tas2):
        L = self.tas[1:]
        L.extend(tas2.tas[1:])
        self.tas = [cle.Cle("0x00000000000000000000000000000000")]
        self.tailleTas = 0
        self.ConsIter(L)
    
    def Union2(self,tas2):
        """ 
        Rend l'union du tas actuel avec le second tas passer en parametres (le tas qui appelle cette fonction vas etre modifier si on l'uni avec un tas non vide)
        Le parametre vas etre une copie du tas a unir dans le tas actuel juste pour eviter de modifier cette liste avec notre algorithme
        complexité en max(n,m)*log(max(n,m))
        """
        if(self.estVide() and tas2.estVide()):
            print("les deux tas son vide Union est vide")
            return
        elif(self.estVide()):
            self.tas = tas2.tas
            self.tailleTas = tas2.tailleTas
            return
        elif(tas2.estVide()):
            return
        else:
            tas1Min = self.getMin()
            tas2Min = tas2.getMin()
 
            if(tas1Min.inf(tas2Min)):
                for i in range(1,tas2.getTaille()+1):
                    add = tas2.tas[i]
                    self.Ajout(add)
            else:
                for i in range(1 ,self.getTaille()+1):
                    add = self.tas[i]
                    tas2.Ajout(add)
                self.tas = tas2.tas
                self.tailleTas = tas2.tailleTas
            return
        
        
        
    def __repr__(self):
        return "Tas Binaire Tab : " + str(self.tas[1:])