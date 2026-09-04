import numpy as np
from scipy import sparse
X = sparse.random(18750, 13826, density=0.01)
W = np.random.random((13826, 1))
y = np.random.random((18750, 1))
import time
t = time.time()
for i in range(500):
    Z = X @ W
    P = 1 / (1 + np.exp(-Z))
    dW = X.T @ (P - y)
print(time.time() - t)
