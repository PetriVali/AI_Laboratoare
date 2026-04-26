from sklearn.datasets import load_iris
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data
Y = iris.target
targets = iris.target_names

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, Y_train)
Y_pred = knn.predict(X_test_scaled)
cm = confusion_matrix(Y_test, Y_pred)
print("Matricea de confuzie: ")
print(cm)
report = classification_report(Y_test, Y_pred, target_names=targets)
print("Raport de clasificare: ")
print(report)
