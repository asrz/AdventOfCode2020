'''
Created on Dec. 18, 2020

@author: Alex
'''

def calculate(line):
    parts = tokenize(line.strip())
    
    if len(parts) == 1:
        part = parts[0]
        if part.startswith('(') and part.endswith(')'):
            return calculate(part[1:-1])
        else:
            return int(part)
    
    result = calculate(parts.pop(0))
    
    while parts:
        operator = parts.pop(0)
        operand = calculate(parts.pop(0))
        
        if operator == '+':
            result = result + int(operand)
        elif operator == '*':
            result = result * int(operand)
        else:
            print 'Error, unknown operator:', operator
            exit()
    
    return result
    
    
    
def tokenize(line):
    parts = []
    
    part = ''
    depth = 0
    for c in list(line):
        part += c
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
             
        if depth == 0 and part.strip() != '':
            parts.append(part.strip())
            part = ''
            
    return parts    

with open('day18.in', 'r') as input_file:
    total = 0 
    
    for line in input_file:
        total += calculate(line)

    print total