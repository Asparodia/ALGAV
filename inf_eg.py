def inf(clef1, clef2):
    listeClef1 = []
    listeClef2 = []
    listeClef1.append(clef1[2:10])
    listeClef1.append(clef1[10:18])
    listeClef1.append(clef1[18:26])
    listeClef1.append(clef1[26:34])

    listeClef2.append(clef2[2:10])
    listeClef2.append(clef2[10:18])
    listeClef2.append(clef2[18:26])
    listeClef2.append(clef2[26:34])
    for i in range(3, 0, -1):
        if listeClef1[i] < listeClef2[i]:
            return True
        elif listeClef1[i] > listeClef2[i]:
            return False

#Return false si faut mais ne retourne rien si vrai
def eg(clef1, clef2):
    listeClef1 = []
    listeClef2 = []
    listeClef1.append(clef1[2:10])
    listeClef1.append(clef1[10:18])
    listeClef1.append(clef1[18:26])
    listeClef1.append(clef1[26:34])

    listeClef2.append(clef2[2:10])
    listeClef2.append(clef2[10:18])
    listeClef2.append(clef2[18:26])
    listeClef2.append(clef2[26:34])
    for i in range(3, 0, -1):
        if listeClef1[i] < listeClef2[i]:
            return False
        elif listeClef1[i] > listeClef2[i]:
            return False

        elif i == 0 :
            if listeClef1[0] == listeClef2[0]:
                return True
