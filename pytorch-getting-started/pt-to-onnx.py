import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import torch.optim as optim
import torch.nn as nn
import torch
import torch.nn.functional as F
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type=str, help="relative path to a .pt file")
args = parser.parse_args()


iris = load_iris()

# Create X and y data
X = iris.data
y = iris.target

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create the model
#############################################################################################

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.lin1 = nn.Linear(4, 50)
        self.lin2 = nn.Linear(50, 50)
        self.out = nn.Linear(50, 3)

    def forward(self, x):
        x = F.relu(self.lin1(x))
        x = F.relu(self.lin2(x))
        x = self.out(x)
        return x


net = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters())

# Train the network
#############################################################################################
for epoch in range(50):
    inputs = torch.autograd.Variable(torch.Tensor(X_train).float())
    targets = torch.autograd.Variable(torch.Tensor(y_train).long())

    optimizer.zero_grad()
    out = net(inputs)
    loss = criterion(out, targets)
    loss.backward()
    optimizer.step()
    
torch.save(net, "net.pt")
print(args.path, os.path.exists(args.path))
net = torch.load("net.pt")
dirname=os.path.dirname(args.path)
filename=os.path.splittext(os.path.basename(args.path))[0]
dummy_input = torch.randn(10, 3, 416, 416, device='cpu') # 10 random tensors for the ONNX exporter to use to generate trace of NN
torch.onnx.export(net, dummy_input, dirname + "/" + filename + ".onnx")