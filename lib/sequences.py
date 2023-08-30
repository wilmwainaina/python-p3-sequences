#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []

    if length >= 1:
        fibonacci_sequence.append(0)
    
    if length >= 2:
        fibonacci_sequence.append(1)
    
    while len(fibonacci_sequence) < length:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    
    print(fibonacci_sequence)

# length = 0
print_fibonacci(0)  # Output: []

#  length = 9
print_fibonacci(9)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]
pass