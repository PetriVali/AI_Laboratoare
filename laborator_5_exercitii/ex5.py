import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
k_values = range(1, 16)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, Y_train)
    acc = knn.score(X_test_scaled, Y_test)
    accuracies.append(acc)

print("Exercitiul 5 - Impactul valorii k")
for k, acc in zip(k_values, accuracies):
    print(f"k = {k:2d} -> acuratete = {acc:.2f}")

plt.plot(k_values, accuracies, marker="o")
plt.title("Acuratetea KNN in functie de k")
plt.xlabel("Valoarea lui k")
plt.ylabel("Acuratete")
plt.xticks(list(k_values))
plt.grid()
plt.show()

max_accuracy = max(accuracies)
optimal_k_values = [k for k, acc in zip(k_values, accuracies) if acc == max_accuracy]
print(
    f"\nValorile optime par a fi {optimal_k_values}, deoarece obtin "
    f"cea mai mare acuratete pe setul de testare: {max_accuracy:.2f}."
)
