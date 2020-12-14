'''
Created on Dec. 14, 2020

@author: Alex
'''
import re

def apply_mask(mask, value):
    and_mask = int(mask.replace('X', '1'), 2)
    or_mask = int(mask.replace('X', '0'), 2)
    
    return (value & and_mask) | or_mask

with open('day14.in') as input_file:
    memory = {}
    mask = 'X'*36
     
    mask_pattern = r'^mask = ([X10]{36})$'
    mem_pattern = r'^mem\[(\d+)\] = (\d+)$'
     
    for line in input_file:
        mask_match = re.match(mask_pattern, line)
        mem_match = re.match(mem_pattern, line)
         
        if mask_match is not None and mem_match is not None:
            print 'Error, both patterns match'
            exit()
        elif mask_match is None and mem_match is None:
            print 'Error, neither pattern matches'
            exit()
        elif mask_match is not None:
            mask = mask_match.group(1)
        elif mem_match is not None:
            address, value = [int(x) for x in mem_match.groups()]
            memory[address] = apply_mask(mask, value)
        else:
            print 'Error, unhandled case'
            exit()
    
    print sum(memory.values())
