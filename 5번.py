import numpy as np
a = np.array([[2, -1, 1],[1, 3, -1],[1, 0, 2]])
b = np.array([-2, 10, -8])
c = np.linalg.inv(a)
d = np.dot(c, b)
print(d)
