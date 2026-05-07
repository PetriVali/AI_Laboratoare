from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
print(df.head(5))
features = diabetes.feature_names
print("Numele caracteristicilor: ", features)
print("Informatii statistice despre date:")
print(df.describe())
#5
plt.hist(df['bmi'], bins=25, edgecolor='black')
plt.title('Distributia caracteristicii BMI')
plt.xlabel('BMI')
plt.ylabel('Frecventa')
plt.grid()
plt.show()
#6
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(df['bmi'], diabetes.target, alpha=0.5)
plt.title('BMI vs Target')
plt.xlabel('BMI')
plt.ylabel('Target')
plt.grid()
plt.subplot(1, 2, 2)
plt.scatter(df['age'], diabetes.target, alpha=0.5)
plt.title('Age vs Target')
plt.xlabel('Age')
plt.ylabel('Target')
plt.grid()
plt.show()
#7
X = df[['bmi']]
y = diabetes.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=50)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
plt.scatter(X_test, y_test, color='blue', label='Date de testare')
plt.plot(X_test, y_pred, color='red', label='Linia de regresie')
plt.title('Regresie liniară simplă: BMI vs Target')
plt.xlabel('BMI')
plt.ylabel('Target')
plt.legend()
plt.grid()
plt.show()
mse = mean_squared_error(y_test, y_pred)
print(f"Eroarea pătratică medie (MSE): {mse:.2f}")
#8
xx = df[['bmi', 'bp']]
yy = diabetes.target
X_train, X_test, y_train, y_test = train_test_split(xx, yy, test_size=0.2)
model_2 = LinearRegression()
model_2.fit(X_train, y_train)
y_pred_2 = model_2.predict(X_test)

for feature, coeficient in zip(xx.columns, model_2.coef_):
    print(f"Coeficient pentru {feature}: {coeficient:.2f}")

r2 = r2_score(y_test, y_pred_2)
print(f"Scorul R2 pentru regresia multipla: {r2:.2f}")
