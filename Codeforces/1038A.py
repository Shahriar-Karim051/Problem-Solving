from collections import Counter
n , k = map(int , input().split())

x = input()
x = list(x)

if len(set(x)) < k:
    print(0)
else:
    a , b= Counter(x).most_common()[-1]
    print(b * k)