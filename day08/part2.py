'''
Created on Dec. 8, 2020

@author: Alex
'''
import re

def operate(instructions, instruction_to_change):
    accumulator = 0
    index = 0
    indices = []
    instructions_passed = 0
    
    instruction_pattern = r'(acc|jmp|nop) ([+-]\d+)'
    
    while index not in indices and index < len(instructions):
        indices.append(index)
        
        instruction = instructions[index]
        match = re.match(instruction_pattern, instruction)
        operation, argument = match.groups()
        
        if operation == 'acc' or 'nop':
            instructions_passed += 1
            
            if instructions_passed == instruction_to_change:
                operation = 'acc' if operation == 'nop' else 'nop'
        
        
        if operation == 'acc':
            accumulator += int(argument)
            index += 1
        elif operation == 'nop':
            index += 1
        elif operation == 'jmp':
            index += int(argument)
        else:
            print 'Unknown operation'
    
    return index, accumulator

with open('day08.in', 'r') as input_file:
    instructions = input_file.readlines()
    
    for instruction_to_change in range(1, len(instructions)):
        index, accumulator = operate(instructions, instruction_to_change)
        if index == len(instructions):
            print accumulator
            break
