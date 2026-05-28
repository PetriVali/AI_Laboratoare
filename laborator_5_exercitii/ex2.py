from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Exercitiul 2 - Impartirea setului in antrenare si testare")
print("Forma X_train:", X_train.shape)
print("Forma X_test:", X_test.shape)
print("Forma Y_train:", Y_train.shape)
print("Forma Y_test:", Y_test.shape)
