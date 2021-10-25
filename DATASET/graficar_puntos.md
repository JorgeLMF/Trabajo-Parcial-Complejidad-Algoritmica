import numpy as np
import numpy.random as npr
import random

len = 1000

a = npr.randint(0, len, (100, 2), dtype=np.int)
#print(a)
np.savetxt('almacenesXyY.csv', a, fmt="%i", delimiter=",", header="x,y", comments="")

b = npr.randint(0, len, (3500, 2), dtype=np.int)
#print(b)
np.savetxt('puntosentregaXyY.csv', b, fmt="%i", delimiter=",", header="x,y", comments="")

l1 = []
l2 = []
for i in range(len):
    l1.append(random.randint(15,25))
    l2.append(random.randint(8,15))
c = np.empty((len,0), int)
c = np.append(c, np.array([l1]).transpose(), axis=1)
c = np.append(c, np.array([l2]).transpose(), axis=1)
print(c)
np.savetxt('costoXhora_costoXkm_Xcamion.csv', c, fmt="%i", delimiter=",", header="costoXhora,costoXkm", comments="")