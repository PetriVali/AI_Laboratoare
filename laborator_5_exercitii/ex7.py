import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data[:, 2:4]
Y = iris.target
targets = iris.target_names

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, Y_train)

print("Exercitiul 7 - Vizualizarea datelor si predictia unei flori noi")
plt.figure(figsize=(8, 6))
for target in np.unique(Y):
    plt.scatter(X[Y == target, 0], X[Y == target, 1], label=targets[target])

plt.xlabel("Lungime petala")
plt.ylabel("Latime petala")
plt.title("Grafic scatter pentru lungime si latime petala")
plt.legend()
plt.grid()
plt.show()

print("Introduceti caracteristicile noii flori:")
petal_length = float(input("Lungime petala: "))
petal_width = float(input("Latime petala: "))

new_flower = np.array([[petal_length, petal_width]])
new_flower_scaled = scaler.transform(new_flower)
predicted_class = knn.predict(new_flower_scaled)
print(f"Floarea introdusa este clasificata ca: {targets[predicted_class][0]}")
