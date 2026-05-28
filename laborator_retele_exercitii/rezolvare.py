import matplotlib.pyplot as plt

try:
    import tensorflow as tf
except ImportError as exc:
    raise ImportError(
        "Acest script necesita TensorFlow. Instaleaza pachetul cu `pip install tensorflow` "
        "intr-un mediu compatibil."
    ) from exc


tf.random.set_seed(42)

fashion_class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

rezultate = {}

print("=" * 70)
print("Experiment de baza pe MNIST: 128 neuroni, 5 epoci, activare relu")

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
class_names = [str(index) for index in range(10)]

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

model = tf.keras.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(x_train, y_train, epochs=5, validation_split=0.1, verbose=2)
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)

rezultate["baza"] = accuracy

print(f"Loss pe setul de test: {loss:.4f}")
print(f"Acuratete pe setul de test: {accuracy:.4f}")

index = 0
probabilities = model.predict(x_test[index : index + 1], verbose=0)[0]
predicted_class = int(tf.argmax(probabilities).numpy())
real_class = int(y_test[index])

plt.figure(figsize=(4, 4))
plt.imshow(x_test[index], cmap="gray")
plt.title(
    f"MNIST\nReal: {class_names[real_class]} | Predictie: {class_names[predicted_class]}"
)
plt.axis("off")
plt.tight_layout()
plt.show()

print(
    f"Imagine afisata pentru MNIST: clasa reala = {class_names[real_class]}, "
    f"predictia modelului = {class_names[predicted_class]}"
)

print("\n" + "=" * 70)
print("Modificare numar de neuroni: 64 neuroni")

model = tf.keras.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(x_train, y_train, epochs=5, validation_split=0.1, verbose=2)
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
rezultate["64_neuroni"] = accuracy

print(f"Loss pe setul de test: {loss:.4f}")
print(f"Acuratete pe setul de test: {accuracy:.4f}")

print("\n" + "=" * 70)
print("Modificare numar de neuroni: 256 neuroni")

model = tf.keras.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(256, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(x_train, y_train, epochs=5, validation_split=0.1, verbose=2)
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
rezultate["256_neuroni"] = accuracy

print(f"Loss pe setul de test: {loss:.4f}")
print(f"Acuratete pe setul de test: {accuracy:.4f}")

print("\n" + "=" * 70)
print("Test cu mai putine epoci: 3 epoci")

model = tf.keras.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(x_train, y_train, epochs=3, validation_split=0.1, verbose=2)
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
rezultate["3_epoci"] = accuracy

print(f"Loss pe setul de test: {loss:.4f}")
print(f"Acuratete pe setul de test: {accuracy:.4f}")

print("\n" + "=" * 70)
print("Test cu mai multe epoci: 8 epoci")

model = tf.keras.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(x_train, y_train, epochs=8, validation_split=0.1, verbose=2)
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
rezultate["8_epoci"] = accuracy

print(f"Loss pe setul de test: {loss:.4f}")
print(f"Acuratete pe setul de test: {accuracy:.4f}")

print("\n" + "=" * 70)
print("Schimbare functie de activare din relu in tanh")

model = tf.keras.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="tanh"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(x_train, y_train, epochs=5, validation_split=0.1, verbose=2)
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
rezultate["tanh"] = accuracy

print(f"Loss pe setul de test: {loss:.4f}")
print(f"Acuratete pe setul de test: {accuracy:.4f}")

print("\n" + "=" * 70)
print("Inlocuire set de date MNIST cu Fashion MNIST")

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
class_names = fashion_class_names

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

model = tf.keras.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(x_train, y_train, epochs=5, validation_split=0.1, verbose=2)
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
rezultate["fashion_mnist"] = accuracy

print(f"Loss pe setul de test: {loss:.4f}")
print(f"Acuratete pe setul de test: {accuracy:.4f}")

index = 0
probabilities = model.predict(x_test[index : index + 1], verbose=0)[0]
predicted_class = int(tf.argmax(probabilities).numpy())
real_class = int(y_test[index])

plt.figure(figsize=(4, 4))
plt.imshow(x_test[index], cmap="gray")
plt.title(
    f"Fashion MNIST\nReal: {class_names[real_class]} | "
    f"Predictie: {class_names[predicted_class]}"
)
plt.axis("off")
plt.tight_layout()
plt.show()

print(
    f"Imagine afisata pentru Fashion MNIST: clasa reala = {class_names[real_class]}, "
    f"predictia modelului = {class_names[predicted_class]}"
)

print("\nRezumat comparativ:")
diferenta = rezultate["64_neuroni"] - rezultate["baza"]
semn = "+" if diferenta >= 0 else ""
print(f"64 neuroni: {rezultate['64_neuroni']:.4f} ({semn}{diferenta:.4f} fata de baza)")

diferenta = rezultate["256_neuroni"] - rezultate["baza"]
semn = "+" if diferenta >= 0 else ""
print(f"256 neuroni: {rezultate['256_neuroni']:.4f} ({semn}{diferenta:.4f} fata de baza)")

diferenta = rezultate["3_epoci"] - rezultate["baza"]
semn = "+" if diferenta >= 0 else ""
print(f"3 epoci: {rezultate['3_epoci']:.4f} ({semn}{diferenta:.4f} fata de baza)")

diferenta = rezultate["8_epoci"] - rezultate["baza"]
semn = "+" if diferenta >= 0 else ""
print(f"8 epoci: {rezultate['8_epoci']:.4f} ({semn}{diferenta:.4f} fata de baza)")

diferenta = rezultate["tanh"] - rezultate["baza"]
semn = "+" if diferenta >= 0 else ""
print(f"Activare tanh: {rezultate['tanh']:.4f} ({semn}{diferenta:.4f} fata de baza)")

print(
    f"fashion_mnist: {rezultate['fashion_mnist']:.4f} "
    "(set de date diferit fata de experimentul de baza)"
)
