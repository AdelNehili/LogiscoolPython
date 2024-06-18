# Task 1 - Print in the same row
myList = []
for i in range(0,3,1):
    myList.append(i*i)
for j in range(0,len(myList),1):
    print(myList[j])
for element in myList:
    print(element)
for index,elem in enumerate(myList):
    print(f"index: {index}; elem : {elem}")