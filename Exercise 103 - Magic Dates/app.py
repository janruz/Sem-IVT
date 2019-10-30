from datetime import datetime
from datetime import timedelta  


def is_date_magic(date: datetime):
    return date.month * date.day == (date.year % 100)


print("All magic dates in any century:")
initial_date = datetime(1900, 1, 1)
number_of_days = (datetime(1999, 12, 31) - initial_date).days


for day_number in range(number_of_days):
    current_date = initial_date + timedelta(days=day_number)
    if is_date_magic(current_date):
        print(current_date.strftime("%x"))