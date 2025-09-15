"""Инкапсуляция
Когда имя атрибута или метода начинается с одного подчеркивания (например: _balance
это означает что он защищен(protected)
или может начинаться с двух подчеркиваний __password что это обозначает что он private"""

# class BankAccount:
#     def __init__(self , login , balance , password):
#         self.login = login          #public - публичный атрибут
#         self._balance = balance     #protected - защищен атрибут
#         self.__password = password  #private - приват атрибут


#     def check_password(self , password):          #это метод вне класс это функция
#         if password == self.__password :
#             print("Successfully")
#         else:
#             print("Error")
#
#     def reset_def_password(self):
#         self.__password = 22082006
#
#     def reset_password(self, password):
#         if password == self.__password :
#             self.reset_def_password()
#
# user = BankAccount("admin" , "123456" , "password")
# user.reset_password("22082006")


"""Абстракция позволяет сосредоточиться на общих характеристиках, скрывая детали
реализации. Это может сделать , создавая абстрактные классы, которые определяют интерфейс
 (методы) для классов-наследников. В Python абстрактные классы обычно создаются с помощью
  модуля abc."""

from abc import ABC , abstractmethod

#Абстрактный класс
class SendSmsOtp(ABC):
    @abstractmethod
    def send_otp(self):
        mg = f"<text>115114</text>"
        pass

class SmsSender(SendSmsOtp):            #Наследование (дочерний класс)
    def send_otp(self):
        mg = {
            "text": "text"
        }