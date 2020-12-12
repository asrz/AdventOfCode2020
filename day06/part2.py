'''
Created on Dec. 6, 2020

@author: Alex
'''

with open('day06.in', 'r') as input_file:
    blocks = []
    block = []
    for line in input_file:
        form = set()
        if len(line.strip()) == 0:
            blocks.append(block)
            block = []
            continue
        for letter in list(line.strip()):
            form.add(letter)
        block.append(form)
    blocks.append(block)
    
    count = 0
    for block in blocks:
        intersect = None
        for form in block:
            if intersect is None:
                intersect = form
            else:
                intersect = intersect.intersection(form)
        count += len(intersect)
        
    print count
        