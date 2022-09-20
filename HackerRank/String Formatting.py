# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:04:05 2020

@author: DELL
"""

def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1 , number + 1):
        o = oct(i)
        h = hex(i)
        b = bin(i)
        print(str(i).rjust(w , ' '),o[2:].rjust(w , ' '),h[2:].upper().rjust(w , ' '),b[2:].rjust(w , ' ')          )
    
    
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)