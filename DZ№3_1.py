list = [1, 2, 3, 4, 5, 6, 7, 8, "Anna", "Inna", "Ivan", "Petr", "Lisa", "Katrin", "Alex", "Mikl"]
listName = []
listNumber = []
for element in list:
    if type(element) == str:
        listName.append(element)
    if type(element) == int:
        x = element + 10
        listNumber.append(x)
print(listName)
print(listNumber)


