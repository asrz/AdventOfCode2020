'''
Created on Dec. 4, 2020

@author: Alex
'''

def count_trees(right_slope, down_slope):
    right = 0
    down = 0
    trees = 0
    
    width = len(tree_map[0]) - 1
    height = len(tree_map)
    
    while down < height:
        letter = tree_map[down][right % width]
        
        #print down, letter
        
        if letter == '#':
            trees += 1
        right += right_slope
        down += down_slope
    return trees

with open('day03.in', 'r') as input_file:
    tree_map = [list(line) for line in input_file]
    
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    
    product = 1
    for slope in slopes:
        product *= count_trees(*slope)
    
    print product