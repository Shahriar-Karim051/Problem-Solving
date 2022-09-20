



from collections import defaultdict

for i in range(int(input())):

    x = input()

    cnt = len(set([i for i in x]))

    current = defaultdict(lambda: 0)
    c = 0
    mn = len(x)
    s = 0
    for j in range(len(x)):
        current[x[j]] += 1
        if current[x[j]] == 1:
            c += 1
        
        if c == cnt:
            while current[x[s]] > 1:
                if current[x[s]] > 1:
                    current[x[s]] -= 1
                s += 1
            
            w = j - s + 1
            if mn > w:
                mn = w
    if mn < 3:
        print(0)
    else:
        print(mn)
            
            
