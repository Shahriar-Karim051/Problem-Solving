
n = input()

l = [int(l) for l in input().split()]

minimum = min(l)
maximum = max(l)
count = l.index(maximum)
l.pop(count)
#print(l)
l.insert(0, count)
#print(l)
l.reverse()
#print(l)
count += l.index(minimum)
print(count)