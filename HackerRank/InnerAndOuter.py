
import numpy as np

a = np.array([int(a) for a in input().split()])
b = np.array([int(b) for b in input().split()])

print(np.inner(a , b))
print(np.outer(a , b))