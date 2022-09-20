
import math

a = int(input())

print(math.factorial(a + a - 2) // (math.factorial(a - 1) * math.factorial(a - 1)))