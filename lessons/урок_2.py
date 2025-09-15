class BaseUser:
    def __init__(self):
        pass  # пока ничего нет

    def info(self):
        print("Это обычный пользователь")


class VipUser(BaseUser):
    def __init__(self, name, username, status):
        super().__init__()  # вызывает конструктор родителя (пустой)
        self.name = name
        self.username = username
        self.status = status

    # Полиморфизм: переопределяем метод info
    def info(self):
        print(f"VIP пользователь: {self.name}, ник: {self.username}, статус: {self.status}")


# Проверка
user = BaseUser()
vip = VipUser("Эльдияр", "eldiyar123", "online")

user.info()  # Это обычный пользователь
vip.info()   # VIP пользователь: Эльдияр, ник: eldiyar123, статус: online
