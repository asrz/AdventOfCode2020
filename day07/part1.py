'''
Created on Dec. 7, 2020

@author: Alex
'''
import json

bag_map = {}
shortcuts = {}

def can_hold(parent_bag, child_bag):
    global bag_map, shortcuts
    
    if parent_bag in shortcuts:
        return shortcuts[parent_bag]
    
    #print 'can', parent_bag, 'hold', child_bag
    if bag_map[parent_bag] is None:
        #print 'No'
        shortcuts[parent_bag] = False
        return False
    for child in bag_map[parent_bag]:
        if child == child_bag:
            #print 'Yes'
            shortcuts[parent_bag] = True
            return True
        else:
            if can_hold(child, child_bag):
                shortcuts[parent_bag] = True
                return True
    shortcuts[parent_bag] = False
    return False

with open('day07.in', 'r') as input_file:
    for line in input_file:
        (head, tail) = line.strip().replace('bags', '').replace('bag', '').replace('.', '').split('contain')
        children = tail.split(',')
        
        #print head, children
        child_map = {}
        
        if children == [' no other ']:
            child_map = None
        else:
            for child in children:
                (num, bag) = child.strip().split(' ', 1)
                child_map[bag] = int(num)
        bag_map[head.strip()] = child_map
        
    #print json.dumps(bag_map, indent=4)
    
    count = 0    


    print map(lambda parent: can_hold(parent, 'shiny gold'), bag_map.keys()).count(True)