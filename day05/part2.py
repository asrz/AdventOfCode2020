'''
Created on Dec. 5, 2020

@author: Alex
'''

def get_coords(seat):
    row = seat[:7]
    row = row.replace('F', '0').replace('B', '1')
    row = int(row, 2)
    col = seat[7:].replace('L', '0').replace('R', '1')
    col = int(col, 2)
    return row, col

with open('day05.in', 'r') as input_file:
    seat_ids = []
    for line in input_file:
        (row, col) = get_coords(line)
        
        seat_id = row * 8 + col
        
        seat_ids.append(seat_id)
        #print row, col, seat_id
        #break
        
    
    seat_ids.sort(reverse=True)
    index = 1
    for index in range(0, len(seat_ids)-1):
        a = seat_ids[index]
        b = seat_ids[index+1]
        if a - 1 != b:
            print a-1
            break
    
    