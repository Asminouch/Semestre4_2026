## Evaluation

# QCM APRES 3 SEMAINES

qcm: biblioteque mi-periode--> Numpy et panda
derniere seance: tp noté- classification par IA
fin de periode DS numpy panda et concept IA

commandes utiles: 

Il existe d'autres méthodes (constructeurs) pour initialiser un tableau NumPy :
- `np.array(liste)` déjà vu
- `np.zeros(shape)` initialise avec des 0
- `np.ones(shape)` intialise avec des 1
- `np.full(shape, value)` intialise avec des *value*<!--- `np.empty(shape)` création du tableau sans initialiser (valeurs arbitraires) -->
- `np.arange([start], stop, [step])` initialise avec une suite de valeurs (*range*)
- `np.linspace(start, stop, num=50])` initialise avec une suite de *num* valeurs réparties de façon égale sur l'intervalle [start, stop]
- [`np.random.randn(dim0, dim1, ...)`](https://numpy.org/doc/1.16/reference/generated/numpy.random.randn.html#numpy.random.randn) initialise avec des valeurs tirées aléatoirement selon une loi normale centrée en 0 ($\mu = 0$) et de variance 1 ($\sigma^2=1$) : ${\cal N}(0,1)$ 

np.linespace(1,10,10)= les valeurs de 1à 10 le dernier élément (10) représentele nombre d'élément qu'on souhaite avoir


La méthode `np.concatenate((ArrayA, ArrayB), axis=0)` permet de concaténer deux tableaux Numpy (de formes compatibles) selon un axe :

exemple: si l'on souhaite assembler **verticalement** deux matrices M1 et M2 (ayant le même nombre de colonnes) on écrira


 M1 = np.zeros((3,2))
 M2 = np.ones((2,2))
 M3 = np.concatenate((M1, M2), axis=0)
 M3


Comme pour les listes Python, on accède aux éléments d'un tableau NumPy :
- par les indices (ex. `t[0]`, `t[-1]`, `t[1, 2]`, etc.) 
- par un slice (ex. `t[1:4]`, `t[:3]`, `t[2:4, 1:6]`, etc.)