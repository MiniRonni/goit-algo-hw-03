from datetime import datetime

def get_days_from_today(date):
    date = datetime.strptime(date, '%Y-%m-%d').date()
    return (date - datetime.today().date()).days

date = input("Enter date (yyyy-mm-dd):")
print(get_days_from_today(date))  