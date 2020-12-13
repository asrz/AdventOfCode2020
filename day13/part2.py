'''
Created on Dec. 13, 2020

@author: Alex
'''
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) / gcd(a, b)

with open('day13.in', 'r') as input_file:
    timestamp = int(input_file.readline())
    busses = input_file.readline().split(',')
     
    earliest_time = int(busses[0])
    time_multiple = int(busses[0])
     
    offset = 0
    for bus in busses[1:]:
        offset += 1
        if bus == 'x':
            continue
        bus = int(bus)
         
        time = earliest_time
        while True:
            if time % bus == (bus - offset) % bus:
                earliest_time = time
                time_multiple = lcm(time_multiple, bus)
                break
             
            time += time_multiple
     
    print earliest_time
