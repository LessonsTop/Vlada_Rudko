№1
list = [1, 2, 3, 4, 5, 6, 7, 8, "Anna", "Inna", "Ivan", "Petr", "Lisa", "Katrin", "Alex", "Mikl"]
listName = [str(element) for element in list if type(element) is str]
print(listName)
listNumber = [int(element) + 10 for element in list if type(element) is int]
print(listNumber)

№2
dict = {"Имя" : "Robot", "Количество жизней" : 3, "Количество маны" : 10, "Cила" : 100, "Ловкость" : 50, "Выносливость" : 60, "Физическая стойкость" : 80, "Магическая стойкость" : 70}
for key,value in dict.items():
    print(key, ':', value)

№3
while True:
    number1 = input('Введите первое число: ')
    number1_1 = int(number1)
    number2 = input('Введите второе число: ')
    number2_2 = int(number2)
    a = input("Выберите дейстивие: '+', '-', '*', '/'")
    if a == '+':
        result = number1_1 + number2_2
        print("Ответ: ", result)
    elif a == '-':
        result = number1_1 - number2_2
        print("Ответ: ", result)
    elif a == '*':
        result = number1_1 * number2_2
        print("Ответ: ", result)
    elif a == '/':
        result = number1_1 / number2_2
        print("Ответ: ", result)
    else:
        print("Неверно указано действие")











