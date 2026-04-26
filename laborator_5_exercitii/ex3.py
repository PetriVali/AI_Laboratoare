from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Exercitiu 3")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Primele 3 exemple inainte de scalare: ")
print(X_train[:3])
print("Primele 3 exemple dupa scalare: ")
print(X_train_scaled[:3])
print("--" * 20)
