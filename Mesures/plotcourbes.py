import matplotlib.pyplot as plt


plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 9.40,12.50 ,75.0 ,150.0 ,303.15,746.94],label="File Binomiale",color="blue")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 9.40,12.50 ,75.0 ,150.0 ,303.15,746.94],'x',color="blue")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 3.125,4.9 ,62.5 ,128.13,281.24,756.3],label="Tas Min Arbre",color="red")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 3.125,4.9 ,62.5 ,128.13,281.24,756.3],'x',color="red")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.158,0.298, 0.73, 1.36, 7.02,14.49,31.06,78.94],label="Tas Min Tableau",color="pink")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.158,0.298, 0.73, 1.36, 7.02,14.49,31.06,78.94],'x',color="pink")
plt.ylabel('temps en miliseconde')
plt.xlabel('taille des listes')
plt.title("Mesures ConsIter ")
plt.legend()
plt.savefig('timeConsIter.png')
plt.show()

plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 3.125, 3.125,25.01,68.737,125.84,240.650],label="Tas Min Tableau",color="pink")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 3.125, 3.125,25.01,68.737,125.84,240.650],'x',color="pink")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [3.125, 3.125, 6.25,9.37 ,53.114 ,134.3,265.66,680.0],label= "File Binomiale",color="blue")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [3.125, 3.125, 6.25,9.37 ,53.114 ,134.3,265.66,680.0],'x',color="b")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 12.46, 18.746 ,121.00 ,337.53 ,737.5 ,1228.35],label = "Tas Min Arbre",color="red")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 12.46, 18.746 ,121.00 ,337.53 ,737.5 ,1228.35],'x',color="red")
plt.ylabel('temps en miliseconde')
plt.xlabel('nombre d\'unions faites')
plt.title("Mesures Union  ")
plt.legend()
plt.savefig('timeUnion.png')
plt.show()









