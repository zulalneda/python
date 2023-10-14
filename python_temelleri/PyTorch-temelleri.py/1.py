import torch
import numpy as np

#Array işlemleri
array =[[1,2,3],[4,5,6]]
print(type(array))

numpy_array = np.array(array) #numpy arrayine çeviriyoruz.
print(numpy_array)
print(type(numpy_array))

torch_tensor = torch.Tensor(array) #pyTorch tensorüne çevirir.
print(torch_tensor)
print(type(torch_tensor))

torch_array = torch.from_numpy(numpy_array)
print(torch_array)
print(type(torch_array))
print("Boyutu: ", torch_array.size())
print(type(torch_array))

matris = np.ones((5,5)) #5x5 birim matris oluşturuyoruz
print(matris)

x = torch.ones(5,5)
print(x)

