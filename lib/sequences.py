#!/usr/bin/env python3



def print_fibonacci(length):
    
    initial_list = [0, 1]

    if length == 0:
        print([])

    elif length == 1:
        print([0]) 

    else:
        while len(initial_list) < length:
            last_value = initial_list[-1]
            penultimate_value = initial_list[-2]
        
            added_value = last_value + penultimate_value
        
            initial_list.append(added_value)
        
        print(initial_list)

print_fibonacci(4)