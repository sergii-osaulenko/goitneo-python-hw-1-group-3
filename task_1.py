from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Get today's date
    today = datetime.today().date()
    
    # Define weekdays starting from Monday
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Create a dictionary to store birthdays for each day of the week
    birthdays_per_week = defaultdict(list)
    
    # Iterate through users
    for user in users:
        name, birthday = user["name"], user["birthday"].date()
        
        # Determine the birthday for this year
        birthday_this_year = birthday.replace(year=today.year)

        # If birthday has passed this year, set it for next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year + 1)
        
        # Calculate the difference in days between birthday and today
        delta_days = (birthday_this_year - today).days
        
        # Determine the weekday of the birthday
        birthday_weekday = (today + timedelta(days=delta_days)).weekday()
        
        # If the birthday falls on a weekend, move it to Monday
        if birthday_weekday >= 5:
            delta_days += (7 - birthday_weekday)
        
        # If the birthday falls within the next week, store it
        if delta_days < 7:
            day_of_week = weekdays[(today + timedelta(days=delta_days)).weekday()]
            birthdays_per_week[day_of_week].append(name)
    
    # Display the result
    for day, users in birthdays_per_week.items():
        print(f"{day}: {', '.join(users)}")

# Example usage
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 3, 8)},
    {"name": "Jan Koum", "birthday": datetime(1976, 3, 9)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 3, 10)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 3, 11)}
]

get_birthdays_per_week(users)