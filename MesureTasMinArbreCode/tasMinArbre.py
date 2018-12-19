import cle

#Arbre binaire
class TasMinArbre:
    """La classe TasMinArbre represente un tas min dont les données 
    sont stocker dans un arbre binaire.
    """
    def __init__(self, data):

        self.left = None
        self.right = None
        
        if data is None :
            self.data = None
            self.nbNoeud = 0
        else :
            self.data = data
            self.nbNoeud = 1
            
    def __repr__(self):
        return str(self.arbreBinareToTab())
    
    def arbreBinareToTab(self):
        #renvoie la representation sous forme de tableau de notre arbre
        queue = list()
        items = list()
        if self.nbNoeud >0:
            queue.append(self)
        while len(queue) > 0:
            node = queue.pop(0)
            items.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return items

    def Ajout(self, data):
        #Ajoute l'élement data dans un arbre
        if self.data is not None :
            if self.data.inf(data) :
                self.nbNoeud = self.nbNoeud + 1
                if self.left is None :
                    self.left = TasMinArbre(data)
                    return True
                if self.right is None:
                    self.right = TasMinArbre(data)
                    return True
                if self.left.nbNoeud >= self.right.nbNoeud:
                    self.right.Ajout(data)
                    return True
                if self.left.nbNoeud < self.right.nbNoeud:
                    self.left.Ajout(data)
                    return True
            else :
                valeur = self.data
                self.data = data
                self.Ajout(valeur)
                return True

        else:
            self.data = TasMinArbre(data)
            return True

    def getMin(self):
        return self.data
    
    def prefixePrint(self):
        if self.left:
            self.left.prefixePrint()
        if self.right:
            self.right.prefixePrint()
        print(self.data)


    def supprMin(self):
        #Supprime l'élement le plus petit de l'arbre
        if self.data is None:
            return False
        else:
            add = union(self.left, self.right)
            return add


    def ajoutArbre(self, arbre):
        #Ajoute un sous arbre dans l'arbre qui l'appelle
        if arbre.right is not None :
            self.ajoutArbre(arbre.right)
        if arbre.left is not None :
            self.ajoutArbre(arbre.left)
    
        self.Ajout(arbre.data)
            


def union(arbre1, arbre2) :
    #Fais l'union de deux arbres
    if arbre1 is None :
        return arbre2
    if arbre2 is None :
        return arbre1
    else :
        if arbre1.data.inf(arbre2.data) :
            arbre1.ajoutArbre(arbre2)
            return arbre1
        else :
            arbre2.ajoutArbre(arbre1)
            return arbre2




def consIter(liste) :
    #Construction itérative d'un arbre à partir d'une liste d'élement
    if(len(liste)>0):
        racine = TasMinArbre(liste[0])
        for i in range(1,len(liste)):
            racine.Ajout(liste[i])
        return racine
    return None