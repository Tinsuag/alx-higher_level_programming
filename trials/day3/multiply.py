mylist = [[1, 2, 3], [4, 5,6], [7, 8, 9]]
list = []
for num in mylist:
    list.append(([i**2 for i in num]))
print(list)