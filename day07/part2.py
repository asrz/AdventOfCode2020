'''
Created on Dec. 7, 2020

@author: Alex
'''
bag_map = {}
shortcuts = {}

def count_children(parent_bag):
    global bag_map, shortcuts
    
    if parent_bag in shortcuts:
        return shortcuts[parent_bag]
    
    if bag_map[parent_bag] is None:
        shortcuts[parent_bag] = 0
        return 0
    
    count = 0
    for child_bag in bag_map[parent_bag]:
        child_count = bag_map[parent_bag][child_bag]
        count += (child_count * (1 + count_children(child_bag)))
    shortcuts[parent_bag] = count
    return count
    

with open('day07.in', 'r') as input_file:
    for line in input_file:
        (head, tail) = line.strip().replace('bags', '').replace('bag', '').replace('.', '').split('contain')
        children = tail.split(',')
        
        child_map = {}
        
        if children == [' no other ']:
            child_map = None
        else:
            for child in children:
                (num, bag) = child.strip().split(' ', 1)
                child_map[bag] = int(num)
        bag_map[head.strip()] = child_map
        
    count = 0    

    print count_children('shiny gold')