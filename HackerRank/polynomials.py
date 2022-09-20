
import numpy as np

a = np.array([float(a) for a in input().split()])

n = int(input())

print(np.polyval(a , n))