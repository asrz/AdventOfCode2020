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
valid_numbers_per_field = {}

rule_pattern = r'([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)'
for rule in rules:
    match = re.match(rule_pattern, rule)
    if match is None:
        print "Error, rule didn't match"
        exit()
    field = match.groups()[0]
    min1, max1, min2, max2 = [int(x) for x in match.groups()[1:]]
    
    valid_numbers_per_field[field] = set()
    
    for i in range(min1, max1+1):
        valid_numbers.add(i)
        valid_numbers_per_field[field].add(i)
    for i in range(min2, max2+1):
        valid_numbers.add(i)
        valid_numbers_per_field[field].add(i)
        
        
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
        

all_possible_fields = [valid_numbers_per_field.keys() for rule in rules]

for ticket in valid_tickets:
    ticket_fields = [int(x) for x in ticket.split(',')]
    for i, ticket_field in enumerate(ticket_fields):
        for field in valid_numbers_per_field:
            if ticket_field not in valid_numbers_per_field[field]:
                all_possible_fields[i].remove(field)


field_map = {}
while len(field_map) < len(rules):
    for i, possible_field_list in enumerate(all_possible_fields):
        if len(possible_field_list) == 1:
            field = possible_field_list[0]
            field_map[i] = field
            for other_field in all_possible_fields:
                if field in other_field:
                    other_field.remove(field)
            break

ticket_values = [int(x) for x in your_ticket.split(',')]

departure_product = 1

for field_index in field_map:
    field = field_map[field_index]
    if field.startswith('departure'):
        departure_product *= ticket_values[field_index]
        
print departure_product