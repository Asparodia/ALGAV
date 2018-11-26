#Pour les fonctions sur les tas ya une bonne explication https://fr.wikipedia.org/wiki/Tas_binaire
#https://codereview.stackexchange.com/questions/197040/min-max-heap-implementation-in-python


#Arbre binaire
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def Ajout(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.Ajout(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.Ajout(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        
        if self.right:
            self.right.PrintTree()
        print( self.data),

# Use the insert method to add nodes

root = Node(2)
root.Ajout(5)
root.Ajout(6)
root.Ajout(10)
root.Ajout(13)
root.Ajout(8)
root.PrintTree()
