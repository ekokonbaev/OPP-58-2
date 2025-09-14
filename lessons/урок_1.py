#Создаем класс
class Cars:
    #Конструктор класса
    def __init__(self, name , model , country , year):
        #Атрибута класса
        self.name = name
        self.model = model
        self.country = country
        self.year = year

#Метод класса | Вне метод это функция
    def motors(self):
        print("Обьем мотор")


#Обьект | Экземпляр
Car1 = Cars("Bmw" , "m5" , "Germany" , 2019)
Car = Cars("Toyota" , "Supra" , "Japan" , 2001)
print(f"Имя: {Car.name} , Модель: {Car.model} , Страна: {Car.country} , Год выпуска: {Car.year}")
print(f"Имя: {Car1.name} , Модель: {Car1.model} , Страна: {Car1.country} , Год выпуска: {Car1.year}")