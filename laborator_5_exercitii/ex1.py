from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
Y = iris.target
features = iris.feature_names
targets = iris.target_names

print("Exercitiu 1")
print("Numar de exemple si dimensiunea datelor: ", X.shape)
print("Numele caracteristicilor: ", features)
print("Numele claselor: ", targets)
print("--" * 20)
