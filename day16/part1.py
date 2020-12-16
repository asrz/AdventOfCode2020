'''
Created on Dec. 16, 2020

@author: Alex
'''
import re

rules = []

your_ticket = ''
nearby_tickets = []


with open('day16.in', 'r') as input_file:
    line = input_file.readline().strip()
    while line != '':
        rules.append(line)
        line = input_file.readline().strip()
        
    line = input_file.readline().strip()
    if line != 'your ticket:':
        print 'Error, expected your ticket'
        exit()
    your_ticket = input_file.readline().strip()
    
    line = input_file.readline().strip()
    if line != '':
        print 'Error, expected blank line'
        exit()
    
    line = input_file.readline().strip()
    if line != 'nearby tickets:':
        print 'Error, expected nearby tickets'
        exit()
    line = input_file.readline().strip()
    while line != '':
        nearby_tickets.append(line)
        line = input_file.readline().strip()
        
valid_numbers = set()
rule_pattern = r'[\w\s]+: (\d+)-(\d+) or (\d+)-(\d+)'
for rule in rules:
    match = re.match(rule_pattern, rule)
    if match is None:
        print "Error, rule didn't match"
        exit()
    min1, max1, min2, max2 = [int(x) for x in match.groups()]
    
    for i in range(min1, max1+1):
        valid_numbers.add(i)
    for i in range(min2, max2+1):
        valid_numbers.add(i)
        
        
invalid_tickets = []
valid_tickets = []

ticket_scanning_error_rate = 0

for ticket in nearby_tickets:
    valid = True
    for field in [int(x) for x in ticket.split(',')]:
        if field not in valid_numbers:
            ticket_scanning_error_rate += field
            valid = False
    if valid:
        valid_tickets.append(ticket)
    else: 
        invalid_tickets.append(ticket)
        
print 'Ticket scanning error rate:', ticket_scanning_error_rate
    