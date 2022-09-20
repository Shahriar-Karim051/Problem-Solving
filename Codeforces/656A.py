
i = int(input())
if i <= 12:
   print(pow(2 , i))
else:
   a = pow(2 , (i - 13)) * 100
   print(pow(2 , i) - a)