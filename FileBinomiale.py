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
        res.tournois.append(self)
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
        return self.tournois[-1]
    
    def reste(self):
        """renvoie la file privé de son tournois de degree minimum"""
        if(self.estVide()):
            return None
        self.tournois.pop()
        return self
    
    def SuppMin(self):
        """ renvoie le tournois avec la racine la plus petite et le supprime de la file"""
        if self.tournois == []:
            return None
        tournoisP = self.tournois[0]
        minimum = tournoisP.racine
        ind = 0
        for i in range(1,len(self.tournois)):
            if(self.tournois[i].racine.inf(minimum)):
                minimum = self.tournois[i].racine
                tournoisP = self.tournois[i]
                ind = i
        
        self.tournois.pop(ind)
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
            f.tournois.append(t)
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
    F.tournois.append(tournoi)
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
    
def main(): 

    print("test ConsIter : \n")       
    l = list()
    a=cle.Cle("0x9c1f03a0d9cf510f2765bd0f226ff5dc")
    b=cle.Cle("0x10fd1015413104a2f26018d0ab77a727")
    c=cle.Cle("0x2e73d8ce4bd45923286e966bc8cf2d95")
    d=cle.Cle("0x767accd0c60c603f71a68be994019c7e")
    e=cle.Cle("0x34c63c08abab99722b945e57081288e7")
    f=cle.Cle("0x6d481adc2aeed025f0374a5982b5c23c")
    t1 = TournoisBino(a)
    t2 = TournoisBino(b)
    t3 = TournoisBino(c)
    t4 = TournoisBino(d)
    t5 = TournoisBino(e)
    t6 = TournoisBino(f)
    l.extend([t1,t2,t3,t4,t5,t6])
    print("les cles (dans des tounois binomiaux de degree 0) qui vont etre dans la file Binomiale : \n"+str(l))
    print("\n")
    print("File construite : ")
    F = FileBinomial()
    F.ConsIter(l)
    print(F)
    print("cette file a pour tournois : ")
    for c in F.tournois:
        print(c)
    print("======================================")
    print("\n")
    print("test SuppMin sur cette file :")
    print("la racine la plus petite est : "+str(F.SuppMin()))
    print("la file apres la suppression de la racine la plus petite est :")
    print(F)
    print("cette nouvelle file a pour tournois : ")
    for c in F.tournois:
        print(c)
    print("======================================")
    print("\n")
    print("test Union de deux files: ")
    a=cle.Cle("0x9a5cdb45f1951a3a82b09af737fdc9aa")
    b=cle.Cle("0x53f7ffe901f3686b875af337039ee262")
    c=cle.Cle("0xa89aa39aa55e5bb5fb33a1802b248207")
    d=cle.Cle("0x8aefe5f306ac962bcbdb63aeb58d1e35")
    e=cle.Cle("0x85c3d80bfe89b91033b23cd659cddb08")
    f=cle.Cle("0x45484c820aee4c04ef89c1db9bb3eaf5")
    t1 = TournoisBino(a)
    t2 = TournoisBino(b)
    t3 = TournoisBino(c)
    t4 = TournoisBino(d)
    t5 = TournoisBino(e)
    t6 = TournoisBino(f)
    l = list()
    l.extend([t1,t2,t3,t4,t5,t6])
    F2 = FileBinomial()
    F2.ConsIter(l)
    print("premiere file : ")
    print(F)
    print("cette file a pour tournois : ")
    for c in F.tournois:
        print(c)
    print("deuxieme file : ")
    print(F2)
    print("cette file a pour tournois : ")
    for c in F2.tournois:
        print(c)
    print("file union des deux :")
    F3 = UnionFile(F,F2)
    print(F3)
    print("cette file a pour tournois : ")
    for c in F3.tournois:
        print(c)
    
    print("======================================")
    print("\n")
    
    print("Test sur les jeu1 et jeu5 de taille 50 000\n")
    fichier = open("cles_alea/jeu_5_nb_cles_50000.txt",'r')
    param = list()
    for line in fichier:
        param.append(TournoisBino(cle.Cle(line)))
    fichier.close()
    print("ConsIter sur une liste de 50 000 cle")
    fileBino = FileBinomial()
    fileBino.ConsIter(param)
    print(fileBino)
    print("cette file a pour tournois : ")
    for c in fileBino.tournois:
        print(c)
        
    print("Union de deux tas construit avec 50 000 clé chacun")
    f2 = open("cles_alea/jeu_1_nb_cles_50000.txt",'r')
    param2 = list()
    for line in f2:
        param2.append(TournoisBino(cle.Cle(line)))
    f2.close()
    fileBino2 = FileBinomial()
    fileBino2.ConsIter(param)
    print("premiere file : ")
    print(fileBino)
    print("deuxieme file : ")
    print(fileBino2)
    print("file union des deux :")
    F3 = UnionFile(fileBino,fileBino2)
    print(F3)
    print("cette file a pour tournois : ")
    for c in F3.tournois:
        print(c)
    print("======================================")
    print(F3.minDegre())
if __name__ == "__main__":
    main()