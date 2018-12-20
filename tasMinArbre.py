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
            res = self.data
            add = union(self.left, self.right)
            self.data = add.data
            self.left = add.left
            self.right = add.right
            return res


    def ajoutArbre(self, arbre):
        #Ajoute un sous arbre dans l'arbre qui l'appelle
        if arbre.right is not None :
            self.ajoutArbre(arbre.right)
        if arbre.left is not None :
            self.ajoutArbre(arbre.left)
    
        self.Ajout(arbre.data)
    
    def getMin(self):
        return self.data
            


def union(arbre1, arbre2) :
    #Fais l'union de deux arbres
    L = arbre1.arbreBinareToTab()
    L.extend(arbre2.arbreBinareToTab())
    res = consIter(L)
    return res

def union2(arbre1,arbre2):
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

def main():
    print("test de Ajout sur notre arbre : ")
    a=cle.Cle("0x9c1f03a0d9cf510f2765bd0f226ff5dc")
    b=cle.Cle("0x10fd1015413104a2f26018d0ab77a727")
    c=cle.Cle("0x2e73d8ce4bd45923286e966bc8cf2d95")
    d=cle.Cle("0x767accd0c60c603f71a68be994019c7e")
    e=cle.Cle("0x34c63c08abab99722b945e57081288e7")
    f=cle.Cle("0x6d481adc2aeed025f0374a5982b5c23c")
    root = TasMinArbre(a)
    root.Ajout(b)
    root.Ajout(c)
    root.Ajout(d)
    root.Ajout(e)
    root.Ajout(f)
    print(root)
    print(" Nombres de noeud : "+ str(root.nbNoeud))
    print("======================================")
    print("test ConsIter : ")
    a=cle.Cle("0x9a5cdb45f1951a3a82b09af737fdc9aa")
    b=cle.Cle("0x53f7ffe901f3686b875af337039ee262")
    c=cle.Cle("0xa89aa39aa55e5bb5fb33a1802b248207")
    d=cle.Cle("0x8aefe5f306ac962bcbdb63aeb58d1e35")
    e=cle.Cle("0x85c3d80bfe89b91033b23cd659cddb08")
    f=cle.Cle("0x45484c820aee4c04ef89c1db9bb3eaf5")
    root2 = consIter([a,b,c,d,e,f])
    print("liste des cles a mettre dans le tas min : " + str([a,b,c,d,e,f]))
    print("\n")
    print(" representation sous forme de tableau de l'arbre obtenue avec consIter : ")
    print(root2)
    print("Nombre de Noeud : "+str(root2.nbNoeud))
    
    print("======================================")
    print("test supprMin sur le premier arbre ")
    print("minimum de l'arbre 1 est : "+str(root.supprMin()))    
    print("arbre apres suppression du minimum : "+str(root))
    print(" Nombre de noeud : "+ str(root.nbNoeud))
    print("======================================")
    print("test union de deux arbre ")
    a=cle.Cle("0x9c1f03a0d9cf510f2765bd0f226ff5dc")
    b=cle.Cle("0x10fd1015413104a2f26018d0ab77a727")
    c=cle.Cle("0x2e73d8ce4bd45923286e966bc8cf2d95")
    d=cle.Cle("0x767accd0c60c603f71a68be994019c7e")
    e=cle.Cle("0x34c63c08abab99722b945e57081288e7")
    f=cle.Cle("0x6d481adc2aeed025f0374a5982b5c23c")
    root = TasMinArbre(a)
    root.Ajout(b)
    root.Ajout(c)
    root.Ajout(d)
    root.Ajout(e)
    root.Ajout(f)
    print("arbre 1 : "+str(root))
    print("Nombre de noeud : "+ str(root.nbNoeud))
    print("\n")
    print("arbre 2 : "+str(root2))
    print("Nombre de Noeud : "+str(root2.nbNoeud))
    print("\n")
    fusion = union(root,root2)
    print("fusion : "+str(fusion))
    print(" Nombres de noeud : "+ str(fusion.nbNoeud))
    
    print("\n========================================")
    print("Test sur les jeu1 et jeu5 de taille 50 000\n")
    fichier = open("cles_alea/jeu_5_nb_cles_50000.txt",'r')
    param = list()
    for line in fichier:
        param.append(cle.Cle(line))
    fichier.close()
    print("ConsIter sur une liste de 50 000 cle")
    tasC = consIter(param)
    print("Nombre de Noeud : "+str(tasC.nbNoeud))
    print("le minimum est : "+str(tasC.getMin()))
    
    print("Union de deux tas construit avec 50 000 clé chacun")
    f2 = open("cles_alea/jeu_1_nb_cles_50000.txt",'r')
    param2 = list()
    for line in f2:
        param2.append(cle.Cle(line))
    f2.close()
    tasU = consIter(param2)
    print("tas 1 minimum : "+str(tasC.getMin()) )
    print("tas 1 nombre de Noeud : "+str(tasC.nbNoeud ))
    print("tas 2 minimum : "+str(tasU.getMin()) )
    print("tas 2 nombre de Noeud : "+str(tasU.nbNoeud) )
    print("on a : \n\t"+ str(tasC.getMin()) +" qui est inferieur a "+ str(tasU.getMin()))
    tasC.getMin().inf(tasU.getMin())
    res = union(tasU,tasC)
    print("tas fusion de tas1 et tas 2 a une taille : "+str(res.nbNoeud ))
    print("le minimum du tas fusion est : "+str(res.getMin()))
    
    
    

if __name__ == "__main__":
    main()
