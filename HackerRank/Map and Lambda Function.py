# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 00:45:05 2020

@author: DELL
"""

cube = lambda x: pow(x , 3)# complete the lambda function 

def fibonacci(n):
    fib = [0 , 1]
    for i in range(2 , n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[0:n]
    # return a list of fibonacci numbers


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
'''
inp = int(input())

cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

print(list(map(cube, list(fibonacci(inp)))))
'''