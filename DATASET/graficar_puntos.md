import numpy as np
import numpy.random as npr
import random

a = npr.randint(0, 300, (90, 2), dtype=np.int)
#print(a)
np.savetxt('almacenesXyY.csv', a, fmt="%i", delimiter=",", header="x,y", comments="")

b = npr.randint(0, 300, (2650, 2), dtype=np.int)
#print(b)
np.savetxt('puntosentregaXyY.csv', b, fmt="%i", delimiter=",", header="x,y", comments="")

l1 = []
l2 = []
for i in range(300):
    l1.append(random.randint(15,25))
    l2.append(random.randint(8,15))
c = np.empty((300,0), int)
c = np.append(c, np.array([l1]).transpose(), axis=1)
c = np.append(c, np.array([l2]).transpose(), axis=1)
print(c)
np.savetxt('costoXhora_costoXkm_Xcamion.csv', c, fmt="%i", delimiter=",", header="costoXhora,costoXkm", comments="")