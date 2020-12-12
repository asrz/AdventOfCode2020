'''
Created on Dec. 11, 2020

@author: Alex
'''
shortcuts = {}

def count_paths(current_index, joltages):
    current_joltage = joltages[current_index]
    
    if current_index in shortcuts:
        return shortcuts[current_index]
    
    count = 0
    index = current_index + 1
    
    while index < len(joltages):
        joltage = joltages[index]
        #print joltage
        if joltage > current_joltage + 3:
            break 
        count += count_paths(index, joltages)
        index += 1
    shortcuts[current_index] = count
    return count
    
    

with open('day10.in', 'r') as input_file:
    joltages = [int(line) for line in input_file]
    
    joltages.append(0)
    
    joltages.sort()
    
    #joltages = [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
    
    shortcuts[len(joltages)-1] = 1
    print count_paths(0, joltages)
    
    

        