from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Prepare data structure to store birthdays by weekday
    birthdays_per_week = defaultdict(list)
    
    # Get current date
    today = datetime.today().date()
    
    # Iterate through users
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        # Convert birthday to this year
        birthday_this_year = birthday.replace(year=today.year)
        
        # Check if this year's birthday has passed
        if birthday_this_year < today:
            # Consider the date for the following year
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Calculate difference in days between birthday and today
        delta_days = (birthday_this_year - today).days
        
        # Determine the weekday of the birthday
        birthday_weekday = (today + timedelta(days=delta_days)).strftime('%A')
        
        # Ensure the birthday is within the next week
        if delta_days < 7:
            # If birthday falls on weekend, move it to Monday
            if birthday_weekday in ['Saturday', 'Sunday']:
                birthday_weekday = 'Monday'
            
            # Store the username on the corresponding day of the week
            birthdays_per_week[birthday_weekday].append(name)
    
    # Display the collected names by day of the week
    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

# Example usage:
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 2, 14)},
]

get_birthdays_per_week(users)