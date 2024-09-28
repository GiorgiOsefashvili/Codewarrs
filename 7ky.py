def sum_two_smallest_numbers(numbers):
    sorted_numbers=sorted(numbers)
    
    return sorted_numbers[0] + sorted_numbers[1]


numbers=[12,3,5,2,1,77]
result = sum_two_smallest_numbers(numbers)
print(result)