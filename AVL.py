import cle

class Node(object):
    """La classe qui represente les noeuds de notre AVL on a besoin du parent particulierement pour les rotations"""
    def __init__(self, data):
        self.data = data
        self.hauteur = 0
        self.parent = None
        self.left = None
        self.right = None
        
    def __repr__(self):
        return str(data)
    
    def equilibre(self):
        # Methode qui nous dit de quelle coté l'arbre est déséquilibré ou si il est equilibré selon la valeur de retour
        return (self.left.hauteur if self.left else -1) - (self.right.hauteur if self.right else -1)
    
    def update_hauteur(self):
        #mets a jour la hauteur du noeud de maniere reccursive (ou plutot la profondeur -> la racine a la plus grande profondeur) 
        if not self.right and not self.left:
            self.hauteur = 0
        elif not self.right:
            self.hauteur = (self.left.hauteur + 1)
        elif not self.left:
            self.hauteur = (self.right.hauteur + 1)
        else:
            self.hauteur = (max(self.left.hauteur, self.right.hauteur) + 1)
    
class AVL(object):
    """ Classe qui vas representer notre AVL """
    def __init__(self, iterable=None):
        self.racine = None
        if iterable:
            for item in iterable:
                self.ajout(item)
        self.collision = 0
    def __repr__(self):
        return str(self.arbreBinareToTab())
    
    def arbreBinareToTab(self):
        #renvoie la representation sous forme de tableau de notre arbre
        queue = list()
        items = list()
        if not self.estVide():
            queue.append(self.racine)
        while len(queue) > 0:
            node = queue.pop(0)
            items.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return items

    def estVide(self):
        #renvoie True si l'arbre est vide
        return self.racine is None

    def recherche(self, data):
        #recherche de façon itérative une cle dans notre AVL
        courant = self.racine
        while courant is not None:
            if courant.data.eg(data):
                return courant.data
            elif courant.data.sup(data):
                courant = courant.left
                continue
            elif courant.data.inf(data):
                courant = courant.right
                continue
        print(str(data) + " n'a pas été trouver ")
        return None

    def ajout(self, data):
        #ajoute une cle (encapsuler dans la classe node definit plus haut) dans notre arbre
        n = Node(data)
        if self.racine is None:
            self.racine = n
            return

        courant = self.racine
        while courant is not None:
            if courant.data.eg(data):
                print(" cette valeur est deja dans l'arbre""")
                self.collision = self.collision + 1 
                return None
            elif courant.data.sup(data):
                #si data > valeur actuelle on l'ajoute a gauche du node qui contient la valeur actuelle
                if not courant.left:
                    courant.left = n
                    n.parent = courant
                    self.reequilibre(n) #mise a jour de la hauteur du parent et rotation si l'arbre est déséquilibré apres cet ajout
                    return
                else:
                    #si le fils gauche du noeud courant etait deja remplis on vas faire l'ajout en prenant ce fils comme noeud actuel dans une seconde itération
                    courant = courant.left
                    continue
            elif courant.data.inf(data):
                #si data < valeur actuelle on l'ajoute a droite du node qui contient la valeur actuelle
                if not courant.right:
                    courant.right = n
                    n.parent = courant
                    #mise a jour de la hauteur du parent et rotation si l'arbre est déséquilibré apres cet ajout
                    self.reequilibre(n)
                    return
                else:
                    courant = courant.right
                    continue

    def reequilibre(self, node):
        #reequilibre l'abre si il faut
        courant = node.parent
        while courant is not None:
            courant.update_hauteur()
            eq = courant.equilibre()
            
            if eq < -1:
                #déséquilibre a droite
                if courant.right:
                    right_eq = courant.right.equilibre()
                    if right_eq >= 1:
                        #double rotation
                        self.right_rotation(courant.right)
                    self.left_rotation(courant)
                    courant = courant.parent
                    continue
                else:
                    self.left_rotation(courant)

            elif eq > 1:
                #déséquilibre a gauche
                if courant.left:
                    left_eq = courant.left.equilibre()
                    if left_eq <= -1:
                        #double rotation
                        self.left_rotation(courant.left)
                    self.right_rotation(courant)
                    courant = courant.parent
                    continue
                else:
                    
                    self.right_rotation(courant)
            else:
                #equilibré
                courant = courant.parent

    def left_rotation(self, node):
        #rotation gauche simple
        new_left = node
        new_right_of_left = node.right.left
        new_parent = node.right

        new_grandparent = node.parent

        if new_grandparent is None:
            self.racine = new_parent
            new_parent.parent = None
        else:
            if node.data .sup(new_grandparent.data):
                new_grandparent.right = new_parent
            else:
                new_grandparent.left = new_parent
            new_parent.parent = new_grandparent

        new_parent.left = new_left
        new_left.parent = new_parent
        new_left.right = new_right_of_left
        if new_right_of_left:
            new_right_of_left.parent = new_left
        new_left.update_hauteur()
        new_parent.update_hauteur()

    def right_rotation(self, node):
        #rotation droite simple
        
        new_right = node
        new_left_of_right = node.left.right
        new_parent = node.left

        new_grandparent = node.parent
        if new_grandparent is None:
            self.racine = new_parent
            new_parent.parent = None
        else:
            if node.data.sup(new_grandparent.data):
                new_grandparent.right = new_parent
            else:
                new_grandparent.left = new_parent
            new_parent.parent = new_grandparent

        new_parent.right = new_right
        new_right.parent = new_parent
        new_right.left = new_left_of_right
        if new_left_of_right:
            new_left_of_right.parent = new_right
        new_right.update_hauteur()
        new_parent.update_hauteur()

    
    def NbColli(self):
        return self.collision


if __name__ == "__main__":
    
    a=cle.Cle("0x00000000000000000000000000000001")
    b=cle.Cle("0x00000000000000000000000000000002")
    c=cle.Cle("0x00000000000000000000000000000003")
    d=cle.Cle("0x00000000000000000000000000000004")
    e=cle.Cle("0x00000000000000000000000000000005")
    f=cle.Cle("0x6d481adc2aeed025f0374a5982b5c23c")
    l = list()
    l.extend([a,b,c])
    data = [a,b,c,d,e,f]
    avl_tree = AVL(data)
    print(avl_tree)
    