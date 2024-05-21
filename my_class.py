import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
from sklearn.linear_model import LinearRegression

class Graph_drawer():
    def __init__(self,x,y):
        self.my_x = x
        self.my_y = y

    def show_values(self):
        print(f"Voila ce qu'on m'a donné {self.my_x}")
        print(f"Voila ce qu'on m'a donné {self.my_y}")

    def plot_my_values(self):
        plt.plot(self.my_x, self.my_y)
        plt.show()
    
    def show_some_csv_data(self,csv_path):
        data = pd.read_csv(csv_path)
        print(f"Here's all the data.columns : {data.columns}")
        print(data.head())
       

    def display_csv_data(self,csv_path,xLabel,yLabel,title=""):
        data = pd.read_csv(csv_path)

        data = data[[xLabel,yLabel,]]
        print(data.head())

        plt.plot(data[xLabel],data[yLabel],marker = "o")
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.grid(True)
        plt.show()
    
    def apply_linear_regression(self,csv_path):
        df = pd.read_csv(csv_path)
        df_expense = df[df["Type"]=="Expense"].copy() #Display in parallele df = df[df["Type"]=="Expense"]
        df_income = df[df["Type"]=="Income"].copy()
        
        model_exepense = LinearRegression()
        model_exepense.fit(df_expense[['Id']],df_expense[['Amount']])
        df_expense['PredictedExpense'] = model_exepense.predict(df_expense[['Id']])

        model_income = LinearRegression()
        model_income.fit(df_income[["Id"]],df_income[["Amount"]])
        df_income["PredictedIncome"] = model_income.predict(df_income[["Id"]])


        # Plotting both datasets and their regression lines
        plt.figure(figsize=(10, 6))
        plt.scatter(df_expense['Id'], df_expense['Amount'], color='blue', label='Actual Expense') #Usually scatter is used for clouds points (scatter points)
        plt.plot(df_expense['Id'], df_expense['PredictedExpense'], color='red', label='Predicted Expense', linewidth=2) #Usually, plot is used for linear/curves functions

        plt.scatter(df_income['Id'], df_income['Amount'], color='green', label='Actual Income')
        plt.plot(df_income['Id'], df_income['PredictedIncome'], color='orange', label='Predicted Income', linewidth=2)


        print(f"Care here's the new DataFrame df : {df.columns}")
        plt.title('Linear Regression Analysis for Income and Expenses')
        plt.xlabel('Id')
        plt.ylabel('Amount')
        plt.legend()
        plt.show()


given_x = []
given_y = []

for x in range(-15,16):
    given_x.append(x)
    given_y.append(x*x)


graph_drawer_obj = Graph_drawer(given_x,given_y)
# #graph_drawer_obj.show_some_csv_data("Student_Income_Expense_Data.csv") #Parfait pour check rapidement la data
#     # Index(['Id', 'Type', 'Amount', 'From', 'To', 'Date'], dtype='object')
graph_drawer_obj.display_csv_data('Student_Income_Expense_Data.csv',"Id","Amount")
# # graph_drawer_obj.apply_linear_regression("Student_Income_Expense_Data.csv")
