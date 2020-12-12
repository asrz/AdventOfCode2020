'''
Created on Dec. 9, 2020

@author: Alex
'''
import itertools


with open('day09.in', 'r') as input_file:
    numbers = [int(x) for x in input_file.readlines()]
    
    preamble = numbers[:25]
    
    for goal in numbers[25:]:
        match = False
        for pair in itertools.combinations(preamble, 2):
            if sum(pair) == goal:
                match = True
                break
        if not match:
            print goal
            break
        preamble.pop(0)
        preamble.append(goal)
                
    
    