'''
Created on Dec. 8, 2020

@author: Alex
'''
import re

with open('day08.in', 'r') as input_file:
    instructions = input_file.readlines()
    
    index = 0
    indices = []
    accumulator = 0
    
    instruction_pattern = r'(acc|jmp|nop) ([+-]\d+)'
    
    while index not in indices:
        indices.append(index)
        
        instruction = instructions[index]
        match = re.match(instruction_pattern, instruction)
        operation, argument = match.groups()
        
        if operation == 'acc':
            accumulator += int(argument)
            index += 1
        elif operation == 'nop':
            index += 1
        elif operation == 'jmp':
            index += int(argument)
        else:
            print 'Unknown operation'
    
    print accumulator