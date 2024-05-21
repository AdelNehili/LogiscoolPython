import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from random import choice, randint

def generate_data(generated_data):
    types = ["Income", "Expense"]
    income_sources = ["Scholarship", "Part-time Job", "Parental Support"]
    expense_sources = ["Rent", "Books", "Groceries", "Utilities", "Transportation"]
    people = ["University", "Bookstore", "Supermarket", "Utility Company", "Bus Service"]

    dates = [datetime(2023, 9, 1) + timedelta(days=randint(0, 180)) for _ in range(generated_data)]

    data = {
        "Id": [],
        "Type": [],
        "Amount": [],
        "From": [],
        "To": [],
        "Date": [],
    }


    # Generate entries
    for i in range(generated_data):
        is_income = np.random.choice([True, False], p=[0.1, 0.9])  # Randomly decide if it's income or expense
        if is_income:
            _type = "Income"
            _source = choice(income_sources)
            _from = "N/A"
            _to = choice(people)
            mean, std_dev = 1000, 150  # Adjust mean and std_dev for income
        else:
            _type = "Expense"
            _source = choice(expense_sources)
            _from = choice(people)
            _to = "N/A"
            mean, std_dev = 50, 15  # Adjust mean and std_dev for expenses

        # Generating amount with Gaussian distribution
        amount = np.random.normal(mean, std_dev)
        # Ensure the amount is non-negative and rounded
        amount = max(1, int(round(amount)))

        data["Id"].append(i + 1)
        data["Type"].append(_type)
        data["Amount"].append(amount)
        data["From"].append(_from)
        data["To"].append(_to)
        data["Date"].append(dates[i].strftime("%Y-%m-%d"))

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    csv_file_path = "Student_Income_Expense_Data.csv"
    df.to_csv(csv_file_path, index=False)

# Example usage
generate_data(300)  # Generate data
