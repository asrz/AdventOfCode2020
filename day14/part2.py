'''
Created on Dec. 14, 2020

@author: Alex
'''
import re
import itertools

def apply_mask(mask, address):
    b_address = bin(address)[2:]
    b_address = list('0' * (36 - len(b_address)) + b_address) #left pad with 0s
    
    mask = list(mask)
    
    for i in range(-1, -37, -1):
        if mask[i] == '1':
            b_address[i] = '1'
        elif mask[i] == 'X':
            b_address[i] = 'X'
    
    addresses = []
    for combo in list(itertools.product('01', repeat=b_address.count('X'))):
        new_address = ''.join(b_address)
        for bit in combo:
            new_address = new_address.replace('X', bit, 1)
        addresses.append(new_address)
        
    return [int(x, 2) for x in addresses]
    

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
            addresses = apply_mask(mask, address)
            for address in addresses:
                memory[address] = value
        else:
            print 'Error, unhandled case'
            exit()
     
    print sum(memory.values())
