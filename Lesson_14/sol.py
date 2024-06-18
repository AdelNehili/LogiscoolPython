from datetime import datetime

# Function to check if a year is a leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Function to calculate age in days more precisely
def calculate_age_in_days(birth_date, current_date):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    current_date = datetime.strptime(current_date, "%Y-%m-%d")
    age_in_days = (current_date - birth_date).days
    return age_in_days

# Get user input
input_date = input("Give me today's date with this format: e.g. 2021-02-24:\n")
date = input("Give me your birth date with the same format:\n")

# Calculate the precise age in days
days = calculate_age_in_days(date, input_date)
print("You are %s days old." % days)
