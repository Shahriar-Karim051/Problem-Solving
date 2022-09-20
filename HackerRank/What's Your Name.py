# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:33:04 2020

@author: DELL
"""

def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)