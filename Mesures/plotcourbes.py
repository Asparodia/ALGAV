import matplotlib.pyplot as plt


plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [3.12, 3.12, 6.25,9.36 ,68.75 ,131.26 ,265.65,687.57],label="File Binomiale",color="blue")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [3.12, 3.12, 6.25,9.36 ,68.75 ,131.26 ,265.65,687.57],'x',color="blue")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 3.11,6.22 ,37.41 ,96.87,196.89,572.08],label="Tas Min Arbre",color="red")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 3.11,6.22 ,37.41 ,96.87,196.89,572.08],'x',color="red")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [3.12,0.0, 0.0, 0.0, 3.12,12.48,15.63,50.00],label="Tas Min Tableau",color="pink")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [3.12,0.0, 0.0, 0.0, 3.12,12.48,15.63,50.00],'x',color="pink")
plt.ylabel('temps en miliseconde')
plt.xlabel('taille des listes')
plt.title("Mesures ConsIter ")
plt.legend()
plt.savefig('timeConsIter.png')
plt.show()

plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 0.0, 0.0,21.87,28.13,84.34,196.89],label="Tas Min Tableau",color="pink")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 0.0, 0.0,21.87,28.13,84.34,196.89],'x',color="pink")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 3.12,12.50 ,37.50 ,65.61,146.90,356.28],label= "File Binomiale",color="blue")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 3.12,12.50 ,37.50 ,65.61,146.90,356.28],'x',color="b")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 9.37, 9.37 ,71.89 ,118.75 ,448.30 ,1013.89],label = "Tas Min Arbre",color="red")
plt.plot([100, 200, 500, 1000,5000,10000,20000,50000], [0.0, 0.0, 9.37, 9.37 ,71.89 ,118.75 ,448.30 ,1013.89],'x',color="red")
plt.ylabel('temps en miliseconde')
plt.xlabel('nombre d\'unions faites')
plt.title("Mesures Union  ")
plt.legend()
plt.savefig('timeUnion.png')
plt.show()









