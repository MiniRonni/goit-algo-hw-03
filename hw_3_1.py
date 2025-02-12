from datetime import datetime

def get_days_from_today(date):
    """
    Calculates the number of days between a given date and the current date.
    
    Args:
        date_str (str): A date string in the format 'YYYY-MM-DD'.
        
    Returns:
        int: The number of days between the given day and today.
        
    Raises:
        ValueError: If the date format is incorrect.
    """
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        return (date - today).days
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")


if __name__:
    date = input("Enter your date (yyyy-mm-dd): ").strip()
    try:
        print(get_days_from_today(date))  
    except ValueError as e:
        print(e)