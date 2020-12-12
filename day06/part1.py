'''
Created on Dec. 6, 2020

@author: Alex
'''

with open('day06.in', 'r') as input_file:
    forms = []
    form = set()
    for line in input_file:
        if len(line.strip()) == 0:
            forms.append(form)
            form = set()
            continue
        for letter in list(line.strip()):
            form.add(letter)
    forms.append(form)
    
    print sum([len(form) for form in forms])
        
        