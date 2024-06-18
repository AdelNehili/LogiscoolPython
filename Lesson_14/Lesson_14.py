import math

input_date = input("Give me today's date with this format: e.g. 2021-02-24:\n")
date = input("Give me your birth date with the same format:\n")
days = 0
daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Spliting the text to list element
born = date.split('-')
date_now = input_date.split('-')
print(born)
print(date_now)
# Converting the list element from string to int
for i in range(len(born)):
    born[i] = int(born[i])
for i in range(len(date_now)):
    date_now[i] = int(date_now[i])

#DIS NOUS QUEL AGE ON A EN TE BASANT SUR LES LISTES born ET date_now
gap_year = math.fabs(born[0]-date_now[0])*365
gap_month = math.fabs(born[1]-date_now[1])*31
gap_day = math.fabs(born[2]-date_now[2])
days = gap_day+gap_month+gap_year
print("You are %s days old." % days)


from datetime import datetime

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
