import numpy as np
import numpy.random as npr

points = npr.randint(0, 2000, (25, 2), dtype=np.int)
print(points)
np.savetxt('points.csv', points, fmt="%i", delimiter=",", header="x,y", comments="")
