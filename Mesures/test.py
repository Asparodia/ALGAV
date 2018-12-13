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

plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 0.0, 3.87 ,19.53 ,23.50 ,50.88,120])
plt.ylabel('temps en miliseconde')
plt.xlabel('taille des fichiers unis')
plt.title("Mesures Union sur le tas min utilisant un tableau ")
plt.savefig('timeUnionTasMinTabV2.png')
plt.show()