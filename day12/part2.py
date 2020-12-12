'''
Created on Dec. 12, 2020

@author: Alex
'''

def rotate(x, y, degrees):
    for _ in range((degrees % 360)/90):
        (x, y) = (y, -x)
    return (x, y)

with open('day12.in', 'r') as input_file:
    waypoint_x = 10
    waypoint_y = 1
     
    ship_x = 0
    ship_y = 0
     
    for line in input_file:
        direction = line[0]
        number = int(line[1:])
         
        if direction == 'N':
            waypoint_y += number
        elif direction == 'S':
            waypoint_y -= number
        elif direction == 'W':
            waypoint_x -= number
        elif direction == 'E':
            waypoint_x += number
        elif direction == 'L':
            waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, -number)
        elif direction == 'R':
            waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, number)
        elif direction == 'F':
            ship_x += waypoint_x * number
            ship_y += waypoint_y * number 
         
         
    print abs(ship_x) + abs(ship_y)

    