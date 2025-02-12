import random

def get_number_ticket(min, max, quantity):
    """
    Generate a set of unique random numbers within the specified range.
    
    Args:
        min (int): The minimum value of the range (>=1).
        max (int): The maximum value of the range (<= 1000).
        quantity (int): The number of unique random numbers to generate.

    Returns:
        list: A list of unique random numbers.
              Return an empty list if parameters are invalid.
    """
    if not (1 <= min <= 1000 and 1 <= max <= 1000 and min <= max):
        return []
    
    if not (min <= quantity <= max):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    
    return sorted(numbers)

print(f"Лотерейні числа: {get_number_ticket(1, 46, 6)}")
