

l = []

for _ in range(int(input())):
    s = input().split()
    cmd = s[0]
    arg = s[1:]
    if cmd != 'print':
        cmd += "(" + ",".join(arg) + ")"
        #print(cmd)
        eval("l." + cmd)
    else:
        print(l)