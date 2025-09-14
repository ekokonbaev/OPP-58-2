
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Цвет: {self.color}")

    def sound(self):
        print("Животное издаёт звук")

class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def sound(self):
        print("Гав-гав!")

animal = Animal("Неизвестное", 5, "серый")
dog = Dog("Шарик", 3, "белый", "Овчарка")

animal.info()
animal.sound()

dog.info()
dog.sound()
print("Порода:", dog.breed)
