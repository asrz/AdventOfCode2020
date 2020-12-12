'''
Created on Dec. 9, 2020

@author: Alex
'''
import itertools


with open('day09.in', 'r') as input_file:
    numbers = [int(x) for x in input_file.readlines()]
    
    preamble = numbers[:25]
    
    invalid = 0
    for goal in numbers[25:]:
        match = False
        for pair in itertools.combinations(preamble, 2):
            if sum(pair) == goal:
                match = True
                break
        if not match:
            invalid = goal
            break
        preamble.pop(0)
        preamble.append(goal)
                
    start_index = 0
    end_index = 0
    
    total = numbers[0]
    while total != invalid:
        if total < invalid:
            end_index += 1
        if total > invalid:
            start_index += 1
        total = sum(numbers[start_index:end_index])
    goal_slice = numbers[start_index:end_index]
    
    print min(goal_slice) + max(goal_slice)
    