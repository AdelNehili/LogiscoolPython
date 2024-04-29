import numpy as np
import matplotlib.pyplot as plt
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


given_x = [x for x in range(-15,15)]
given_y = [x*x for x in range(-15,15)]

graph_drawer_obj = Graph_drawer(given_x,given_y)
graph_drawer_obj.plot_my_values()
