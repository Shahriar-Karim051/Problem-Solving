# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 01:18:04 2020

@author: DELL
"""

regex_pattern = r"[,.]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))