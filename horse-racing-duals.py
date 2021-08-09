'''
Codingame Challenge: horse racing duals

Casablanca’s hippodrome is
organizing a new type of horse racing: duals.
During a dual, only two horses will participate in the race. 
In order for the race to be interesting, 
it is necessary to try to select two horses with similar 
strength.

Write a program which, using a given number of strengths, 
identifies the two closest strengths and shows their 
difference with an integer (≥ 0).
'''
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

horses = []
n = int(input())
for horse in range(n):
    pi = int(input())
    horses.append(pi)

horses.sort(reverse=True)

results = []
for index in range(len(horses) - 1):
    D = horses[index] - horses[index + 1]
    results.append(D)
result = min(results)
print(result)