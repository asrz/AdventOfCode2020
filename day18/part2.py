'''
Created on Dec. 18, 2020

@author: Alex
'''

def calculate(line):
    parts = tokenize(line)
    
    if len(parts) == 1:
        part = parts[0]
        if part.startswith('(') and part.endswith(')'):
            return calculate(part[1:-1])
        else:
            return int(part)
    
    while '+' in parts:
        i = parts.index('+') - 1
        
        term = calculate(parts.pop(i))
        parts.pop(i)
        operand = calculate(parts.pop(i))
        
        
        parts.insert(i, str(term + operand))
    
    while '*' in parts:
        i = parts.index('*') - 1
        
        term = calculate(parts.pop(i))
        parts.pop(i)
        operand = calculate(parts.pop(i))
        
        
        parts.insert(i, str(term * operand))
    
    return int(parts[0])
    
    
    
def tokenize(line):
    line += ' '
    parts = []
    
    part = ''
    depth = 0
    for c in list(line):
        part += c
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
             
        if depth == 0 and part.strip() != '' and c == ' ':
            parts.append(part.strip())
            part = ''
            
    return parts    

with open('day18.in', 'r') as input_file:
    total = 0 
    
    for line in input_file:
        total += calculate(line.strip())

    print total