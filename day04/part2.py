'''
Created on Dec. 4, 2020

@author: Alex
'''
import re

def validate(passport):
    byr = int(passport['byr'])
    if byr < 1920 or byr > 2002:
        return False
    
    iyr = int(passport['iyr'])
    if iyr < 2010 or iyr > 2020:
        return False
    
    eyr = int(passport['eyr'])
    if eyr < 2020 or eyr > 2030:
        return False
    
    hgt_pattern = r'(\d+)(cm|in)\Z'
    hgt_match = re.match(hgt_pattern, passport['hgt'])
    if hgt_match is None:
        return False
    (hgt, unit) = hgt_match.groups()
    hgt = int(hgt)
    if unit == 'in' and (hgt < 59 or hgt > 76):
        return False
    if unit == 'cm' and (hgt < 150 or hgt > 193):
        return False
    
    hcl_pattern = r'#[0-9a-f]{6}\Z'
    if re.match(hcl_pattern, passport['hcl']) is None:
        return False
    
    ecl = passport['ecl']
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    
    pid_pattern = r'\d{9}\Z'
    if re.match(pid_pattern, passport['pid']) is None:
        return False
    
    return True
        

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
        passport_map = {}
        for element in ' '.join(passport.split('\n')).strip().split(' '):  
            (key, value) = element.split(':', 1)
            passport_map[key] = value
            
        if len(neccesary_keys.difference(passport_map.keys())) > 0:
            continue
        
        if validate(passport_map):
            valid_count += 1
            
    print valid_count
            
        
    
    