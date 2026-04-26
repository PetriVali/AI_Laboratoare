from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
Y = iris.target

print("Exercitiu 2")
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)
print("Forma setului de antrenare: ", X_train.shape, Y_train.shape)
print("Forma setului de testare: ", X_test.shape, Y_test.shape)
print("--" * 20)
