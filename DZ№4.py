# №1
text = "Любите жизнь, покуда живы.\nМеж ней и смертью только миг." \
       "\nА там не будет ни крапивы,\nНи звезд, ни пепельниц, ни книг."
f = open("DZText.txt", "w")
f.write(text)
f.close()

f = open("DZText.txt", "r")
for x in f.readlines(1):
    f = open("DZText1.txt", "w")
    f.write(x)
f.close()

f = open("DZText1.txt", "r")
print(f.read())
f.close()

# №2
import json
jsonText = {
    "product": [
        {
            "name" : "Milk",
            "price" : 50
        },
        {
            "name" : "Bread",
            "price" : 40
        },
        {
            "name" : "Meat",
            "price" : 350
        }
    ],
    "product owner": [
        {
            "name" : "OOO_Сow",
            "city" : "Krasnodar"
        },
        {
            "name" : "OOO_Pole",
            "city" : "Voronezh"
        },
        {
            "name" : "Piggy",
            "city" : "Tambov"
        }
    ]
}
# print(jsonText)
write = json.dumps(jsonText, indent=4)
f = open("dz4.json", "w")
f.write(write)
f.close()

f = open("dz4.json", "r")
readjson = json.load(f)
f.close()

for x in readjson["product"]:
    print("Наименование продукта: " + x ["name"])
    print("Стоимость продукта: " + str(x["price"]))
    print("-" * 10)
for x in readjson["product owner"]:
    print("Наименование производителя: " + x ["name"])
    print("Город производителя: " + x ["city"])
    print("-" * 10)