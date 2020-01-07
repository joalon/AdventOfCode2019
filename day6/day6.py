#!/usr/bin/env python
# -*- coding: utf-8 -*-

inp = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
inp = inp.strip().split('\n')

inp = []
with open('input.txt', 'r') as f:
  for line in f.readlines():
    inp.append(line.strip())

orbitDict = {}

for line in inp:
  orbiter, orbits = line.split(')')

  if orbits not in orbitDict.keys():
    orbitDict[orbits] = []

  if orbiter not in orbitDict:
    orbitDict[orbiter] = [orbits]
  else:
    updatedOrbits = orbitDict.get(orbiter)
    updatedOrbits.append(orbits)
    orbitDict[orbiter] = updatedOrbits
    
def stepThroughOrbits(orbits: dict, currentPlanet: str, stepsFromRoot: int) -> int:
  if not orbits[currentPlanet]:
    return stepsFromRoot

  acc = stepsFromRoot
  for nextPlanet in orbits[currentPlanet]:
    acc += stepThroughOrbits(orbits, nextPlanet, stepsFromRoot + 1)

  return acc

def findRoot(orbitDict: dict) -> str:
  nrRoots = 0
  for v in orbitDict.keys():
    if v not in [item for sublist in orbitDict.values() for item in sublist]:
        return v


print("Part 1 answer is: " + str(stepThroughOrbits(orbits=orbitDict, currentPlanet='COM', stepsFromRoot=0)))
