'''
Created on Dec. 11, 2020

@author: Alex
'''
with open('day10.in', 'r') as input_file:
    joltages = [int(line) for line in input_file]
    
    joltages.sort()
    
    delta1s = 0
    delta3s = 0
    
    current_joltage = 0
    
    for joltage in joltages:
        delta = joltage - current_joltage 
        if delta > 3:
            print 'Error'
            exit()
        elif delta == 3:
            delta3s += 1
        elif delta == 1:
            delta1s += 1
        current_joltage = joltage
    
    delta3s += 1 #device
    
    print delta1s * delta3s