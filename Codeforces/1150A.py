

n , m , r = map(int , input().split())

b = [int(b) for b in input().split()]
s = [int(s) for s in input().split()]

buy = (r // min(b)) * min(b)
sell = (r // min(b)) * max(s)
profit = (r - buy) + sell

print(profit if profit > r else r) 