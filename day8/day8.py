#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys


class Img:

    def __init__(self, intlist, width, height):
        self.layers = []
        self.width = width
        self.height = height

        for gi in range(0, len(intlist), width*height):
            currentslice = intlist[gi:gi+width*height] 

            newlayer = []
            sliceindex = 0
            for i in range(height):
                slic = []
                for j in range(width):
                    slic.append(currentslice[sliceindex])
                    sliceindex += 1
                newlayer.append(slic)

            self.layers.append(newlayer)

    def __repr__(self):
        
        rep = "Img: \n"
        for layer in self.layers:
            rep += str(layer) + '\n'

        return rep

    def getlayercontaininglowestnrzeroes(self):
        resultlayer = None
        lowestnumberofzeroes = sys.maxsize
        for index, layer in enumerate(self.layers):
            currentlayerzeroes = 0
            for h in range(self.height):
                for w in range(self.width):
                    if layer[h][w] == 0:
                        currentlayerzeroes += 1
            if currentlayerzeroes < lowestnumberofzeroes:
                lowestnumberofzeroes = currentlayerzeroes
                resultlayer = index

        return resultlayer, lowestnumberofzeroes

    def verifylayer(self, layerindex):
        ones = 0
        twoes = 0
        for h in range(self.height):
            for w in range(self.width):
                if self.layers[layerindex][h][w] == 1:
                    ones += 1
                elif self.layers[layerindex][h][w] == 2:
                    twoes += 1

        return ones * twoes


inp = []
with open('day8/input.txt','r') as f:
    for line in f.readlines():
        for c in line.strip():
            inp.append(int(c))


realimg = Img(inp, width=25, height=6)
layer, number = realimg.getlayercontaininglowestnrzeroes() 
print("Part 1 solution is: " + str(realimg.verifylayer(layer)))

