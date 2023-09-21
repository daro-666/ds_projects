import os
from sklearn.datasets import make_moons
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras import backend as K


K.clear_session()

X, y = make_moons(n_samples=500, noise=0.1, random_state=42)

model = Sequential(
    [
        Dense(units=1000, input_shape=(2,)),
        Activation("elu"),

        Dense(units=100),
        Activation("elu"),

        Dense(units=10),
        Activation("elu"),

        Dense(units=1),
        Activation("sigmoid")
    ]
    )

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"],
    #jit_compile=True
)

fit = model.fit(X, y, epochs=150, batch_size=256, validation_split=0.2, verbose=1)

ypred = model.predict(X)

cmap = 'cool'
plt.style.use('ggplot')
plt.rcParams["figure.figsize"] = (12,12)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap)
ax1.title.set_text("True labels") 
ax2.scatter(X[:, 0], X[:, 1], c=ypred, cmap=cmap)
ax2.title.set_text("Predicted labels")
ax3.plot(fit.history["accuracy"], label="train data")
ax3.plot(fit.history["val_accuracy"], label="test data")
ax3.title.set_text("Accuracies")
ax3.legend()
ax4.plot(fit.history["loss"], label="train data")
ax4.plot(fit.history["val_loss"], label="test data")
ax4.title.set_text("Losses")
ax4.legend()
plt.savefig("Moonplots.pdf")