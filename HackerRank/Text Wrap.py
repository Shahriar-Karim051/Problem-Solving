# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:07:07 2020

@author: DELL
"""

import textwrap

def wrap(string, max_width):
    a = textwrap.wrap(string , max_width)
    return "\n".join(a)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)