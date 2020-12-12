'''
Created on Dec. 4, 2020

@author: Alex
'''

with open('day04.in') as input_file:
    passports = []
    passport = '' 
    
    i = 0
    for line in input_file:
        if len(line.strip()) == 0:
            passports.append(passport)
            passport = ''
        else:
            passport += line
    passports.append(passport)
    
    valid_count = 0        
    
    neccesary_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    for passport in passports:
        present_keys = []
        for element in ' '.join(passport.split('\n')).strip().split(' '):  
            (key, value) = element.split(':', 1)
            present_keys.append(key)
            
        
        missing_keys = neccesary_keys.difference(present_keys)
        
        if len(missing_keys) == 0:
            valid_count += 1
        else:
            #print missing_keys
            pass
            
    print valid_count
            
        
    
    