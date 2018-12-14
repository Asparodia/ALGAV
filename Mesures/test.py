import matplotlib.pyplot as plt
#plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 3.125, 3.125,12.25,21.88,46.885,115.645])
#plt.ylabel('temps en miliseconde')
#plt.xlabel('nb d\'elements de la liste')
#plt.title("Mesures ConsIter sur le tas min utilisant un tableau ")
#plt.savefig('timeConsIterTasMinTab.png')
#plt.show()

#plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 3.125, 3.125,25.01,68.737,125.84,240.650])
#plt.ylabel('temps en miliseconde')
#plt.xlabel('nb d\'union faite')
#plt.title("Mesures Union sur le tas min utilisant un tableau ")
#plt.savefig('timeUnionTasMinTab.png')
#plt.show()


#plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 0.0, 3.87 ,19.53 ,23.50 ,50.88,120])
#plt.ylabel('temps en miliseconde')
#plt.xlabel('taille des fichiers unis')
#plt.title("Mesures Union sur le tas min utilisant un tableau ")
#plt.savefig('timeUnionTasMinTabV2.png')
#plt.show()

#plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 9.40,12.50 ,75.0 ,150.0 ,303.15,746.94])
#plt.ylabel('temps en miliseconde')
#plt.xlabel('taille des listes')
#plt.title("Mesures ConsIter sur les FileBino ")
#plt.savefig('timeConsIterFileBino.png')
#plt.show()

#plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [3.125, 3.125, 6.25,9.37 ,53.114 ,134.3,265.66,680.0])
#plt.ylabel('temps en miliseconde')
#plt.xlabel('nb d\' union effectuées')
#plt.title("Mesures Union sur les FileBino ")
#plt.savefig('timeUnionFileBino.png')
#plt.show()

#plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 3.125,4.9 ,62.5 ,128.13,281.24,756.3])
#plt.ylabel('temps en miliseconde')
#plt.xlabel('nb d\'element de la liste')
#plt.title("Mesures ConsIter sur les tas min utilisant un arbre ")
#plt.savefig('timeConsiterTasArbre.png')
#plt.show()



#plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 12.46, 18.746 ,121.00 ,337.53 ,737.5 ,1228.35])
#plt.ylabel('temps en miliseconde')
#plt.xlabel('nb d\'union effectuées')
#plt.title("Mesures Union sur les tas min utilisant un arbre ")
#plt.savefig('timeUnionTasArbre.png')
#plt.show()

plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 3.9, 7.8, 11.7 ,98,200,307,1077])
plt.ylabel('temps en miliseconde')
plt.xlabel('taille des fichiers unis')
plt.title("Mesures Union sur les tas min utilisant un arbre ")
plt.savefig('timeUnionTasArbreV2.png')
plt.show()

