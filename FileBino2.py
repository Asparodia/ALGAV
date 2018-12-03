class TournoisBino:
    
    def __init__(self):
        self.key = None
        self.parent = None
        self.enfants = []
        self.degre = 0
    
    def estVide(self):
        if( (self.key is None) and ( len(self.enfants) == 0 ) ):
            return True
        return False

    def decapite(self):
        if(self.estVide()):
            return False
        root = self.key
        
            
        
    
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
        