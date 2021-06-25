import torch
import numpy as np

data = [[1, 2],
        [3, 4]]

x_data = torch.tensor(data)
print(x_data)

np_data = np.array(data)
x_np = torch.from_numpy(np_data)
print(x_np)

x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")

shape = (2, 3)
tensor = torch.rand(shape)
print(f"Random Tensor: \n {tensor} \n")
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

tensor = torch.ones(4, 4)
print('First row: ', tensor[0])
print('first column: ', tensor[:, 0])
for i in range(tensor.shape[1]):
        tensor[:, i] = i

print('Last column: ', tensor[..., -1])

t1 = torch.cat([tensor, tensor, tensor], dim=0)
print(t1)