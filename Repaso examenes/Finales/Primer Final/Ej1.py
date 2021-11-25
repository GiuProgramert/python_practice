def max_sequence(numbers):
    n = len(numbers)
    
    max_number = 0
    for i in range(n):
        acumulator = 0
        for j in range(i, n):
            acumulator = acumulator + numbers[j]
            
            if acumulator > max_number:
                max_number = acumulator
                
    return max_number