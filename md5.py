""" XD c'est mega chaud a implementer en vrai... https://equi4.com/md5/"""
import math
r = []
k = [None]*63

r[0:16] = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22]
r[16:32] = [5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20]
r[32:48] = [4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23]
r[48:64] = [6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]

print(len(k))
#MD5 utilise des sinus d'entiers pour ses constantes :
for i in range(0,63):
    k[i] = math.floor(abs(math.sin(i + 1)) * 2**32)

h0 = 0x67452301
h1 = 0xEFCDAB89
h2 = 0x98BADCFE
h3 = 0x10325476




#Les boucles principales
def F(b, c, d):
    return (b & c) | (~b & d)

def G(b, c, d):
    return (b & d) | (c & ~d)

def H(b, c, d):
    return b ^ c ^ d

def I(b, c, d):
    return c ^ (b | ~d)

def add_binaire(*args) :
    return bin(sum(int(x, 2) for x in args))

print(k)
