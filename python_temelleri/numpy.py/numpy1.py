import matplotlib.pyplot as matplot
import numpy as np

maasListesi = np.random.normal(400,500,1000)
print(np.mean(maasListesi))

matplot.hist(maasListesi,50)
print(matplot.show())