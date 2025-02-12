import re

def normalize_phone(phone_number):
    """
    Normalizes phone numbers to a standard format.
    
    Args:
        phone_number (str): The phone number in various format.

    Returns:
        str: The normalized phone number with only digits and '+'.
    """
    # Remove all non-digit characters except '+'
    phone_number = re.sub(r"[^\d+]", "", phone_number)

    # Ensure only one '+' at the beginning
    phone_number = re.sub(r"\++", "+", phone_number)
    
    # Normalize phone number format
    if phone_number.startswith("+380"):
        return phone_number
    elif phone_number.startswith("380"):
        return "+" + phone_number
    elif phone_number.startswith("+"):
        return phone_number
    else:
        return "+38" + phone_number


# Test case
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів:", sanitized_numbers)