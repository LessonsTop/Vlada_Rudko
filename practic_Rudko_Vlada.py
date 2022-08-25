"""
Задание:
1. Вывести данные из файла json, а именно id, name, age, gender, balance, email, phone, isActive
2. Отсортировать полученные данные по полю isActive, записать полученный результат в файл result.txt
3. Осортировать по возрастанию balance только активных пользователей, записать полученный результат в файл result.txt
4. Опубликовать работу на гитхаб. Репозиторий: https://github.com/LessonsTop/practic-1 в ветки practic_FI (Где FI - фамилия и имя).
"""
# №1
import json

f = open("generated.json", "r")
jsonData = json.load(f)
f.close()
# print(jsonData)
userList = []

for x in jsonData:
    # print("User id: ", x["_id"])
    # print("User name: ", x["name"])
    # print("User age: ", x["age"])
    # print("User gender: ", x["gender"])
    # print("User balance: ", x["balance"])
    # print("User email: ", x["email"])
    # print("User phone: ", x["phone"])
    # print("User isActive: ", x["isActive"])
    # print("-" * 10)
    newGenerated = {
        "_id" : x["_id"],
        "name" : x["name"],
        "age" : x["age"],
        "gender" : x["gender"],
        "balance" : x["balance"],
        "email" : x["email"],
        "phone" : x["phone"],
        "isActive" : x["isActive"]
    }
    userList.append(newGenerated)
# print(userList)

# №2
f = open("result.txt", "w")
userList.sort(key=lambda row: row["isActive"])
active = str(userList)
f.write(active)
f.close()
# print(active)

# №3
f = open("result.txt", "w")
listActive = list(filter(lambda row: row["isActive"] == True, userList)
listActive.sort(key=lambda row: row["balance"], revers=True)
balance = str(listActive)
f.write(balance)
f.close()
print(balance)
for x in listActive:
    print(x)
