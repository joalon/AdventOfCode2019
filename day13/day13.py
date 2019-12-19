#!/usr/bin/env python
# -*- coding: utf-8 -*-

l = []
with open("input2.txt", "r") as f:
    for line in f.readlines():
        l.append(line.strip())

print(l[2: len(l): 3].count('2'))
