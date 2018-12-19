import cle

class TournoisBino:
    """ Classe representant un tournois binomial, elle vas etre utiliser pour representer notre file binomiale comme une liste de tournois binomiaux"""
    def __init__(self,root):
        self.racine = root
        self.enfants = [] #chaque enfant est un tournois de degre plus petit que le tournoi actuel
        self.degre = 0
    
    def decapite(self):
        res = self.racine
        if(len(self.enfants)>1):
            self.degre = self.degre - 1
            self.racine = self.enfants[0].racine
            self.enfants.pop(0)
            return res
        self.racine = None
        return res
    
    def estVide(self):
        if(self.racine is None):
            return True
        return False
    
    def file(self):
        """ transforme un tournois en file binomial qui a pour unique tournois ce tournois"""
        res = FileBinomial()
        res.AjoutTournois(self)
        return res
    
    def __repr__(self):
        res = "Tournois Binomial : "
        res = res +" racine : " + str(self.racine) 
        res = res +" degre : [" + str(self.degre) +"]"
        return res

    
class FileBinomial:
    """ Une file Binomiale est une liste de tournois"""
    def __init__(self):
        self.tournois = []
        
    def estVide(self):
        if(self.tournois == []):
            return True
        return False
    
    def minDegre(self):
        """ renvoie le tournois de degre minimum"""
        if(self.estVide()):
            return None
        self.tournois = sorted(self.tournois,key = lambda tournoi : tournoi.degre)
        return self.tournois[0]
    
    def reste(self):
        """renvoie la file privé de son tournois de degree minimum"""
        if(self.estVide()):
            return None
        self.tournois = sorted(self.tournois,key = lambda tournoi : tournoi.degre)
        self.tournois.pop(0)
        return self
    
    def SuppMin(self):
        """ renvoie le tournois avec la racine la plus petite et le supprime de la file"""
        if self.tournois == []:
            return None
        
        tournoisP = self.tournois[0]
        self.tournois.pop(0)
        h = FileBinomial()
        for t in tournoisP.enfants:
            h.AjoutTournois(t)
            
        res = UnionFile(self,h)
        self.tournois = res.tournois
 
        return tournoisP.racine


    def AjoutTournois(self, t):
        """ Ajoute un tournois dans la file"""
        if(self.tournois == []):
            self.tournois.append(t)
        else:
            f = FileBinomial()
            f.AjoutTournois(t)
            res = UnionFile(self,f)
            self.tournois = res.tournois
            
            
    def ConsIter(self,tournois):
        """Construit une file a partir d'une liste de tournois"""
        for t in tournois:
            self.AjoutTournois(t)
        
    def __repr__(self):
        res = "File Binomiale : < "
        for x in self.tournois:
            res = res + "TB" + str(x.degre) +" "
        res = res + ">"
        return res
        
def union2Tid(t1,t2):
    """ Renvoie l'union entre deux tournois de meme taille"""
    if(t1.estVide() or t2.estVide()):
        return None
    rac1 = t1.racine
    rac2 = t2.racine
    if(rac1.inf(rac2)):
        t1.enfants.append(t2)
        t1.racine = rac1
        t1.degre = t1.degre + 1
        return t1
    else:
        t2.enfants.append(t1)
        t2.racine = rac2
        t2.degre = t1.degre + 1
        return t2

def UnionFile(F1,F2):
    """ renvoie l'union entre deux file Binomial"""
    t = TournoisBino(None)
    return Union(F1,F2,t)

def ajoutMin(F,tournoi):
    """ ajoute un tournois de degre plus petit que le tournois de degre plus petit d'une file dans une file"""
    if(F.minDegre().degre<tournoi.degre):
        return None
    F.tournois.insert(0,tournoi)
    return F
        
def Union(F1,F2,t):
    """fait l'addition binaire avec une retenue (ici t) pour l'union de deux file binomiale"""
        
    if(t.estVide()):
        
        if(F1.estVide()):
            
            return F2
            
        if(F2.estVide()):
            
            return F1
        
        t1 = F1.minDegre()
        t2 = F2.minDegre()
        
        if(t1.degre<t2.degre):
            return ajoutMin(UnionFile(F1.reste(),F2),t1)
        if(t2.degre<t1.degre):
            return ajoutMin(UnionFile(F2.reste(),F1),t2)
        if(t1.degre == t2.degre):
            return Union(F1.reste(),F2.reste(),union2Tid(t1,t2))
                
    else:
        if(F1.estVide()):
            return UnionFile(t.file(),F2)
        if(F2.estVide()):
            return UnionFile(t.file(),F1)
        t1 = F1.minDegre()
        t2 = F2.minDegre()
        
        if(t.degre<t1.degre and t.degre<t2.degre):
            return ajoutMin(UnionFile(F1,F2),t)
        if(t.degre==t1.degre and t.degre==t2.degre):
            return ajoutMin(Union(F1.reste(),F2.reste(),union2Tid(t1,t2)),t)
        if(t.degre == t1.degre and t.degre<t2.degre):
            return Union(F1.reste(),F2,union2Tid(t,t1))
        if(t.degre < t1.degre and t.degre==t2.degre):
            return Union(F2.reste(),F1,union2Tid(t,t2))