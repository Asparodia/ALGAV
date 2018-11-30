class TournoisBino:
    
    def __init__(self):
        self.key = None
        self.enfants = []
    
    def estVide(self):
        if( (self.key is None) and ( len(self.enfants) == 0 ) ):
            return True
        return False

    def decapite(self):
        if(self.estVide()):
            return False
        root = self.key
        if(self.degree() > 1 ):
            self.key = self.enfants.remove()
        else:
            self.key = None
        return root
    
    def degree(self):
        return len(self.enfants)
    
    def racine(self):
        return self.key
    
    def union2Tid(self,T):
        mine = self.racine()
        yours = T.racine()
        if(mine<yours):
            self.key = mine
            self.enfants.append(T)
            self.enfants.extend(T.enfants)
        elif(yours<mine):
            self.key = yours
            T.enfants.append(self)
            T.enfants.extend(self.enfants)
        