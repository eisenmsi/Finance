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

train = pd.read_csv("CSV_data.csv")
train_features = train.copy()
train_labels = train_features.pop("return_stock(+1)")
train_features = np.array(train_features)
train_labels = np.array(train_labels)

dev = pd.read_csv("CSV_data_dev.csv")
dev_features = dev.copy()
dev_labels = dev_features.pop("return_stock(+1)")
dev_features = np.array(dev_features)
dev_labels = np.array(dev_labels)

test = pd.read_csv("CSV_data_test.csv")
test_features = test.copy()
test_labels = test_features.pop("return_stock(+1)")
test_features = np.array(test_features)
test_labels = np.array(test_labels)

normalize = preprocessing.Normalization()
normalize.adapt(train_features)

model = tf.keras.Sequential([
  normalize,
  layers.Dense(32, activation='relu'),
  layers.Dense(8, activation='relu'),
  layers.Dense(1)
])

model.compile(loss = tf.losses.MeanSquaredError(), optimizer = tf.optimizers.Adam())

model.fit(train_features, train_labels, epochs=500)
train_predictions = model(train_features).numpy()

print("Mean error test:", mean_error(train_predictions, train_labels))

print("evaluate:")
model.evaluate(dev_features, dev_labels)
dev_predictions = model(dev_features).numpy()

print("Mean error dev:", mean_error(dev_predictions, dev_labels))
