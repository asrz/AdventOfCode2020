'''
Created on Dec. 4, 2020

@author: Alex
'''
import re

with open('day02.in', 'r') as input_file:
    count = 0
    
    for line in input_file:
        pattern = r'(\d+)-(\d+) (\w): (\w+)'
        match = re.match(pattern, line)
        
        minimum = int(match.group(1))
        maximum = int(match.group(2))
        letter = match.group(3)
        password = match.group(4)
        
        #print minimum, maximum, letter, password
        
        occurances = list(password).count(letter)
        #print occurances
        if occurances >= minimum and occurances <= maximum:
            count += 1
            
    print count
        