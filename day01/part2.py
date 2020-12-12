with open('day1.in', 'r') as input_file:
    expenses = [int(line) for line in input_file]
    
    expenses.sort()
    
    root_index = 0
    head_index = 1
    tail_index = len(expenses) - 1
    
    while True:
        root = expenses[root_index]
        head = expenses[head_index]
        tail = expenses[tail_index]
        
        goal = 2020 - root
        
        total = head + tail
        if total == goal:
            print head * tail * root
            exit()
        elif total < goal:
            head_index += 1
        elif total > goal:
            tail_index -= 1
            
        if tail_index <= head_index:
            root_index += 1
            head_index = root_index + 1
            tail_index = len(expenses) - 1
            