import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

wine = load_wine(as_frame=True)
df = wine.frame

print("Primele 5 randuri din setul de date wine:")
print(df.head())
print()

print("Toate caracteristicile disponibile:")
print(wine.feature_names)
print()

X = df[["alcohol", "flavanoids"]]
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X_train, y_train)

plt.figure(figsize=(12, 8))
plot_tree(
    model,
    feature_names=["alcohol", "flavanoids"],
    class_names=wine.target_names,
    filled=True,
    rounded=True,
)
plt.title("Arbore de decizie limitat la adancimea 2")
plt.tight_layout()
plt.show()

print("Structura arborelui a fost afisata cu plot_tree")
print()

print("Interpretarea primelor doua noduri:")
arbore = model.tree_

conditie_nod_0 = f"{['alcohol', 'flavanoids'][arbore.feature[0]]} <= {arbore.threshold[0]:.3f}"
clasa_nod_0 = wine.target_names[arbore.value[0][0].argmax()]
print(f"Nodul 0: conditie = {conditie_nod_0}")
print(f"Nodul 0: clasa prezisa = {clasa_nod_0}")

conditie_nod_1 = f"{['alcohol', 'flavanoids'][arbore.feature[1]]} <= {arbore.threshold[1]:.3f}"
clasa_nod_1 = wine.target_names[arbore.value[1][0].argmax()]
print(f"Nodul 1: conditie = {conditie_nod_1}")
print(f"Nodul 1: clasa prezisa = {clasa_nod_1}")
print()

model_complet = DecisionTreeClassifier(max_depth=None, random_state=42)
model_complet.fit(X_train, y_train)
y_pred = model_complet.predict(X_test)
acuratete = accuracy_score(y_test, y_pred)

print("Acuratete pe setul de testare pentru arborele complet (2 caracteristici):")
print(f"{acuratete:.4f}")
print()

X_toate = df[wine.feature_names]

X_train_toate, X_test_toate, y_train_toate, y_test_toate = train_test_split(
    X_toate, y, test_size=0.3, random_state=42, stratify=y
)

model_toate = DecisionTreeClassifier(max_depth=None, random_state=42)
model_toate.fit(X_train_toate, y_train_toate)
y_pred_toate = model_toate.predict(X_test_toate)
acuratete_toate = accuracy_score(y_test_toate, y_pred_toate)

print("Acuratete pe setul de testare pentru arborele complet (toate cele 13 caracteristici):")
print(f"{acuratete_toate:.4f}")
print()

importante = pd.Series(
    model_toate.feature_importances_, index=wine.feature_names
).sort_values(ascending=False)

print("Importanta caracteristicilor:")
print(importante)
print()

print("Caracteristicile care influenteaza cel mai mult deciziile arborelui sunt:")
print(", ".join(importante.head(3).index))
