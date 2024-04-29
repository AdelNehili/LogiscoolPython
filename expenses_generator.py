import pandas as pd
from random import randint, choice
from datetime import datetime, timedelta

# Create a sample data for student income/outcome
data = {
    "Id": [],
    "Type": [],
    "Amount": [],
    "From": [],
    "To": [],
    "Date": []
}
def generate_data(generated_data):
    types = ["Income", "Expense"]
    income_sources = ["Scholarship", "Part-time Job", "Parental Support"]
    expense_sources = ["Rent", "Books", "Groceries", "Utilities", "Transportation"]
    people = ["University", "Bookstore", "Supermarket", "Utility Company", "Bus Service"]

    dates = [datetime(2023, 9, 1) + timedelta(days=randint(0, 180)) for _ in range(generated_data)]

    # Generate 20 entries
    for i in range(generated_data):
        is_income = randint(0, 1)  # Randomly decide if it's income or expense
        if is_income:
            _type = "Income"
            _source = choice(income_sources)
            _from = "N/A"
            _to = choice(people)
        else:
            _type = "Expense"
            _source = choice(expense_sources)
            _from = choice(people)
            _to = "N/A"
        
        data["Id"].append(i + 1)
        data["Type"].append(_type)
        data["Amount"].append(randint(100, 1000))
        data["From"].append(_from)
        data["To"].append(_to)
        data["Date"].append(dates[i].strftime("%Y-%m-%d"))

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    csv_file_path = "Student_Income_Expense_Data.csv"
    df.to_csv(csv_file_path, index=False)


generate_data(300)