### Read CSV
```c
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('....csv', sep=",", decimal="." header=None si il y en a pas sinon 0, index_col=None si il y a des index sinon 0')
df
df.describe()
X = np.array(zoo.iloc[:, 1:-1])
y = np.array(zoo["type"])
print (X.shape, y.size)
```

### Valeurs manquantes
```c
df2.dropna(axis=0, inplace=True)
```

### Distribution train test
```c
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=40)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

labels1, sizes1 = np.unique(y_test, return_counts=True)
ax1.pie(sizes1, labels=labels1)
ax1.set_title("test")
labels2, sizes2 = np.unique(y_train, return_counts=True)
plt.pie(sizes2, labels=labels2)
ax2.set_title("train")
plt.show()
```

### Erreurs
```c
k_range = range(1, y_test.size+1)
errors = [error_kNN(k, X_train, y_train, X_test, y_test) for k in k_range]
plt.plot(k_range, errors)
plt.show()
```

### Normalisation
```c
from sklearn.preprocessing import MinMaxScaler
scaler1 = MinMaxScaler()

scaler1.fit(X_train)

Xn1_train = scaler1.transform(X_train)
Xn1_test = scaler1.transform(X_test)
```

### Prédiction
```c
from sklearn.neighbors import KNeighborsClassifier

neighbors = KNeighborsClassifier(n_neighbors=2)
neighbors.fit(Xn1_train, y_train)
print("Scaler 1 : ", neighbors.predict(Xn1_test))
neighbors.fit(Xn2_train, y_train)
print("Scaler 2 : ", neighbors.predict(Xn2_test))

predictions = neighbors.predict(Xn2_test)
```

### Prédictions pondérées
```c
neighbors = KNeighborsClassifier(n_neighbors=4, weights="distance")
neighbors.fit(Xn1_train, y_train)
neighbors.fit(Xn2_train, y_train)
```

### One hot encoding
```c
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
encoder.fit(X)
Xbin = encoder.transform(X)
```

### Arbre de décision
```c
from sklearn import tree

dtree = tree.DecisionTreeClassifier(criterion="entropy", min_samples_leaf=10)
dtree.fit(X_train, y_train)

# Afficher
plt.figure(figsize=(15,15))
tree.plot_tree(dtree, fontsize=6)
plt.show()
```

### Taux d'erreur arbre de décision
```c
samples = range(1, 51)

erreurs_train = [eval_DT(X_train, y_train, X_test, y_test, s)[0] for s in samples]
erreurs_test = [eval_DT(X_train, y_train, X_test, y_test, s)[1] for s in samples]

plt.plot(samples, erreurs_train, label="Taux d'erreur train")
plt.plot(samples, erreurs_test, label="Taux d'erreur test")
plt.legend()
plt.show()
```

### Over fitting
```c
predictions_train = dtree.predict(X_train)
predictions_test = dtree.predict(X_test)

error_train = sum(predictions_train!=y_train)/y_train.size
error_test = sum(predictions_test!=y_test)/y_test.size

print("Entraînement : ", error_train)
print("Test : ", error_test)

def eval_DT(X_train, y_train, X_test, y_test, min_samples_leaf):
    """Evaluer le taux d'erreurs d'un arbre de décision avec le paramètre min_samples_leaf"""
    dtree = tree.DecisionTreeClassifier(criterion="entropy", min_samples_leaf=min_samples_leaf)
    dtree.fit(X_train, y_train)
    predictions_train = dtree.predict(X_train)
    predictions_test = dtree.predict(X_test)

    error_train = sum(predictions_train!=y_train)/y_train.size
    error_test = sum(predictions_test!=y_test)/y_test.size
    return error_train, error_test

samples = range(1, 51)

erreurs_train = [eval_DT(X_train, y_train, X_test, y_test, s)[0] for s in samples]
erreurs_test = [eval_DT(X_train, y_train, X_test, y_test, s)[1] for s in samples]

plt.plot(samples, erreurs_train, label="Taux d'erreur train")
plt.plot(samples, erreurs_test, label="Taux d'erreur test")
plt.legend()
plt.show()

```
