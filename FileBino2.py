import cle

class TournoisBino:
    
    def __init__(self):
        self.keyNode = None
        self.enfants = [self] #le premier enfant c'est enfants[1]
        self.degre = 0
        self.ind = 0

    def Ajout(self,add):
        
        self.enfants.append(add)
        self.degre = self.degre + 1
        #self.remonte(self.degre)
   
    def ConsIter(self, vals):
	#if(len(vals) != math.pow(2,math.floor(math.log(len(vals),2)))):
	#	return None
        
        self.key = vals[0]
        self.enfants[0] = self
        for i in range(1,len(vals)):
            self.Ajout(vals[i])

    def getDegre(self):
        return degree

    """def remonte(self, ind):
        while ind != 0:
            if (self.enfants[ind//2].keyNode.sup(self.tas[ind].keyNode)):
                tmp = self.tas[ind//2]
                self.tas[ind//2] = self.tas[ind]
                self.tas[ind] = tmp
                ind = ind//2
            else:
                break

    def descend(self,ind):
        while ((ind * 2) <= self.degre):
            if (ind * 2 + 1 > self.degre):
                minFils = ind * 2
            else:
                if( self.enfants[ind*2].keyNode.inf( self.tas[ind*2+1].keyNode)):
                    minFils = ind * 2
                else:
                    minFils = ind * 2 + 1
            
            if (self.tas[minFils].keyNode.inf(self.tas[ind].keyNode)):
                tmp = self.tas[ind]
                self.tas[ind] = self.tas[minFils]
                self.tas[minFils] = tmp

            ind = minFils"""
    
class FileBinomial:
    def __init__(self):
        self.tournois = []
        
    def Union(self, h):
        self.combine_roots(h)
        if self.tournois == []:
            return None
        i = 0
        while i < len(self.tournois)-1:
            current = self.tournois[i]
            after = self.tournois[i + 1]
            if current.degre == after.degre:
                if (i + 1 < len(self.tournois) - 1 and self.tournois[i + 2].degre == after.degre):
                    after_after = self.tournois[i + 2]
                    if after.key.inf(after_after.key):
                        after.Ajout(after_after)
                        del self.tournois[i + 2]
                    else:
                        after_after.Ajout(after)
                        del self.tournois[i + 1]
                else:
                    if current.key.inf(after.key):
                        current.Ajout(after)
                        del self.tournois[i + 1]
                    else:
                        after.Ajout(current)
                        del self.tournois[i]
            i = i + 1
            
    def combine_roots(self, h):
        self.tournois.extend(h.tournois)
        self.tournois = sorted(self.tournois,key = lambda tournoi : tournoi.degre)

    def SuppMin(self):
        if self.tournois == []:
            return None
        tournoisP = self.tournois[0]
        for t in self.tournois:
            if t.key.inf(tournoisP.key):
                tournoisP = t
        self.tournois.remove(tournoisP)
        h = FileBinomial()
        h.tournois = tournoisP.enfants
        self.Union(h)
 
        return tournoisP.key


    def AjoutTournois(self, t):
        f = FileBinomial()
        f.tournois.append(t)
        self.Union(f)
        
l = list()
a=cle.Cle("0x9c1f03a0d9cf510f2765bd0f226ff5dc")
b=cle.Cle("0x10fd1015413104a2f26018d0ab77a727")
c=cle.Cle("0x2e73d8ce4bd45923286e966bc8cf2d95")
d=cle.Cle("0x767accd0c60c603f71a68be994019c7e")
e=cle.Cle("0x34c63c08abab99722b945e57081288e7")
f=cle.Cle("0x6d481adc2aeed025f0374a5982b5c23c")
l.append(a)
l.append(b)
l.append(c)
l.append(d)
l.append(e)
l.append(f)
t1 = TournoisBino()
t1.ConsIter(l[0:2])
t2 = TournoisBino()
t2.ConsIter(l[2:5])
file = FileBinomial()
file.AjoutTournois(t2)
file.AjoutTournois(t1)

A=cle.Cle("0xb26a633d855b8b0af4c692dda999ddcc")
B=cle.Cle("0x31a872636ac53ed0dd00b3f27470bbb4")
C=cle.Cle("0xd78cdbe82edab23a56f47f978fcbb8be")
D=cle.Cle("0xe76f477e1431b3577ebf079fc7e4493e")
E=cle.Cle("0x4c97cd1b0b09e387826e0d9d68d4071d")
l = list()
l.append(A)
l.append(B)
l.append(C)
l.append(D)
l.append(E)
t1 = TournoisBino()
t1.ConsIter(l[0:1])
t2 = TournoisBino()
t2.ConsIter(l[1:4])
file2 = FileBinomial()
file2.AjoutTournois(t2)
file2.AjoutTournois(t1)
file2.Union(file)

for x in file2.tournois:
    print(x.degre)
