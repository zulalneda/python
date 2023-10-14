import torch
import numpy as np

# array = [[1,2,3],[4,5,6]]
# numpy_array = np.array(array)

# torch_tensor = torch.Tensor(array)
# torch_array = torch.from_numpy(numpy_array)

from PIL import Image
image = Image.open("C:\\Users\\huawei\\AppData\\Local\\Temp\\AweZip\\Temp1\\AweZip4\\data_f1\\images\\train\\bahri13221.jpg")
print(image)

print(image.size)

image=np.array(image)
image= torch.from_numpy(image)
print(image)

print(image.size())

array1 = torch.ones(3,3)
print(array1)
array2 = torch.Tensor([1,2,3],[1,2,3],[1,2,3])
print(array2)

