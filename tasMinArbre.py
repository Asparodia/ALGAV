#Pour les fonctions sur les tas ya une bonne explication https://fr.wikipedia.org/wiki/Tas_binaire
#https://codereview.stackexchange.com/questions/197040/min-max-heap-implementation-in-python


#Arbre binaire
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        if data is None :
            self.data = None
        else :
            self.data = data
        
#renvoie le nombre de noeud qu'à le sous arbre enraciné en ce noeud
    def NbNoeud(self):
        if self.right is None and self.left is None :
            return 1
        elif self.right == None :
            return 1 + self.left.NbNoeud()
        elif self.left == None :
            return 1 + self.right.NbNoeud()
        else :
            return 1 + self.right.NbNoeud() + self.left.NbNoeud()
#Ajoute l'élement data dans un arbre
    #j'ai fais des retourne parce que ça ne s'arrête pas sinon tu me diras quoi mettre sinon.
    def Ajout(self, data):
        if self.data is not None:
            if self.data <= data :
                if self.left is None :
                    self.left = Node(data)
                    return True
                if self.right is None:
                    self.right = Node(data)
                    return True
                if self.left.NbNoeud() >= self.right.NbNoeud():
                    self.right.Ajout(data)
                    return True
                if self.left.NbNoeud() < self.right.NbNoeud():
                    self.left.Ajout(data)
                    return True
            else :
                valeur = self.data
                self.data = data
                self.Ajout(valeur)
                return True

        else:
            self.data = Node(data)
            return True


    # lorsqu'on ajoute un node
    def ajoutNode(self,data):
        if self.data is not None :
            if self.data < data.data:
                if self.left is None:
                    self.left = data
                    return True
                if self.right is None:
                    self.right = data
                    return True
                if self.left.NbNoeud() >= self.right.NbNoeud():
                    self.right.ajoutNode(data)
                    return True
                if self.left.NbNoeud() < self.right.NbNoeud():
                    self.left.ajoutNode(data)
                    return True
            else:
                valeur = self
                self = data
                self.ajoutNode(valeur)
                return True
        else :
            self = data
            return True


    def prefixePrint(self):
        if self.left:
            self.left.prefixePrint()
        if self.right:
            self.right.prefixePrint()
        print(self.data)

#Supprime l'élement le plus petit de l'arbre
    def supprMin(self):
        if self.data is None:
            return False
        else:
            print("Suppresion de la racine :"+str(self.data))
            print(self.left.NbNoeud())
            print(self.right.NbNoeud())
            add = union(self.left, self.right)
            print(add.NbNoeud())
            return add


    def ajoutArbre(self, arbre):
        if arbre.right is not None :
            self.ajoutArbre(arbre.right)
        if arbre.left is not None :
            self.ajoutArbre(arbre.left)
    
        self.Ajout(arbre.data)
            

#Fais l'union de deux arbres
def union(arbre1, arbre2) :
    if arbre1 is None :
        return arbre2
    if arbre2 is None :
        return arbre1
    else :
        if arbre1.data < arbre2.data :
            arbre1.ajoutArbre(arbre2)
            return arbre1
        else :
            arbre2.ajoutArbre(arbre1)
            return arbre2



#Construction itérative d'un arbre à partir d'une liste d'élement
def consIter(liste) :
    racine = Node()
    for i in range(len(liste)):
        racine.Ajout(liste[i])


root = Node(2)
root.Ajout(13)
root.Ajout(8)
root.Ajout(30)
root.Ajout(6)
root.Ajout(10)

root2 = Node(120)
root2.Ajout(5)
root2.Ajout(1)
root2.Ajout(9)
root2.Ajout(7)
root2.Ajout(12)
root2.Ajout(35)
root2.Ajout(42)
root2.Ajout(22)

root3 = Node(1)
root3.ajoutNode(Node(2))
root3.ajoutNode(Node(3))
root3.ajoutNode


print(root.NbNoeud())

arbre = root.supprMin()
"""root.Ajout(7)
root.Ajout(12)
root.Ajout(15)
root.Ajout(14)
"""

"""print("hauteur " + str(root.Hauteur()))"""
print(arbre.NbNoeud())
