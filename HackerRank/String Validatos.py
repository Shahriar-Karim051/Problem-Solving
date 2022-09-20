# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:25:09 2020

@author: DELL
"""

if __name__ == '__main__':
    s = input()
    for i in [str.isalnum , str.isalpha , str.isdigit , str.islower , str.isupper]:
        print(any(i(c) for c in s))
    
    