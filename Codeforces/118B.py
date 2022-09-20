
n = int(input())
ret = []
for i in range(n + 1):
    line = " " * 2 * (n - i)
    if i == 0:
        line += "0"
    elif i == 1:
        line += "0 1 0"
    else:
        line = list(ret[-1])
        line.pop(0)
        line.pop(0)
        line.insert(2 * i + 2 * (n - i), str(i - 1) + " ")
        line.insert(2 * i + 2 * (n - i), str(i) + " ")
        line = "".join(line)
    ret.append(line)
buf = list(ret)
buf.pop()
buf.reverse()
ret.extend(buf)
print("\n".join(ret))