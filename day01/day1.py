with open('day1.in') as input_file:
    expenses = [int(line) for line in input_file]
    
    expenses.sort()
    
    #print expenses[:5]
    
    head_index = 0
    tail_index = len(expenses)-1
    
    while True:
        head = expenses[head_index]
        tail = expenses[tail_index]
        total = head + tail
        if total == 2020:
            print head * tail
            exit()
        elif total < 2020:
            head_index += 1
        elif total > 2020:
            tail_index -= 1
        else:
            print 'wtf', total
            