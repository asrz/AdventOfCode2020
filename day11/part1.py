'''
Created on Dec. 11, 2020

@author: Alex
'''

def deep_copy(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element)
        new_matrix.append(new_row)
    return new_matrix

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
                
                if not north_wall:
                    neighbours.append(seats[row-1][col])
                if not south_wall:
                    neighbours.append(seats[row+1][col])
                if not west_wall:
                    neighbours.append(seats[row][col-1])
                if not east_wall:
                    neighbours.append(seats[row][col+1])
                if not north_wall and not west_wall:
                    neighbours.append(seats[row-1][col-1])
                if not north_wall and not east_wall:
                    neighbours.append(seats[row-1][col+1])
                if not south_wall and not west_wall:
                    neighbours.append(seats[row+1][col-1])
                if not south_wall and not east_wall:
                    try:
                        neighbours.append(seats[row+1][col+1])
                    except IndexError:
                        print row, col, north_wall, south_wall, west_wall, east_wall
                        raise
                
                if seat == 'L' and '#' not in neighbours:
                    next_seats[row][col] = '#'
                elif seat == '#' and neighbours.count('#') >= 4:
                    next_seats[row][col] = 'L'
        
        if next_seats == seats:
            break #no change    
        seats = next_seats
        
    count = 0
    for row in seats:
        count += row.count('#')
    print count
            