'''
Created on Dec. 12, 2020

@author: Alex
'''

with open('day12.in', 'r') as input_file:
    x = 0
    y = 0
    
    direction_order = ['N', 'E', 'S', 'W']
    direction_index = 1
    
    for line in input_file:
        direction = line[0]
        number = int(line[1:])
        
        if direction == 'F':
            direction = direction_order[direction_index]
            
        if direction == 'N':
            y += number
        elif direction == 'S':
            y -= number
        elif direction == 'W':
            x -= number
        elif direction == 'E':
            x += number
        elif direction == 'R':
            direction_index = (direction_index + number/90) % len(direction_order)
        elif direction == 'L':
            direction_index = (direction_index - number/90) % len(direction_order)  
        
    print abs(x) + abs(y)
    