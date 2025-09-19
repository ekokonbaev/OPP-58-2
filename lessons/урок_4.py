"""Множество наследование"""
#Родительский класс
class A:
    def action(self):
        print("A")
#Наследование
class B(A):
    def action(self):
        print("B")
#Наследование
class C(B):
    def action(self):
        print("C")
#Наследование
class D(C):
    def action(self):
        super().action()        #Обращение к С
        print("D")

obj = D()                          #Обращение классу
obj.action()                        #Вывод
print(D.mro())                      #Узнать путь к обращение класс