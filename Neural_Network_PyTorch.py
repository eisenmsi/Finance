import pandas as pd
import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader


def normalize(x, m, s):
    return (x - m) / s


data = pd.read_csv("CSV_data.csv")
data = data.sample(frac=1)
data_features = data.copy()
data_labels = data_features.pop("return_stock(+1)")
data_features = np.array(data_features)
data_labels = np.array(data_labels)

train_features = data_features[0:60].astype('float32')
train_labels = data_labels[0:60].astype('float32')
dev_features = data_features[60:80].astype('float32')
dev_labels = data_labels[60:80].astype('float32')
test_features = data_features[80:].astype('float32')
test_labels = data_labels[80:].astype('float32')


class Data(torch.utils.data.Dataset):
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        return self.features[idx], np.array([self.labels[idx]])


training_data = Data(train_features, train_labels)
dev_data = Data(dev_features, dev_labels)
test_data = Data(test_features, test_labels)

batch_size = 10

# Create data loaders.
train_dataloader = DataLoader(training_data, batch_size=batch_size)
dev_dataloader = DataLoader(dev_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

device = "cpu"

m = train_features.mean(0)
s = train_features.std(0)


# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(7, 16)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(16, 16)
        self.linear3 = nn.Linear(16, 1)

    def forward(self, x):
        x = normalize(x, m, s)
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        x = self.relu(x)
        x = self.linear3(x)
        return x


model = NeuralNetwork().to(device)

loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.0019, weight_decay=0.00001)


def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Compute prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


def test(dataloader, model, loss_fn):
    num_batches = len(dataloader)
    model.eval()
    test_loss = 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
    test_loss /= num_batches
    print(f"Avg loss: {test_loss:>8f} \n")


epochs = 500
for t in range(epochs):
    print(f"Epoch {t + 1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer)
    test(train_dataloader, model, loss_fn)
    test(dev_dataloader, model, loss_fn)
print("Done!")
