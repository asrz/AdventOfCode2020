'''
Created on Dec. 4, 2020

@author: Alex
'''

with open('day03.in', 'r') as input_file:
    tree_map = [list(line) for line in input_file]
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
        right += 3
        down += 1
    print trees