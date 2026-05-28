from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
features = iris.feature_names
targets = iris.target_names

print("Exercitiul 1 - Explorarea setului de date Iris")
print(f"Numar de exemple: {X.shape[0]}")
print(f"Dimensiunea caracteristicilor: {X.shape[1]}")
print("Denumirile coloanelor:", features)
print("Numele claselor:", targets)
