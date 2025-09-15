class LibraryBook:
    def __init__(self, title, secret_code):
        self.title = title
        self._is_taken = False
        self.__secret_code = secret_code

    def take_book(self, code):
        if code == self.__secret_code and not self._is_taken:
            self._is_taken = True
            print(f"Книга '{self.title}' успешно взята!")
        elif self._is_taken:
            print(f"Книга '{self.title}' уже занята!")
        else:
            print("Неверный секретный код!")

    def return_book(self):
        if self._is_taken:
            self._is_taken = False
            print(f"Книга '{self.title}' возвращена в библиотеку.")
        else:
            print(f"Книга '{self.title}' и так свободна.")


from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата {amount} сом через банковскую карту прошла успешно.")

    def refund(self, amount):
        print(f"Возврат {amount} сом на банковскую карту выполнен.")


class CryptoPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата {amount} USDT через криптовалюту прошла успешно.")

    def refund(self, amount):
        print(f"Возврат {amount} USDT в криптовалюте выполнен.")
