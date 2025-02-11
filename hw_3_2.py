import random

def get_number_ticket(min, max, quantity):
    result_arr = set()

    while len(result_arr) != quantity:
        result_arr.add(random.randint(min, max))

    numbers = sorted(list(result_arr))
    
    return numbers

print(f"Лотерейні числа: {get_number_ticket(1, 49, 6)}")
