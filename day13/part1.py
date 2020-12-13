'''
Created on Dec. 13, 2020

@author: Alex
'''
import sys

with open('day13.in', 'r') as input_file:
    timestamp = int(input_file.readline())
    busses = [int(x) for x in input_file.readline().split(',') if x != 'x']
    
    min_wait = sys.maxint
    best_bus = 0
    
    for bus in busses:
        missed_bus = timestamp % bus
        wait_time = bus - missed_bus
        if wait_time < min_wait:
            best_bus = bus
            min_wait = wait_time
            
    print best_bus * min_wait
        