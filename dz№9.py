from peewee import *
"""импортировали всё для манипуляций с базой данных"""
def main():

    db = PostgresqlDatabase('dz9', user='postgres', password='vladushka99', host='127.0.0.1', port=5432)
    """создаем соединение с базой данных"""
    class BaseModel(Model):
        class Meta:
            database = db

    class City(BaseModel):
        city = CharField()
        street = CharField()
        house = CharField()

    class Country(BaseModel):
        country = CharField()
        city = ForeignKeyField(City, backref='Countrys')
        """связь с таблицей city, обратная ссылка"""

    db.connect()
    """подключились к базе данных"""
    db.create_tables([City,Country])
    """создали таблицы"""

    a = City.create(city = "Moscov", street = "Lenina", house = 50)
    b = City.create(city = "Paris", street = "Richelieu", house = 3)
    с = City.create(city = "London", street = "Oxford", house = 1)
    x = Country.create(country = "Russia", city = 1)
    y = Country.create(country = "France", city = 2)
    z = Country.create(country = "England", city = 3)
    """создали объекты в таблицах"""

    tab = Country.select().join(City)
   """объединили данные из двух таблиц"""
    for row in tab:
        print(row.country, row.city.city, row.city.street, row.city.house)
    """вывели данные на экран"""

if __name__ == '__main__':
    main()