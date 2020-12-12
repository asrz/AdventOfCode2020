'''
Created on Dec. 11, 2020

@author: Alex
'''
from __builtin__ import False

def deep_copy(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element)
        new_matrix.append(new_row)
    return new_matrix

def valid_coords(row, col, width, height):
    if row < 0 or row >= height:
        return False
    if col < 0 or col >= width:
        return False
    return True

def apply_vector(row, col, vector, multiplier):
    new_row = row + vector[0] * multiplier
    new_col = col + vector[1] * multiplier
    return (new_row, new_col)


with open('day11.in', 'r') as input_file:
    seats = [list(line.strip()) for line in input_file]
    
    height = len(seats)
    width = len(seats[0])
    
    i = 0
    while True:
        next_seats = deep_copy(seats)
        i += 1
        print 'Iteration', i
        for row in range(height):
            for col in range(width):
                seat = seats[row][col]
                
                if seat == '.':
                    continue
                
                north_wall = row == 0
                south_wall = row == height-1
                west_wall = col == 0
                east_wall = col == width-1
                
                occupied_neighbours = 0
                
                neighbours = []
                
                debug = False and i == 3 and row == 0 and col == 2
                
                for vector in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    j = 0
                    while True:
                        j += 1
                        new_row, new_col = apply_vector(row, col, vector, j)
                        if debug:
                            print row, col, '+', vector, '*', j, '=', new_row, new_col
                        if not valid_coords(new_row, new_col, width, height):
                            if debug:
                                print new_row, new_col, 'Invalid'
                            #reach wall
                            break
                        neighbour = seats[new_row][new_col]
                        if debug:
                            print 'neighbour', neighbour
                        if neighbour != '.':
                            #reach seat
                            neighbours.append(neighbour)
                            break
                
                if debug:
                    print 'neighbours', neighbours
                if seat == 'L' and '#' not in neighbours:
                    next_seats[row][col] = '#'
                elif seat == '#' and neighbours.count('#') >= 5:
                    next_seats[row][col] = 'L'
        
        if next_seats == seats:
            break #no change    
        seats = next_seats
        
    count = 0
    for row in seats:
        count += row.count('#')
    print count
            