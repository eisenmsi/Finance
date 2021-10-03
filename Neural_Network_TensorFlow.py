import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing


def mean_error(predictions, labels):
    mean = 0
    for i in range(len(predictions)):
        mean += abs(np.squeeze(predictions[i]) - labels[i])
    return mean / len(predictions)


data = pd.read_csv("CSV_data.csv")
data = data.sample(frac=1)
data_features = data.copy()
data_labels = data_features.pop("return_stock(+1)")
data_features = np.array(data_features)
data_labels = np.array(data_labels)

train_features = data_features[0:60]
train_labels = data_labels[0:60]
dev_features = data_features[60:80]
dev_labels = data_labels[60:80]
test_features = data_features[80:]
test_labels = data_labels[80:]

normalize = preprocessing.Normalization()
normalize.adapt(train_features)

model = tf.keras.Sequential([
    normalize,
    layers.Dense(16, activation='relu'), #kernel_regularizer=tf.keras.regularizers.L2(0.1)),
    layers.Dense(16, activation='relu'), #kernel_regularizer=tf.keras.regularizers.L2(0.1)),
    layers.Dense(1)
])

model.compile(loss=tf.losses.MeanSquaredError(), optimizer=tf.optimizers.Adam())

model.fit(train_features, train_labels, epochs=500)
train_predictions = model(train_features).numpy()

print("Mean error test:", mean_error(train_predictions, train_labels))

print("evaluate:")
model.evaluate(dev_features, dev_labels)
dev_predictions = model(dev_features).numpy()

print("Mean error dev:", mean_error(dev_predictions, dev_labels))
