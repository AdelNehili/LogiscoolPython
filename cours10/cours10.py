# Task 1 - Print in the same row
myList = []
for i in range(0,3,1):
    myList.append(f"{input(f'{i}/3 : Dis moi ce que tu veux que j ajoute : ')}")
for element in myList:
    print(type(element))
