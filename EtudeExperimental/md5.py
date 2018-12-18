import math


k = []*64
r = []*64

#Initialisation de r
r =  [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
      5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
      4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
      6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]

#Initialisation de k
for i in range(0, 64):
    k.append(math.floor(abs(math.sin(i+1)) * 2**32))

#Initialisation de nos variables A B C D
h0 =0x67452301
h1 =0xEFCDAB89
h2 =0x98BADCFE
h3 =0x10325476

#Les fonctions outils
def F(b, c, d):
    return (b & c) | (~b & d)

def G(b, c, d):
    return (b & d) | (c & ~d)

def H(b, c, d):
    return b ^ c ^ d

def I(b, c, d):
    return c ^ (b | ~d)

def leftrotate(x, y):
    x &= 0xFFFFFFFF # le '&= 0xFFFFFFFF' sert a garder nos variables sur 32 bits sinon l'algo ne marche pas
    return ((x<<y) | (x>>(32-y))) & 0xFFFFFFFF

def padding(message):
    msg = bytearray(message,"utf-8") # On convertit notre message en bytes
    lenByte = (8 * len(msg)) & 0xffffffffffffffff # On a la taille en de notre msg en bytes avec len(msg), on multiplie par 8 pour avoir la taille en bit (8 bits = 1 bytes)
    # on veux ajouter le bit '1' a la fin du message qui est rpz en bytes on vas donc devoir ajouter un bytes a ce gros message avec 1 au debut (pour l'avoir a la fin du mes) et des 0 partout apres
    msg.append(0x80) # 0x80 -> 1 byte = 1000 0000 en bits
    # On veux ajouter le bit '0' jusqu'à ce que la taille du message en bit soit egale à 448 (mod 512)
    #la taille du message en bit est comme au dessus : 8*len(msg) avec msg une representation en byte
    while (8*len(msg)) % 512 != 448:
        msg.append(0)
    # On ajoute la taille initial du message a la fin du message (elle vas occuper les 64 derniers bit)
    #elle est en little endiant 
    msg += lenByte.to_bytes(8, byteorder='little')
    return msg

# MD5 l'algo du wiki
def md5(msg):
    
    # Preparation du message
    message = padding(msg)
    #len(msg) apres le padding est un multiple de 512 bit, comme le message est en bytes il aura comme len un multiple de 512/8 
    #c'est pour ca que sa len ici est 64 (le message etais court on a eu que un bloc de 512 bits == 64 bytes *8)
    
    h0 =0x67452301
    h1 =0xEFCDAB89
    h2 =0x98BADCFE
    h3 =0x10325476
    
    
    # le nb de tour qu'on vas faire ici vas dependre du message de base et en combien de bloc de 512 bits il a du etre subdiviser si il est court en general on rentre que une fois dans cette boucle si c'est un paragraphe on aura donc plusieur block de 512 bit a traiter
    # On fait un range avec un pas de 64 car on regarde bloc de 512 bits par bloc de 512 bits
    for i in range(0, len(message), 64):
        
        #Initialisation des valeurs de hachage
        AA = h0
        BB = h1
        CC = h2
        DD = h3
        # m est le bloc actuel de 512 bit
        m = message[i : i + 64]
        for j in range(64):
            # Boucle principale on applique nos formules
            if (0 <= j | j < 16):
                f = F(BB,CC,DD)
                g = j
            elif (j >= 16 | j < 32):
                f = G(BB,CC,DD)
                g = (5 * j + 1) % 16
            elif (j >= 32 | j < 48):
                f = H(BB,CC,DD)
                g = (3 * j + 5) % 16
            elif (j >= 48 | j < 64):
                f = I(BB,CC,DD)
                g = (7 * j) % 16
            # On subdivide le bloc en mini bloc et on mets les mini bloc en little endiant
            w = int.from_bytes(m[4*g:4*g+4],byteorder='little')
            # ont mets a jour nos variables
            tmp = AA+f+k[j]+w & 0xFFFFFFFF # Apres chaque operation qui change une valeur on veux etre sur qu'elle reste sur 32 bits d'où le &=0FFFFFFFF
            AA = DD
            DD = CC
            CC = BB
            BB = (BB+leftrotate(tmp,r[j])) & 0xFFFFFFFF


        # On ajoute le resultat a chaque bloc au fur et a mesure qu'on parcours nos bloc de 512 bits
        h0 += AA
        h0 &= 0xFFFFFFFF
        h1 += BB
        h1 &= 0xFFFFFFFF
        h2 += CC
        h2 &= 0xFFFFFFFF
        h3 += DD
        h3 &= 0xFFFFFFFF
        
    # On reconstitue le message modifier par md5 ce message est sur 128 bits et on a h0 qui correspond au 32 premiers bits h1 au 32 suivant etc... d'où les decalage de 32, de 64, de 96 pour reconstituer le message sur 128 bits
    x = h0 + (h1 << 32) + (h2 << 64) + (h3 << 96)
    
    # L'algo nous fournis un message en little endian ici on le remets dans le bon sens pour pouvoir le lire c'est tout 
    return hexAffiche(x.to_bytes(16, byteorder='little'))

# Return md5 in hexadecimal
def hexAffiche(digest):
    return '{:032x}'.format(int.from_bytes(digest, byteorder='big'))

print(md5("Merci mon gars Durassel"))
print(md5("of"))