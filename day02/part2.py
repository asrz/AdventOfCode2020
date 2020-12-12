'''
Created on Dec. 4, 2020

@author: Alex
'''
import re

def xor(a, b):
    if a and not b:
        return True
    elif b and not a:
        return True
    else:
        return False


with open('day02.in', 'r') as input_file:
    count = 0
    
    for line in input_file:
        pattern = r'(\d+)-(\d+) (\w): (\w+)'
        match = re.match(pattern, line)
        
        index1 = int(match.group(1)) - 1
        index2 = int(match.group(2)) - 1
        letter = match.group(3)
        password = match.group(4)
        
        if xor(password[index1] == letter, password[index2] == letter):
            count += 1
        
            
    print count
        