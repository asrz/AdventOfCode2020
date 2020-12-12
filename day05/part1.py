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
    max_seat_id = 0
    for line in input_file:
        (row, col) = get_coords(line)
        
        seat_id = row * 8 + col
        
        max_seat_id = max(max_seat_id, seat_id)
        #print row, col, seat_id
        #break
        
    print max_seat_id