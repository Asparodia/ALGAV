import cle

class Noeud():
    """ Represente un noeud de notre AVL (elle vas nous servir a contenir notre donnée qui vas etre nos clé)"""
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.key)
        
class ArbreAVL:
    def __init__(self):
        self.node = None
        self.hauteur = -1 #hauteur de l'arbre vide est -1
        self.equilibre = 0
    
    def ajout(self, val):
        arbre = self.node
        add = Noeud(val)
        
        if(arbre is None):
            self.node = add
            self.node.left = ArbreAVL()
            self.node.right = ArbreAVL()
        elif(add.key.inf(arbre.key)):
            self.node.left.ajout(add.key)
        elif(add.key.sup(arbre.key)):
            self.node.right.ajout(add.key)
        self.reEquilibrage()
    
    def consIter(self,liste):
        for add in liste:
            self.ajout(add)
    
    def reEquilibrage(self):
        self.MAJ_hauteur(False)
        self.MAJ_equilibre(False)
        
        while (self.equilibre < -1 or self.equilibre > 1):
            if(self.equilibre > 1):
                if(self.node.left.equilibre < 0):
                    self.node.left.rotationGauche()
                    self.MAJ_hauteur()
                    self.MAJ_equilibre()
                self.rotationDroite()
                self.MAJ_hauteur()
                self.MAJ_equilibre()
                
                if(self.equilibre < -1):
                    if(self.node.right.equilibre > 0):
                        self.node.right.rotationDroite()
                        self.MAJ_hauteur()
                        self.MAJ_equilibre()
                    self.rotationGauche()
                    self.MAJ_hauteur()
                    self.MAJ_equilibre()
    
    def rotationDroite(self):
        racine = self.node
        fg = self.node.left.node
        fd = fg.right.node
        self.node = fg
        fg.right.node = racine
        racine.left.node = fd
        
    def rotate_left(self):
        racine = self.node
        fd = self.node.right.node
        fg = fd.left.node
        self.node = fd
        fd.left.node = racine
        racine.right.node = fg
    
    def MAJ_hauteur(self, recursion = True):
        if(not self.node is None):
            if recursion:
                if(self.node.left is not None):
                    self.node.left.MAJ_hauteur()
                if(self.node.right is not None):
                    self.node.right.MAJ_hauteur()
            self.hauteur = max(self.node.left.hauteur,self.node.right.hauteur)
            
        else:
            self.hauteur = -1
    
    def MAJ_equilibre(self,recursion=True):
        if(not self.node is None):
            if recursion:
                if(self.node.left is not None):
                    self.node.left.MAJ_equilibre()
                if(self.node.right is not None):
                    self.node.right.MAJ_equilibre()
            self.equilibre = self.node.left.hauteur - self.node.right.hauteur
        else:
            self.equilibre = 0
        
    def recherche(self,val):
        
        nodeCourant = self.node
        
        
        
        while(nodeCourant is not None):
            if(val.eg(nodeCourant.key)):
                return nodeCourant
            elif(val.inf(nodeCourant.key)):
                
                nodeCourant = nodeCourant.left.node
            else:
                
                nodeCourant = nodeCourant.right.node
        
        return nodeCourant
    
    def printTree(self, node=None, level=0):
        if not node:
            node = self.node

        if node.right.node:
            self.printTree(node.right.node, level + 1)
            print(('\t' * level), (' / '))
        print(('\t' * level), node.key)

        if node.left.node:
            print(('\t' * level), (' \\ '))
            self.printTree(node.left.node, level + 1)
    
    
    
def main():
    a=cle.Cle("0x9c1f03a0d9cf510f2765bd0f226ff5dc")
    b=cle.Cle("0x10fd1015413104a2f26018d0ab77a727")
    c=cle.Cle("0x2e73d8ce4bd45923286e966bc8cf2d95")
    d=cle.Cle("0x767accd0c60c603f71a68be994019c7e")
    e=cle.Cle("0x34c63c08abab99722b945e57081288e7")
    f=cle.Cle("0x6d481adc2aeed025f0374a5982b5c23c")
    l = list()
    l.extend([e,a,c,d,b])
    avl = ArbreAVL()
    avl.consIter(l)
    avl.printTree()    
    print(avl.recherche(d))
    
        
if __name__ == "__main__":
    main()
        
        