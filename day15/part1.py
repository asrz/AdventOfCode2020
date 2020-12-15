'''
Created on Dec. 15, 2020

@author: Alex
'''
import time


start = time.time()

with open('day15.in', 'r') as input_file:
    starting_numbers = [int(x) for x in input_file.readline().split(',')]
    
    turn = 0
    
    last_spoken = {}
    current_number = None
    
    for number in starting_numbers:
        if current_number is not None:
            last_spoken[current_number] = turn
        turn += 1
        current_number = number
        #print current_number

    
    next_number = None
        
    while turn < 30000000:
        if current_number in last_spoken:
            next_number = turn - last_spoken[current_number]
        else:
            next_number = 0
        
        last_spoken[current_number] = turn
        turn += 1
        current_number = next_number
        #print current_number
        
    print current_number
    
print time.time() - start, 's'