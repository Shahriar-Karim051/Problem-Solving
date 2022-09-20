
import re

x = input()

y = input()


z = re.findall("1" , y)

if z:
    print("HARD")
else:
    print("EASY")